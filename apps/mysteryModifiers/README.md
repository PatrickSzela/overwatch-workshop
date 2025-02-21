### Who doesn't love some chaos?

Charge the global meter by dealing damage, healing and using ultimate.
Once the meter is fully charged, the same randomly selected modifier will be applied to each player.

**New:** Now also with Twitch integration! Instead of charging the meter, let your chat vote on the next modifier - [external application](https://github.com/PatrickSzela/overwatch-workshop-integrations) required

More information about the Workshop mode available on the [Workshop.codes](https://workshop.codes/mystery-modifiers) website

Source code written in [OSTW](https://github.com/ItsDeltin/Overwatch-Script-To-Workshop)

#### Custom Game Settings

Because, as of the day of writing this, the Custom Game menus are pretty broken, and precompiled settings cannot even be imported, after compiling and importing the code, you must change these settings manually, in the specified order:

1. **Modes:**

- Enable **all, normally available** modes - if the modes are duplicated, load `Quick Play` preset and remember which modes are enabled, then enable the exact same modes in this step. Optionally also enable **Competitive Rules** for these modes too
- Disable **Skirmish** and **Deathmatch** mode - these are only enabled as a workaround so we can import the code _(optional)_
- Open **All** menu:
  - Set **Game Mode Start** to `Manual`
  - Set **Hero Limit** to `1 per team` _(optional)_
  - Set **Limit Roles** to `1 Tank, 2 Offense, 2 Support` _(optional)_
  - Set **Tank Role Passive Health Bonus** to `1 Tank, 2 Offense, 2 Support` _(optional)_

2. **Lobby:**

- Set **Max Team 1 Players** and **Max Team 2 Players** to `5`
- Set **Max FFA Players** to `10`
- Set **Max Spectators** to `12` _(optional)_
