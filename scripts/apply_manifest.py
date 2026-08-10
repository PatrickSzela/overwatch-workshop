#!/usr/bin/env python3

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, cast

import tomllib


def rel_path(path: Path):
    return path.relative_to(Path.cwd())


def find_ds_toml(start: Path) -> Path:
    directory = start if start.is_dir() else start.parent

    for candidate in [directory, *directory.parents]:
        ds = candidate / "ds.toml"
        if ds.is_file():
            return ds

    raise FileNotFoundError(
        f"Could not find 'ds.toml' in '{rel_path(directory)}' or higher."
    )


def traverse_json(node: Any, key_path: list[str], json_path: Path) -> Any:
    path = rel_path(json_path)

    for key in key_path:
        if isinstance(node, list):
            node = cast(list[Any], node)

            if not key.lstrip("-").isdigit():
                raise TypeError(
                    f"{path}': expected an integer to access an array, got '{key}'."
                )

            index = int(key)

            if not -len(node) <= index < len(node):
                raise IndexError(
                    f"'{path}': index {index} out of range for array of length {len(node)}."
                )

            node = node[index]
        elif isinstance(node, dict):
            if key not in node:
                raise KeyError(f"'{path}': key '{key}' not found.")

            node = cast(Any, node[key])
        else:
            raise TypeError(
                f"'{path}': cannot traverse into {type(node).__name__} with key '{key}'."
            )

    return node


def replace_placeholders(content: str, ds_dir: Path) -> str:
    # Matches {{JSON_FILE_NAME.A.B.C}}
    # - group 1: JSON_FILE_NAME
    # - group 2: A.B.C
    placeholder = re.compile(r"\{\{([^.}{]+)\.([^}]+)\}\}")

    def replacer(match: re.Match[str]) -> str:
        file = match.group(1)
        key_path = match.group(2).split(".")
        json_file = ds_dir / f"{file}.json"

        if not json_file.is_file():
            raise FileNotFoundError(f"File '{file}.json' doesn't exists.")

        data = json.loads(json_file.read_text(encoding="utf-8"))
        return str(traverse_json(data, key_path, json_file))

    return placeholder.sub(replacer, content)


def apply_manifest():
    parser = argparse.ArgumentParser(
        description="Helper script for replacing {{JSON_FILE.A.B.C}} with corresponding value in the JSON file placed next to ds.toml"
    )

    parser.add_argument(
        "file",
        type=Path,
        help="Path to a file",
    )

    args = parser.parse_args()
    file = args.file.resolve()

    try:
        if not file.exists():
            raise FileNotFoundError(f"File '{file}' doesn't exists.")

        ds_toml_path = find_ds_toml(file)
        app_dir = ds_toml_path.parent
        print(f"Found 'ds.toml' at '{rel_path(ds_toml_path)}'")

        ds_toml = tomllib.loads(ds_toml_path.read_text(encoding="utf-8"))

        if "out_file" not in ds_toml:
            sys.exit("Error: 'out_file' key not found in ds.toml.")

        out_file = (app_dir / ds_toml["out_file"]).resolve()

        if not out_file.is_file():
            sys.exit(f"Error: out_file '{rel_path(out_file)}' does not exist.")

        print(f"Found 'out_file' at '{rel_path(out_file)}'")

        out_file_contents = out_file.read_text(encoding="utf-8")
        result = replace_placeholders(out_file_contents, app_dir)

        out_file.write_text(result, encoding="utf-8")
        print("Updated 'out_file'")

        return result
    except (FileNotFoundError, KeyError, TypeError, IndexError) as e:
        sys.exit(f"Error: {repr(e)}")


if __name__ == "__main__":
    apply_manifest()
