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
| `wind` | General outdoor air, louder when zoomed out | 20000 loop | **In the game:** Simon's three-minute recording, looped seamlessly (22 kHz, 32 kb/s MP3, embedded). Not continuous: comes in for a minute or so in the calm after a fight, or after a long quiet, and leaves when fighting starts. |
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
| `whirl-take` | The whirlwind tearing a building out whole | 2500 | Timber wrenched apart and sucked upward. |
| `bog` | Bog laid | 2000 | A wet gulp. It should be quiet, because the bog is meant to be hidden. |
| `bog-claim` | Someone drowning in a bog | 1200 | ×3. A struggle and a sucking under. |
| `bog-drain` | A bog using up its ten lives and draining away | 1500 | |
| `erode` | Erode | 2500 | Ground sinking, water rushing in. |
| `quake` | Earthquake | 4000 | The deepest sound in the game. |
| `fire` | Day o'the Stones | 10000 loop | A hail of falling stones: whistling, then heavy thuds and splintering timber. Loops for the spell's ten seconds. |
| `angel` | St. Anthony's Fire present | 10000 loop | A low, feverish whispering hum, sickly rather than holy. |
| `fits` | Someone seized by St. Anthony's Fire | 1200 | ×3. Choking, retching gasps. They die three seconds later. |
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

## The Grimoire spells

These belong to the Grimoire and Seasons of the Witch. None of them has a placeholder sound yet, except Seas of Blood, which borrows `quake`.

| ID | What it is for | Length (ms) | Notes |
|---|---|---|---|
| `changeling` | Changeling cast: your villager slips into a rival's colours | 1500 | A soft rustle and an indrawn breath, slightly wrong. |
| `changeling-swap` | The swapped rival running to your fold | 800 | Quick bare feet and a frightened whimper, heard at the fold end. |
| `kindle` | A changeling setting its fire | 1800 | A crackle catching, then a high fairy laugh. |
| `unmask` | A changeling found out | 1200 | A shriek, as of something caught. ×2 |
| `murrain` | Murrain cast over a herd | 4000 | A sour green drone with distant lowing. |
| `murrain-die` | An animal falling to Murrain | 900 | ×3. A bleat or squawk cut short. |
| `flies-carcass` | Flies over a carcass | 6000 loop | Lighter and lazier than `swarm`. Loops while the stain lies. |
| `phillip-wake` | Black Phillip cast on a rival goat | 1500 | A low goat bleat, pitched down and breathy. |
| `phillip-kick` | Black Phillip's backward kick | 500 | ×3. A thud of hooves and a body thrown. |
| `phillip-rampage` | Black Phillip rampaging | 8000 loop | Snorting, hooves, scattering people. Runs for the 30 seconds. |
| `familiar` | Familiar cast on your own goat | 1500 | A faint violet chime and a whisper. |
| `familiar-drink` | The familiar drinking at a rival altar | 4000 loop | Lapping, very quiet. It is meant to go unnoticed. |
| `fetch-labour` | A Cunning Woman labouring in her cottage | 10000 loop | Low, strained breathing behind a wall; smoke and a slow creak. Heard only nearby: it must not warn anyone further off. |
| `fetch` | The Fetch born, heard by whoever it hunts as well as its mother | 3000 | A long exhale into smoke, a muffled bell. The game uses `horn` here for now. |
| `fetch-walk` | The Fetch walking | 6000 loop | Heavy, unhurried footfalls with felled timber now and then. |
| `fetch-take` | The Fetch taking a Cunning Woman | 2500 | A choked cry and silence. |
| `glamour` | Glamour cast | 1500 | A shimmer, like a breath on glass. |
| `glamour-break` | A glamour falling away when a blow is struck | 600 | A brittle crack. |
| `pricking` | Pricking cast | 900 | A single sharp pin of sound, then a hiss. |
| `pricking-reveal` | Someone revealed by Pricking | 700 | ×2. A gasp. |
| `beltane` | Beltane Fire lit | 2500 | Fire taking in the pit, a cheer, a pipe starting. |
| `beltane-leap` | A couple leaping the fire | 600 | ×3. A whoop and a rush of flame. |
| `sworddance` | Sword Dance | 8000 loop | Stamping feet and clashing blades in rhythm. Loops for the minute. |
| `blight` | Cradle Blight cast | 3500 | A thin, sickly mist sound with a baby's cry that stops. |
| `keening` | Keening Wail | 4000 | A woman's wordless wail, carried a long way. Stereo. |
| `briar` | Briar Sleep cast | 3000 | Thorns creaking and growing, then a drowsy hush. |
| `briar-wake` | A sleeper woken by a blow | 500 | A start and a gasp. |
| `seas` | Seas of Blood cast: the sea turns | 5000 | A deep, wet swell and a low choir. Stereo. |
| `seas-warn` | The blood tide's countdown | 1200 | A tolling bell, repeated by the game in the last twenty seconds. |
| `seas-rise` | The blood tide rising | 8000 | A huge surge of water over land. |

## Livestock

| ID | What it is for | Length (ms) | Notes |
|---|---|---|---|
| `goat` | A goat nearby | 800 | ×3. A bleat. Occasional, on its own timer. |
| `chicken` | Chickens nearby | 1500 loop | Contented clucking, quiet. |
| `rabbit` | A rabbit at its hutch | 400 | ×2. Barely there: a thump of a back foot. |
| `offer-animal` | An animal offered at an altar or into a wicker figure | 1000 | ×3. A short cry and the knife. The game currently uses `die`. |

## Specifics worth knowing

- The cues that matter most for play are `horn`, `bog-claim` and `die`, because they tell you something is happening off screen. They are worth getting right first.
- The loops (`swarm`, `whirl`, `fire`, `angel`, `maypole`, `ritual`, `oak-hang`, `hunt-roam`, `flies-carcass`, `phillip-rampage`, `familiar-drink`, `fetch-labour`, `fetch-walk`, `sworddance`, `chicken`) need clean loop points, with no click where the end meets the start.
- The game currently synthesises 13 of these (`select`, `blast`, `quake`, `built`, `thunder`, `die`, `boom`, `arrow`, `swarm`, `horn`, `hit`, `chop` and `cast`). Blood-Running-Sea borrows `quake`, animal offerings borrow `die` and the Fetch's birth borrows `horn`. Everything else in this list is silent for now.
