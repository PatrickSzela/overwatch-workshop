### (Not So) Simple Menu

**_(Not So) Simple Menu_** is a fully featured menu system that allows you to execute some built-in actions at runtime, without the need of fiddling around in Workshop Editor and restarting the match every time you make a change in the code.

It allows you to:

- Create dummy bots
- Change players hero or send them to Hero Select screen
- Teleport players:
  - to a selected position
  - to payload or objective
  - to another player
- Set looking position of players (once or over time):
  - to a selected position
  - to payload or objective
  - to another player
  - to looking position of other player
- Apply statuses (Asleep, Hacked, Unkillable, Phased out, etc.)
- Control abilities:
  - press, hold, or spam button
  - set current and max ammo, cooldown, resource or charge
  - enable infinite ammo, cooldown, resource or charge
- Set current health or max health, enable auto heal
- Display info about player's health, position, speed, pressed buttons etc.
- Show healing and damage taken by other players
- and more...

Most of these actions can also be added to the **Timeline**, which allows you to create a playable action set that can be played on repeat even with the menu itself being closed.

#### Custom Game Settings

Because, as of the day of writing this, the Custom Game menus are pretty broken, and precompiled settings cannot even be imported, after compiling and importing the code, you must change these settings manually, in the specified order:

1. **Modes:**

- Disable all modes and enable **Skirmish** _(optional)_
- For every enabled mode:
  - Set **Enable Perks** to `On` _(optional)_
- Open **All** menu:
  - Set **Game Mode Start** to `Manual` _(optional)_
  - Set **Hero Limit** to `Off`
  - Set **Limit Roles** to `Off`
  - Set **Respawn Time Scalar** to `0%` _(optional)_
  - Set **Tank Role Passive Health Bonus** to `1 Tank, 2 Offense, 2 Support` _(optional)_

2. **Maps:**

- Disable every map except for **Workshop Island (Night)** _(optional)_
