import json
import os
from datetime import date
from typing import Any
import argparse

class Box:
    def __init__(
        self, Orientation: list[float], Translation: list[float], Extents: list[float]
    ) -> None:
        self.orientation = Orientation
        self.translation = Translation
        self.extents = Extents


class Area:
    def __init__(self, UUID: str, Boxes: list[Any]) -> None:
        self.uuid = UUID
        self.boxes = [Box(**box) for box in Boxes]


class Map:
    def __init__(self, name: str, mode: str, areas: list[Any]) -> None:
        self.name = name
        self.mode = mode
        self.areas = [Area(**area) for area in areas]
        self.max_box_count = max([len(area.boxes) for area in self.areas])


type Data = dict[str, dict[str, Map]]


def format_floats_in_array(array: list[float]):
    return [format(x, ".8f") for x in array]

def array_to_vector(array: list[Any]):
    return f"Vector({', '.join(format_floats_in_array(array))})"


def output_ostw_rule(map_name: str, mode: str, area: Area, max_box_count: int):
    orientations = json.dumps([format_floats_in_array(box.orientation) for box in area.boxes]).replace('"', '')
    translations = json.dumps([array_to_vector(box.translation) for box in area.boxes]).replace('"', '')
    extents = json.dumps([array_to_vector(box.extents) for box in area.boxes]).replace('"', '')

    return f'''rule: "{map_name} - {area.uuid}"
if("{map_name}" == ToString(CurrentMap()))
if("{mode}" == ToString(CurrentGameMode()))
if(DistanceBetween({array_to_vector(area.boxes[0].translation)}, ObjectivePosition(ObjectiveIndex())) < 20)
{{
  orientations = {orientations};
  translations = {translations};
  extents = {extents};
  maxBoxCount = {max_box_count};
}}
'''

# TODO: split output into multiple files (per mode)

def main():
    parser = argparse.ArgumentParser(
        prog="generate-data.py",
        description="Generate data.del file based on Areas.json file containing control point boundaries data extracted with datatool.",
    )
    parser.add_argument("path", help="path to Areas.json file")
    args = parser.parse_args()
    file_path = args.path

    script_dir = os.path.dirname(os.path.abspath(__file__))
    # output_path_json = os.path.join(script_dir, "data.json")
    output_path = os.path.join(script_dir, "data.del")
    total_max_box_count = 0

    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            data = json.load(f)

        output_data: Data = {}

        for _i, mapData in enumerate(data):
            if not isinstance(mapData, dict):
                print("Map data is not a dictionary")
                return

            if not isinstance(mapData["MapName"], str) or not isinstance(
                mapData["Areas"], list
            ):
                return

            name, _lightning, mode, *rest = mapData["MapName"].split(" - ")

            # some maps names have hardcoded information about their variant (for example, "Busan - Sanctuary"), so let's skip these by checking if string after the 2nd ` - ` contains a mode's name
            # this should prob be handled better in case blizzard adds a map with ` - ` in its name to one of the core gamemodes
            if mode.lower() not in (
                "control",
                "assault",
                "flashpoint",
                "hybrid",
                "clash",
            ):
                continue

            if len(rest):
                # additional data usually means the map belongs to some limited-time event, and we don't care about these
                continue

            if mode not in output_data:
                output_data[mode] = {}

            data = Map(name, mode, mapData["Areas"])  # type: ignore

            if mode in output_data and name in output_data[mode]:
                # check if duplicated map has the same boxes
                uuids = [i.uuid for i in data.areas]
                uuids2 = [i.uuid for i in output_data[mode][name].areas]

                if uuids != uuids2:
                    print("Duplicated map {name} found, but boxes UUIDs differ!")
                    print(uuids)
                    print(uuids2)

                continue

            total_max_box_count = max(total_max_box_count, *[len(area.boxes) for area in data.areas])

            output_data[mode][name] = data

        #with open(output_path_json, "w") as f:
        #    json.dump(output_data, f, indent=2, default=vars)

        # output to .del file
        rules: list[str] = [
            f'globalvar String importDate = "{str(date.today())}";\n',
        ]
        for mode, maps in output_data.items():
            for map, mapData in maps.items():
                for _idx, area in enumerate(mapData.areas):
                    rules.append(output_ostw_rule(map, mode, area, mapData.max_box_count))

        with open(output_path, "w") as f:
            f.write("\n".join(rules))

        print(f"Max boxes count: {total_max_box_count}")


if __name__ == "__main__":
    main()
