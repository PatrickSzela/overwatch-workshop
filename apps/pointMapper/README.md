### Point Mapper

Automatically map more accurate boundaries of control points. A spiritual successor to my previous mode [Control Point Boundaries](https://workshop.codes/WNSY6).

With the default (2.5 cm) accuracy, it takes around 30 secs to 1 min to map the outline of the objective, depending on its size. For this reason, this tool only maps boundaries at the ground level.

> [!NOTE]
> Because of in-game limitations, with every subsequent run the chance to crash the server gets higher. In game modes with multiple control points, it might be preferable to set _Limit Valid Control Points_ setting to a preferred control point

More information about the Workshop mode available on the [Workshop.codes](https://workshop.codes/point-mapper/) website

Source code written in [OSTW](https://github.com/ItsDeltin/Overwatch-Script-To-Workshop)

#### Custom Game Settings

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

- Set **Max Team 1 Players** and **Max Team 2 Players** to `1`
- Set **Max Spectators** to `12` _(optional)_
- Set **Allow Players Who Are In Queue** to `Yes` _(optional)_

3. **Heroes:**

- Open **General** menu:
  - Set **Ability Cooldown Time** to `0%`
