### Point Boundaries

Displays precise Control Point boundaries. A spiritual successor to my previous mode [Control Point Boundaries](https://workshop.codes/WNSY6).

**Import code:** `WXAMY`

More information about the Workshop mode available on the [Workshop.codes](https://workshop.codes/point-boundaries/) website

Source code written in [OSTW](https://github.com/ItsDeltin/Overwatch-Script-To-Workshop)

#### Updating boundaries data

1. Extract map objectives data (`extract-map-objectives` mode) with [DataTool](https://github.com/overtools/OWLib)
2. Execute script `generate-data.py <PATH>`, where `<PATH>` points to the extracted `Areas.json` file from 1st point
3. Compile `main.del` file
