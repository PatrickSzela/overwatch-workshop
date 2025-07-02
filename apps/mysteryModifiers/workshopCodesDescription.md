### **_Who doesn't love some chaos?_**

Charge the global meter by dealing damage, healing and using ultimate.
Once the meter is fully charged, the same randomly selected modifier will be applied to each player.

**==New:==** Now also with Twitch integration! Instead of charging the meter, let your chat vote on the next modifier - [external application](https://github.com/PatrickSzela/overwatch-workshop-integrations) required

### **Available modifiers:**

<div class="modifiers">
	<div class="modifier">
		<div class="modifier__header">
			<div class="modifier__title">Adaptive Shield</div>  
			<div class="modifier__duration">7 secs</div>
		</div>
		<div class="modifier__content">
			<div class="modifier__description">
				<p>Creates temporary extra health that increases with more nearby enemies</p>
			</div>
			<ul class="update-notes__changes">
				<li>
          Adds 100 base overhealth and 100 additional overhealth per every enemy within 10 meter radius
        </li>
			</ul>
		</div>
	</div>

  <div class="modifier">
		<div class="modifier__header">
			<div class="modifier__title">Ana's Sleep Dart Paintball<span>[1][2][3]</span></div>  
			<div class="modifier__duration">15 secs</div>
		</div>
		<div class="modifier__content">
			<div class="modifier__description">
				<p>
          Sleep Dart instantly kills a victim. Greatly accelerates Sleep Dart cooldown, and getting an elimination resets it
        </p>
			</div>
			<ul class="update-notes__changes">
        <li>Switches player's hero to Ana</li>
        <li>Speeds up Sleep Dart cooldown to 500%</li>
        <li>Getting an elimination instantly restores Sleep Dart cooldown</li>
        <li>Increases ammunition count to 1000</li>
        <li>Disables usage of Biotic Grenade</li>
			</ul>
		</div>
	</div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">Anti-Heal</div>  
      <div class="modifier__duration">5 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>Prevents everyone from being healed</p>
      </div>
      <ul class="update-notes__changes">
        <li>Reduces healing received to 0%</li>
      </ul>
    </div>
  </div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">Baby D.Va<span>[1][2][3]</span></div>  
      <div class="modifier__duration">15 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>No mech? No problem!</p>
      </div>
      <ul class="update-notes__changes">
        <li>Switcher player's hero to D.Va and forcefully takes them out of the mech</li>
        <li>Disables usage of Call Mech</li>
      </ul>
    </div>
  </div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">Blinded</div>  
      <div class="modifier__duration">8 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>Everyone's vision becomes obstructed</p>
      </div>
      <ul class="update-notes__changes">
        <li>
          Creates a black blob in front of every player's eyes, obstructing their vision
        </li>
        <li>Disables outlines and nameplates of other players</li>
      </ul>
    </div>
  </div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">Body Odor</div>  
      <div class="modifier__duration">10 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>Standing close to other players will deal damage over time to them</p>
      </div>
      <ul class="update-notes__changes">
        <li>
          Creates area of effect around players with radius of 5 meters that deals 35 damage per second to other players, including teammates
        </li>
      </ul>
    </div>
  </div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">Drunk</div>  
      <div class="modifier__duration">15 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>An alcohol intoxication symptoms include: trouble walking, loss of balance and slowed down brain functions</p>
      </div>
      <ul class="update-notes__changes">
        <li>
          Adds random throttle to players in random directions, without overriding their requested movement direction
        </li>
        <li>Randomly applies Knocked Down status every few seconds</li>
        <li>Slows down time to 85%</li>
      </ul>
    </div>
  </div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">Duplicate - Random Hero<span>[1][2][3]</span></div>  
      <div class="modifier__duration">15 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>Become a copy of a random hero. Greatly accelerates Ultimate generation</p>
      </div>
      <ul class="update-notes__changes">
        <li>
          Switches every player's hero to the same, randomly selected hero that isn't currently being played by anyone in the lobby
        </li>
        <li>Speeds up Ultimate generation to 550%</li>
      </ul>
    </div>
  </div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">Emote<span>[3]</span></div>  
      <div class="modifier__duration">5 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>Forces the use of an emote</p>
      </div>
      <ul class="update-notes__changes">
        <li>Triggers usage of Emote Up</li>
        <li>Disables ability of cancelling the Emote until timer runs out (thanks to the Season 14 mid-season change)</li>
        <li>
          Because Emotes cannot be used while in the air, for players not on the ground this modifier will be delayed until they (forcefully) land... assuming they don't die in the process
        </li>
        <li>
          Players unable to Emote because of being in alternate form (Rammatra's Nemesis Form, Bastion's Configuration: Recon etc) will be frozen in place and be unable to use any abilities until they can Emote or the modifier ends
        </li>
      </ul>
    </div>
  </div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">Energized</div>  
      <div class="modifier__duration">10 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>Accelerates movement speed, cooldowns, resources and Ultimate generation</p>
      </div>
      <ul class="update-notes__changes">
        <li>Increases move speed to 130%</li>
        <li>Speeds up cooldowns to 200%</li>
        <li>Speeds up resource restoration to 200%</li>
        <li>Speeds up Ultimate generation to 200%</li>
      </ul>
    </div>
  </div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">Floor Is Lava</div>  
      <div class="modifier__duration">10 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>The ground is made of lava. And lava is hot... very hot</p>
      </div>
      <ul class="update-notes__changes">
        <li>
          Standing on the ground will apply burning effect to a player and deal 50 damage over time
        </li>
      </ul>
    </div>
  </div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">Go Forward</div>  
      <div class="modifier__duration">10 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>Forces players to go forward</p>
      </div>
      <ul class="update-notes__changes">
        <li>
          Forces players to go forward, while also allowing them to control their horizontal direction
        </li>
      </ul>
    </div>
  </div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">Gravity - High</div>  
      <div class="modifier__duration">10 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>Greatly increases gravity</p>
      </div>
      <ul class="update-notes__changes">
        <li>Increases player gravity to 200%</li>
        <li>Increases projectile gravity to 200%</li>
      </ul>
    </div>
  </div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">Gravity - Low</div>  
      <div class="modifier__duration">10 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>Greatly lowers gravity</p>
      </div>
      <ul class="update-notes__changes">
        <li>Decreases player gravity to 37.5%</li>
        <li>Decreases projectile gravity to 37.5%</li>
      </ul>
    </div>
  </div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">Hacked</div>  
      <div class="modifier__duration">5 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>Stops players from using their abilities</p>
      </div>
      <ul class="update-notes__changes">
        <li>
          Hacks players, disabling usage of their abilities and stopping any channeled abilities currently in use
        </li>
      </ul>
    </div>
  </div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">Health-Bound Size<span>[4]</span></div>  
      <div class="modifier__duration">10 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>Players' size depends on their current health</p>
      </div>
      <ul class="update-notes__changes">
        <li>Scales players' size gradually, depending on their health, starting from 200% when at full health, to 50% when at 0 health</li>
      </ul>
    </div>
  </div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">Health-Bound Speed</div>  
      <div class="modifier__duration">10 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>Players' speed depends on their current health</p>
      </div>
      <ul class="update-notes__changes">
        <li>Scales players' speed gradually, depending on their health, starting from 100% when at full health, to 200% when at 0 health</li>
      </ul>
    </div>
  </div>
  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">Hypothermia</div>  
      <div class="modifier__duration">15 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>
          Keep yourself warm or you'll freeze! Moving around, standing near others and setting yourself on fire will help you stay warm
        </p>
      </div>
      <ul class="update-notes__changes">
        <li>Adds new progress bar on screen displaying current Freeze percentage</li>
        <li>Freeze percentage grows over time, with base value of 20% per second</li>
        <li>Player's movement speed decreases based on their Freeze percentage</li>
        <li>Once Freeze percentage reaches 100%, player gains Frozen status and are unable to control their character</li>
        <li>Players can slow down the rate at which their Freeze percentage grows, and even cause it to decrease, depending on whether they are:
          <ul>
            <li>moving,</li>
            <li>burning,</li>
            <li>phased out,</li>
            <li>invincible,</li>
            <li>nearby other players (in 2.5 meter radius)</li>
          </ul>
        </li>
        <li>
          Frozen players can get unfrozen by other players by standing near them or moving them
        </li>
      </ul>
    </div>
  </div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">Ice Rink</div>  
      <div class="modifier__duration">10 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>The ground is made of ice, causing everyone to slide</p>
      </div>
      <ul class="update-notes__changes">
        <li>
          Causes players to slide while on the ground, depending on the direction they are looking at
        </li>
      </ul>
    </div>
  </div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">Inverted Controls</div>  
      <div class="modifier__duration">10 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>Movement controls are inverted</p>
      </div>
      <ul class="update-notes__changes">
        <li>Inverts movement controls of players</li>
      </ul>
    </div>
  </div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">Invisibility</div>  
      <div class="modifier__duration">10 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>Gain invisibility and increased movement speed. Taking damage or standing near others will reveal you</p>
      </div>
      <ul class="update-notes__changes">
        <li>Players become invisible to other players</li>
        <li>Increases players' move speed to 160%</li>
        <li>
          Standing near other players in 4 meter radius or taking damage will reveal you
        </li>
      </ul>
    </div>
  </div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">Jet Pack</div>  
      <div class="modifier__duration">15 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>Hold the Jump button to gain height, while also consuming fuel. Fuel regenerates after a short duration of not using it</p>
      </div>
      <ul class="update-notes__changes">
        <li>Grants ability to fly, by holding the Jump button</li>
        <li>Adds new progress bar on screen displaying current Fuel percentage</li>
        <li>Fuel percentage gets consumed over time while using Jet Pack, with base value of 20% per second</li>
        <li>Fuel percentage regenerates over time after 0.5 seconds of not using the Jet Pack, with base value of 40% per second</li>
        <li>Increases move speed to 120% while Jet Pack is in use</li>
      </ul>
    </div>
  </div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">Lagging</div>  
      <div class="modifier__duration">10 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>Randomly teleport back in time to your previous location</p>
      </div>
      <ul class="update-notes__changes">
        <li>Players get randomly teleported back in time to their previous location</li>
      </ul>
    </div>
  </div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">Laser Eyes</div>  
      <div class="modifier__duration">10 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>Gain ability to emit beams of energy from your eyes, dealing damage over time to a player you look at</p>
      </div>
      <ul class="update-notes__changes">
        <li>
          Players gain ability to emit laser beams from their eyes, while also dealing 25 damage over time to the player they are looking at, including teammates
        </li>
      </ul>
    </div>
  </div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">Low Visibility</div>  
      <div class="modifier__duration">10 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>Greatly reduces visibility range</p>
      </div>
      <ul class="update-notes__changes">
        <li>Creates black spheres around players, reducing their visibility</li>
        <li>
          Visibility starts being reduced at 10 meters away from players, reaching minimal visibility at 20 meters
        </li>
        <li>Disables outlines and nameplates of other players 11.5 meters away from the player</li>
      </ul>
    </div>
  </div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">Moth War<span>[1][2][3]</span></div>  
      <div class="modifier__duration">15 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>Dr. Ziegler became fed up with healing others, and decided to take matters into her own hands</p>
      </div>
      <ul class="update-notes__changes">
        <li>Switcher player's hero to Mercy and triggers Valkyrie</li>
        <li>Increases damage dealt to 200%</li>
        <li>Disables usage of Caduceus Staff</li>
        <li>Disables usage of Resurrect</li>
      </ul>
    </div>
  </div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">Nano Boost</div>  
      <div class="modifier__duration">8 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>Increases damage output. Heals upon activation</p>
      </div>
      <ul class="update-notes__changes">
        <li>Heals players by 250 HP</li>
        <li>Increases damage dealt to 150%</li>
      </ul>
    </div>
  </div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">No HUD</div>  
      <div class="modifier__duration">10 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>HUD and player outlines are disabled</p>
      </div>
      <ul class="update-notes__changes">
        <li>Hides most of the UI elements</li>
        <li>Disables other players outlines</li>
      </ul>
    </div>
  </div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">Player Size - Big<span>[4]</span></div>  
      <div class="modifier__duration">10 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>Greatly increases the size of players</p>
      </div>
      <ul class="update-notes__changes">
        <li>Increases player's size to 200%</li>
      </ul>
    </div>
  </div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">Player Size - Small<span>[4]</span></div>  
      <div class="modifier__duration">10 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>Greatly reduces the size of players</p>
      </div>
      <ul class="update-notes__changes">
        <li>Reduces player's size to 50%</li>
      </ul>
    </div>
  </div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">Primal Rage<span>[1][2][3]</span></div>  
      <div class="modifier__duration">10 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>Winton is angy</p>
      </div>
      <ul class="update-notes__changes">
        <li>Switches player's hero to Winston and triggers Primal Rage</li>
        <li>Reduces Player's maximum health to 350 HP</li>
      </ul>
    </div>
  </div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">Red Light, Green Light</div>  
      <div class="modifier__duration">15 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>Don't move or use abilities once light turns red</p>
      </div>
      <ul class="update-notes__changes">
        <li>Creates a ring of light around player's screen</li>
        <li>
          The ring will randomly switch from green, to red, and back to green at random intervals, at the same time for every player. First green light is guaranteed to always last 4 seconds
        </li>
        <li>
          While the ring is green, players are allowed to move around and use abilities
        </li>
        <li>
          While the ring is red, players are not allowed to move or start/stop using abilities. Players who fail to fulfill these requirements will be killed
        </li>
        <li>Players in the Invincible or Phased Out states can survive being killed</li>
        <li>
          Players who applied knockback to other players will get the kill credit if the victim dies due to movement during red light
        </li>
      </ul>
    </div>
  </div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">Sigma Dodgeball<span>[1][2][3]</span></div>  
      <div class="modifier__duration">15 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>Greatly increases damage and accelerates cooldown of Accretion. Getting an elimination resets Accretion's cooldown. Grants ability to fly and reduces the size of shield</p>
      </div>
      <ul class="update-notes__changes">
        <li>Switches player's hero to Sigma</li>
        <li>Grants ability to fly, by holding the Jump button</li>
        <li>Increases damage dealt to 1000%</li>
        <li>Speeds up Accretion cooldown to 1000%</li>
        <li>Getting an elimination instantly resets Accretion cooldown</li>
        <li>Scales barrier down to 50%</li>
        <li>Overrides usage of Hyperspheres with Accretion</li>
        <li>Disables usage of Kinetic Grasp</li>
        <li>Disables usage of Gravitic Flux</li>
        <li>Disables usage of melee</li>
      </ul>
    </div>
  </div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">Sleep</div>  
      <div class="modifier__duration">5 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>Puts players to Sleep. Taking damage will wake you</p>
      </div>
      <ul class="update-notes__changes">
        <li>Puts players to Sleep</li>
        <li>Players who take damage while slept will get woken up</li>
        <li>Because of a bug that makes tanks immune to the Sleep status applied with Workshop, it had to be recreated manually - expect minor issues</li>
      </ul>
    </div>
  </div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">Slow Motion</div>  
      <div class="modifier__duration">10 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>Greatly slows down the time</p>
      </div>
      <ul class="update-notes__changes">
        <li>Slows down the time to 50%</li>
      </ul>
    </div>
  </div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">Speed Boost</div>  
      <div class="modifier__duration">10 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>Greatly increases movement speed</p>
      </div>
      <ul class="update-notes__changes">
        <li>Increases player speed to 200%</li>
      </ul>
    </div>
  </div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">Spider-Woman<span>[1][2][3]</span></div>  
      <div class="modifier__duration">15 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>With purple skin... comes a requirement for airborne kills</p>
      </div>
      <ul class="update-notes__changes">
        <li>Switches player's hero to Widowmaker</li>
        <li>Disables Secondary Fire (scoped shots) while on ground</li>
        <li>Speeds up Grapple Hook cooldown to 500%</li>
        <li>Getting an elimination instantly restores Grapple Hook cooldown</li>
      </ul>
    </div>
  </div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">Sunburn</div>  
      <div class="modifier__duration">13 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>Increased Sun activity detected. Seek shelter immediately</p>
      </div>
      <ul class="update-notes__changes">
        <li>Players not standing under any cover take 35 damage over time</li>
        <li>Players in the Phased Out or Invincible states are immune</li>
      </ul>
    </div>
  </div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">T-Bagging</div>  
      <div class="modifier__duration">10 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>Your crouch button might be broken...</p>
      </div>
      <ul class="update-notes__changes">
        <li>Randomly forces players on the ground to crouch for a very short period of time</li>
      </ul>
    </div>
  </div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">The Voices<span>[3]</span></div>  
      <div class="modifier__duration">10 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>Hello. Thanks. Boop! Good kitty. Boo boo doo de doo. Sigh...</p>
      </div>
      <ul class="update-notes__changes">
        <li>Forces usage of randomly chosen communication method (voice lines, hello, thank you etc.)</li>
      </ul>
    </div>
  </div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">Third Person Camera</div>  
      <div class="modifier__duration">13 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>Forces Third Person Camera</p>
      </div>
      <ul class="update-notes__changes">
        <li>Moves players' camera behind and above them</li>
        <li>Creates a red sphere that indicates the actual position at which the hero is looking at</li>
      </ul>
    </div>
  </div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">Top Down Camera</div>  
      <div class="modifier__duration">13 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>Forces Top Down Camera</p>
      </div>
      <ul class="update-notes__changes">
        <li>Moves players' camera 15 meters above their heads</li>
        <li>Disables ability to aim upwards</li>
        <li>Creates a red sphere that indicates the actual position at which the hero is looking at</li>
      </ul>
    </div>
  </div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">Torbjörn's Forge Hammer War<span>[1][2][3]</span></div>  
      <div class="modifier__duration">15 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>It's Hammer time!</p>
      </div>
      <ul class="update-notes__changes">
        <li>Switches player's hero to Torbjörn</li>
        <li>Disables usage of Rivet Gun</li>
        <li>Disables usage of Deploy Turret</li>
      </ul>
    </div>
  </div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">Trampoline</div>  
      <div class="modifier__duration">10 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>Touching the ground will launch you upwards</p>
      </div>
      <ul class="update-notes__changes">
        <li>While touching the ground, the player is launched upwards into the air, with randomized strength</li>
      </ul>
    </div>
  </div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">Use Ultimate</div>  
      <div class="modifier__duration">10 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>Fully charges and forces usage of the Ultimate ability</p>
      </div>
      <ul class="update-notes__changes">
        <li>Grants every player 100% Ultimate charge and forcefully triggers it</li>
        <li>
          Players with Ultimates that have some kind of requirement - like looking at another player or pressing a confirmation input - will be forced to keep pressing the Ultimate button until it's successfully used
        </li>
      </ul>
    </div>
  </div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">Weakened</div>  
      <div class="modifier__duration">10 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>Lowers move speed, cooldowns, resources and ultimate charge generation. Increased damage and lowered healing received. Slightly increased gravity</p>
      </div>
      <ul class="update-notes__changes">
        <li>Increases damage received to 125%</li>
        <li>Decreases healing received to 75%</li>
        <li>Decreases move speed to 75%</li>
        <li>Increases gravity to 125%</li>
        <li>Slows down cooldowns to 75%</li>
        <li>Slows down resource restoration to 75%</li>
        <li>Slows down Ultimate generation to 75%</li>
      </ul>
    </div>
  </div>

  <div class="modifier">
    <div class="modifier__header">
      <div class="modifier__title">Vampiric Exchange</div>  
      <div class="modifier__duration">10 secs</div>
    </div>
    <div class="modifier__content">
      <div class="modifier__description">
        <p>Dealing damage to other players heals you, but healing others depletes your health</p>
      </div>
      <ul class="update-notes__changes">
        <li>25% of damage done to other Players gets converted into self-healing</li>
        <li>50% of healing done to other Players gets converted into self-damage </li>
      </ul>
    </div>
  </div>
</div>

##### **References**

<ol class="references">
  <li>After this Modifier ends, player's health and Ultimate charge are restored from before the Modifier was applied</li>
  <li>Dying while this Modifier is active cancels it prematurely for that specific player and restores their Ultimate charge</li>
  <li>Because of Workshop limitations, this Modifier won't work properly on AI bots</li>
  <li>Due to a Workshop bug, player's nameplates do not scale properly</li>
</ol>

### **Available Settings**

| Section                       | Name                                                        | Default value      |
| ----------------------------- | ----------------------------------------------------------- | ------------------ |
| Global                        | Modifiers are controlled by                                 | Game               |
| Global - Controlled by Game   | Points required to trigger modifier                         | 50                 |
| Global - Controlled by Game   | Percentage above which to decrease points over time         | 75                 |
| Global - Controlled by Game   | Rate at which decrease points over time                     | 0.50               |
| Global - Controlled by Game   | Percentage of damage done that will be converted to Points  | 1.25               |
| Global - Controlled by Game   | Percentage of healing done that will be converted to Points | 1.00               |
| Global - Controlled by Game   | Points to grant per Ultimate usage                          | 2                  |
| Global - Controlled by Game   | Hide Modifier charge meter                                  | Off                |
| Global - Controlled by Stream | Poll duration in seconds                                    | 30                 |
| Global - Controlled by Stream | Start poll                                                  | When Modifier ends |
| Global - Controlled by Stream | Show poll HUD in-game                                       | On                 |
| Modifier                      | Global modifier duration scalar                             | 1                  |
| Modifier                      | \<Modifier name\> toggle                                    | On                 |

Source code for [this Workshop mode](https://github.com/PatrickSzela/overwatch-workshop/tree/main/apps/mysteryModifiers) and [the external application](https://github.com/PatrickSzela/overwatch-workshop-integrations) are available on GitHub

<style>
  .modifiers {
    border: 2px solid #4c555b !important;
  }

  .modifier {
    border-bottom: 2px solid #4c555b;
    background-color: #1f2326;
  }
    
  .modifier:last-child {
    border-bottom: none;
  }
    
  .modifier__header {
    padding: 0.75rem 1rem;
    background: #292e31;
    display: flex;
    gap: 8px;
    align-items: baseline;
  }
    
  .modifier__title {
    font-size: 1.115rem;
    color: #e4e6e7;
    line-height: 1.5rem;
    font-weight: bold;
  }

  .modifier__title span {
    vertical-align: super;
    font-size: x-small;
    line-height: 1;
  }

  .modifier__duration {
    font-size: smaller;
    line-height: 1;
  }
    
  .modifier__content {
    padding: 1rem;
  }
    
  .modifier__description {
    border-left: 4px solid var(--primary);
    padding-left: 1rem;
    margin-bottom: 1rem;
  }

  .references li::marker {
    content: "[" counter(list-item) "] ";
    color: var(--primary);
  }

  .references li::before {
    content: "" !important;
  }
</style>
