### Classic vs Modern Heroes

Have you ever thought how the game would look like, if you could put classic Overwatch 1 heroes against modern Overwatch 2 ones, or even if you could mix them all together?
Well now you can, with configurable Self Healing and Tank Bonus Health passives!

> [!NOTE]
> This mode doesn't recreate nor it magically brings back the "old" heroes. Instead, it relies on Blizzard reintroducing the classic heroes in their time-limited events. Once the time-limited event is gone, this mode **will no longer function**, until the next Classic event is introduced.

More information about the Workshop mode available on the [Workshop.codes](https://workshop.codes/5KMTT) website

Source code written in [OSTW](https://github.com/ItsDeltin/Overwatch-Script-To-Workshop)

#### Custom Game Settings

Because, as of the day of writing this, the Custom Game menus are pretty broken, and precompiled settings cannot even be imported, after compiling and importing the code, you must change these settings manually, in the specified order:

1. **Modes:**

- Enable **Classic** modes - if the modes are duplicated, load _Overwatch: Classic_ preset (if available) and remember which modes are enabled, then enable the exact same modes in this step. Optionally also enable **Competitive Rules** for these modes too
- Disable **Practice Range** mode - this mode is only enabled as a workaround so we can import the code
- Open **All** menu:
  - Set **Tank Role Passive Health Bonus** to `Disabled`
  - Set **Hero Limit** to `1 per team` _(optional)_
  - Set **Limit Roles** to `Off` _(optional)_

2. **Lobby:**

- Set **Max Team 1 Players** and **Max Team 2 Players** to `6` _(optional)_
- Set **Max Spectators** to `12` _(optional)_

3. **Heroes:**

- Set **Passive Health Regeneration** to `Disabled`
