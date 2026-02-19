### Point Boundaries

Displays precise Control Point boundaries. A spiritual successor to my previous mode [Control Point Boundaries](https://workshop.codes/WNSY6).

**Import code:** `WXAMY`

More information about the Workshop mode available on the [Workshop.codes](https://workshop.codes/point-boundaries/) website

Source code written in [OSTW](https://github.com/ItsDeltin/Overwatch-Script-To-Workshop)

#### Updating boundaries data

1. Extract map objectives data (`extract-map-objectives` mode) with [DataTool](https://github.com/overtools/OWLib)
2. Execute script `generate-data.py <PATH>`, where `<PATH>` points to the extracted `Areas.json` file from 1st point
3. Compile `main.del` file

#### Settings to apply after pasting compiled code

Because, as of the day of writing this, the Custom Game menus are pretty broken, and precompiled settings cannot even be imported, after compiling and importing the code, you must change these settings manually, in the specified order:

1. **Modes:**

- Enable **all modes that use Control Points** - if the modes are duplicated, load `Quick Play` preset and remember which modes are enabled, then enable the exact same modes in this step
- For every enabled mode, where applicable:
  - Set **Capture Speed Modifier** to `500%`
  - Set **Score To Win** to maximum available value
  - Set **Scoring Speed Modifier** to `500%`
- Open **All** menu:
  - Set **Game Mode Start** to `Immediately`
  - Set **Hero Limit** to `Off`
  - Set **Limit Roles** to `Off`
  - Set **Respawn Time Scalar** to `0%` _(optional)_

2. **Lobby:**

- Set **Max Spectators** to `12` _(optional)_
- Set **Allow Players Who Are In Queue** to `Yes` _(optional)_

3. **Heroes:**

- Open **General** menu:
  - Set **Ability Cooldown Time** to `0%`
- Open **Pharah** menu:
  - Set **Hover Jets Unlimited Fuel** to `Enabled`
