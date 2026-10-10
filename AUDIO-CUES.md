# Wicker: audio cue list

Each cue has an ID that will become its filename (for example `horn.ogg`). Where a cue already exists as a synthesised placeholder in the game, the ID is the same as the one the code calls with `sfx()`, so a recording can replace it without any rewiring. The length column gives a suggested duration in milliseconds. It is a target rather than a limit, and for loops it is the length of one seamless cycle.

**Delivery.**
- **Format:** mono WAV or OGG at 44.1 or 48 kHz. The game pans and attenuates positional sounds itself, so stereo is only worth it for the UI, music and ambience cues marked "stereo".
- **Variants:** cues marked ×3 are heard so often that they want two or three takes. The game will pick one at random so that repetition doesn't grate.
- **Silence:** trim leading silence to nothing, because the sound fires on the frame the event happens. Leave natural tails on.
- **Levels:** normalise to about −3 dBFS peak and leave the mix balance to the game.

## Interface

| ID | What it is for | Length (ms) | Notes |
|---|---|---|---|
| `select` | Tapping a unit, a building tile or a spell | 120 | ×3. A dry wooden tick or a bone rattle. Heard constantly, so it should be soft. |
| `order` | A move or attack order accepted | 200 | ×3. Distinct from `select`: a short murmur or a stick on hide. |
| `deny` | An order or placement refused (no mana, bad ground) | 250 | A dull, low thud. Not a buzzer. |
| `toast` | A message appearing at the top of the screen | 300 | Very quiet. Optional; it may be better left silent. |
| `level-intro` | The campaign level card appearing | 2500 | Stereo. A single sustained note or a struck bell with a long tail. |
| `victory` | The Rejoice! sequence before the victory screen | 6000 | Stereo. Bells, voices, a rising drone, all three together. |
| `defeat` | The defeat screen | 4000 | Stereo. A falling drone, a single crow. |

## Ambience and music

| ID | What it is for | Length (ms) | Notes |
|---|---|---|---|
| `drone` | The constant bed under play (currently synthesised) | 30000 loop | Stereo. Low, slowly shifting, barely there. |
| `drone-all` | The bed during All-against-all | 30000 loop | Stereo. The same bed, darker and more urgent; it will crossfade from `drone`. |
| `wind` | General outdoor air, louder when zoomed out | 20000 loop | Stereo. |
| `water` | Lapping at shorelines when the camera is near the sea | 12000 loop | |
| `forest` | Birds and leaves when the camera is over trees | 15000 loop | Should feel slightly wrong: too still, one bird too many. |

## Villagers and the economy

| ID | What it is for | Length (ms) | Notes |
|---|---|---|---|
| `chop` | A villager cutting wood | 350 | ×3. An axe biting into wet wood. |
| `tree-fall` | A tree coming down | 1400 | |
| `build` | Villagers working on a building site | 400 | ×3. Mallet, rope, thatch being thrown. |
| `built` | A building finished | 1200 | A settling creak and a short communal "hey". |
| `breed` | A new villager born in a hut | 600 | Very quiet. A baby's cry, or something less literal. |
| `flee` | Housed villagers bursting out of a destroyed hut | 900 | A scattering of voices. |
| `desert` | A follower running away because dread is too high | 800 | A single figure's footsteps, a door. |

## Fighting

| ID | What it is for | Length (ms) | Notes |
|---|---|---|---|
| `hit` | A warrior's blow landing | 220 | ×3. Wood and flesh, not steel. |
| `arrow` | An archer loosing | 300 | ×3. String and flight. |
| `die` | A follower dying | 700 | ×3. Short and unshowy, because this happens a lot. |
| `horn` | An enemy wave setting out (the alarm) | 3500 | The most important warning in the game. A long, low animal horn. |
| `break` | An enemy attack breaking and running home | 1500 | Scattered shouts receding. |
| `charge` | A balloonist's explosive charge falling | 900 | A fizzing fuse, then silence (the `boom` follows). |
| `boom` | Any explosion: a charge landing, a building bursting | 1500 | |
| `bld-fall` | A building destroyed | 2000 | Timber and thatch collapsing. |
| `hedge-hack` | Enemies hacking at a blackthorn hedge | 400 | ×3. Bill-hook through thorn. |

## The Cunning Woman and her spells

| ID | What it is for | Length (ms) | Notes |
|---|---|---|---|
| `cast` | The Cunning Woman beginning any spell | 900 | A breath and a rising whisper. |
| `blast` | Blast | 800 | A rushing whump of fire. |
| `thunder` | Lightning | 2200 | A crack, then a long roll. |
| `swarm` | Plague of Flies | 6000 loop | Buzzing that swells and swirls. Loops for the spell's life (10 s). |
| `shield` | Shield | 1500 | A low, held hum. |
| `ghost` | Ghost Army appearing | 1800 | Breathy, wordless voices. |
| `ghost-pop` | A ghost vanishing when struck | 300 | ×3 |
| `bridge` | Land Bridge rising | 3000 | Grinding earth and draining water. |
| `flatten` | Flatten | 2500 | A long, low settling rumble. |
| `hypno` | Hypnotise | 2000 | A wavering, detuned chant. |
| `whirl` | Whirlwind | 8000 loop | Roaring air. Loops while the tornado wanders. |
| `bog` | Bog laid | 2000 | A wet gulp. It should be quiet, because the bog is meant to be hidden. |
| `bog-claim` | Someone drowning in a bog | 1200 | ×3. A struggle and a sucking under. |
| `bog-drain` | A bog using up its ten lives and draining away | 1500 | |
| `erode` | Erode | 2500 | Ground sinking, water rushing in. |
| `quake` | Earthquake | 4000 | The deepest sound in the game. |
| `fire` | Firestorm | 8000 loop | Crackle with intermittent impacts. |
| `angel` | Angel of Death present | 10000 loop | High, keening and unsettling. |
| `volcano` | Volcano rising | 6000 | Rumble building to an eruption. |
| `reincarnate` | The Cunning Woman returning after death | 2500 | A breath drawn in. |

## Sacrifice and ritual

| ID | What it is for | Length (ms) | Notes |
|---|---|---|---|
| `altar` | An offering at the forest altar | 1500 | Intimate: a knife, a gasp, leaves. |
| `wicker-load` | A victim placed in the wicker man | 600 | ×3. Creaking wicker, a muffled cry. |
| `wicker-burn` | The wicker man lit | 7000 | Fire taking, then voices. The big set piece. |
| `god-burn` | The Wicker God burning | 10000 | Bigger again, with a bestial bellow from the effigy. |
| `frenzy` | A tribe entering frenzy after a burning | 3000 | Drums and whooping, heard from that tribe's direction. |
| `oss-capture` | An oss seizing someone | 700 | A snort, a scuffle. |
| `fold-breed` | A captive born in a thrall fold | 600 | Quiet. |
| `fold-escape` | A captive escaping a fold | 800 | Running and a gate banging. |
| `maypole` | Dancing at the maypole | 12000 loop | Pipe and tabor, slightly off. Loops while a festival is on. |
| `queen-crowned` | A May Queen crowned | 3000 | A cheer and a bell. |
| `queen-sac` | A May Queen sacrificed, with the rooks rising | 5000 | Wings, a cry, and silence. |
| `ritual` | The Cunning Woman's entombment rite at a hollow hill | 15000 loop | A low chant that builds while the rite runs. |
| `entomb` | Entombment completing as the hill becomes a fortress | 5000 | Earth closing over, wicker groaning. |
| `oak-hang` | The Cunning Woman hanging in Herne's Oak | 10000 loop | Creaking bough and wind. Runs for the two minutes. |
| `hunt-wake` | The Wild Hunt waking | 4000 | Hounds and a horn, distinct from the enemy `horn`. |
| `hunt-roam` | The Wild Hunt passing nearby | 6000 loop | Distant baying and hooves. |
| `all-against-all` | All-against-all invoked | 8000 | Every horn at once, then the darker drone. |

## Specifics worth knowing

- The cues that matter most for play are `horn`, `bog-claim` and `die`, because they tell you something is happening off screen. They are worth getting right first.
- The loops (`swarm`, `whirl`, `fire`, `angel`, `maypole`, `ritual`, `oak-hang`, `hunt-roam`) need clean loop points, with no click where the end meets the start.
- The game currently synthesises 13 of these (`select`, `blast`, `quake`, `built`, `thunder`, `die`, `boom`, `arrow`, `swarm`, `horn`, `hit`, `chop` and `cast`). Everything else in this list is silent for now.
