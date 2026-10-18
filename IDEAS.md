# Wicker: ideas for after the campaign

A place to keep design ideas between sessions. Nothing here is built yet. Each entry carries a status:

- **Decided**: agreed and wanted.
- **Liked**: wanted in some form, with details still open.
- **Candidate**: suggested but not yet discussed.

---

## Now / Next / Later

- **Now:** Grimoire mode, built in v127 in test mode only. It's a procedural game where you choose eight spells before you start; rivals keep every spell, and All-against-all is always available. Play it to settle the palette size and find which spells feel essential and which feel weak.
- **Built in v128, test mode or Grimoire only:** offering livestock (chickens, rabbits and the goat, at altars and wicker figures, with no dread; animals breed back), the changeling, and Murrain.
- **Built in v131:** Black Phillip and the familiar.
- **Built in v135:** the fetch, with rival Cunning Women fleeing from it.
- **Next:** teaching rivals to offer animals and cast the new spells (including fetches aimed at you); Pricking to reveal familiars; Glamour.
- **Later:** the challenge levels, one per proven spell; then the unlock wiring (finishing the campaign opens the challenge campaign, and challenge levels open spells); then charms and counters as gaps appear.

## Structure (Decided)

**The base game stays as it is.** The current campaign and procedural games are left untouched by everything in this file, apart from the Oss quality-of-life features. The new spells, charms, livestock and the spell palette all belong to a separate mode.

**Progression:**

1. **From the start:** the campaign and the base procedural games.
2. **Finishing the campaign unlocks a challenge campaign** (working title *Seasons of the Witch*). Each of its levels forces one new spell into the palette in place of an existing one and teaches it. That spell is then unlocked for good.
3. **The new mode.** Alongside the base procedural games sits a new procedural mode with the spell palette, where you choose a set number of spells before each game, probably eight. Its pool holds the base spells plus every new spell unlocked so far. Livestock and the other additions would live here too.

**Open questions:**

- How many challenge levels should there be? One per new spell, or some levels introducing two?
- How big should the palette be?
- Is Extreme available in the new mode as well?

## Livestock (Decided; cosmetic version built in v126, test mode only)

- **Built so far.** Each settled cluster (wherever a well appears) gets a black goat, three to five chickens and a rabbit hutch with a run holding two or three rabbits. Goat and chickens wander around the well; rabbits stay in their run. Visible only while test mode is ticked. The models are in the workshop under Animals.

- **What appears.** A black goat and a few chickens appear procedurally as a village grows. They bring villages to life, as the flowers and bunting did.
- **Offering animals.** Animals can be given to the wicker in place of villagers. They yield less but add no dread, which gives a gentler path that spares morale.
- **Spells that use them.** Black Phillip, and possibly Murrain. Both are under Curses.

## Curses

- **The Fetch (Liked).** The Cunning Woman gives birth to her fetch, her own model made of translucent black smoke, like the shadow in Game of Thrones that kills Renly.
  - **How it moves.** It walks slowly in a straight line towards one target, crossing water and flattening the ground it passes, which leaves a permanent scar across the map.
  - **What it can and can't do.** It can't be harmed or guarded against, and it affects nothing but its target. It can be outrun, and it disperses after about 90 seconds.
  - **What it needs to balance.**
    - It must be slower than a Cunning Woman.
    - Rival AIs must flee from it.
    - It needs a warning when cast, and a line on the minimap.
    - One per tribe at a time, at Volcano-level cost.
  - **Edge cases.** An entombed target: it waits at the foot of the hill. A target who leaps from the crag: it disperses.
- **Changeling (Liked).** It replaces a rival villager silently. The rival sees nothing; you see a faint tell, such as eyes catching the light. It goes home and lives as a villager.
  - **Trigger.** You select it and press Kindle, or it kindles on its own after three minutes.
  - **Effect.** The building it's in or beside bursts into flame, and the fire jumps once to the nearest building within a few paces. Then it runs off into the wilds.
  - **Special case.** If the rival sacrifices it in the wicker, the fire takes early and burns empty, wasting their offering.
- **Keening Wail (Liked).** A song that disheartens, carried on the wind into a rival village. Spooked villagers go wild and flee to the edge of your land as stragglers, where your Osses can round them up. It's desertion that feeds your captive economy.
- **Briar Sleep / The Hundred Years (Liked).** A wide area sleeps for 30 seconds, and blackthorn springs up in a ring around it, withering after a minute.
  - Sleepers can't resist Osses, but the thorns keep fighters out on both sides.
  - It works in two ways: as a capture raid on a rival village, or cast on your own village to trap attackers inside.
- **Black Phillip (Decided).** It targets a rival's black goat. When spooked, the goat goes feral and kicks to death every villager within reach. He doesn't speak.
- **Murrain (Candidate).** A cattle plague. All livestock in the target village sicken and die. The carcasses can't be offered and raise dread while they lie there. It closes off the dread-free path livestock opens.
- **Cradle Blight / The Barren Year (Liked).** No breeding in the target tribe for a minute.
- **Seas of Blood (Liked).** The water across the whole map turns red. After a 30-second countdown, sea level rises a little and destroys anything left below it.
  - It's a world-ending spell, priced as such, and it hits the caster too, so it rewards building high.
  - It should be limited to once per game, for everyone.
  - Rival AIs must move uphill during the countdown.
  - **Open:** is the rise permanent, or does it recede after a few minutes?
- **The familiar (Liked; reframed).** It's now seen as the counterpart to Black Phillip: a spell you can only cast on your own goat, which binds it to your Cunning Woman as her familiar. Decided: it steals mana from rival altars (the Pyewacket errand below) and lifts the fog wherever it walks.
- **Pyewacket (earlier version of the familiar).** It summons a familiar, a hare or a black cat, named after the imps recorded by Matthew Hopkins (*Discovery of Witches*, 1647). It slips unseen into a rival village and drinks mana from their altar on every visit, until someone kills it. It slows the more it has drunk.
- **The Devil's Skin (Candidate).** From *The Blood on Satan's Claw*. A curse that spreads by touch: the marked villagers pass it on, and anyone carrying it long enough turns wild. Need-fire cures it.
- **The Poppet (Candidate).** A clay doll of a rival's Cunning Woman, placed in your village. While it stands, she takes damage from time to time. She has to find it and destroy it, so she's drawn into your territory.
- **The Mandrake (Candidate).** A planted trap. When an enemy pulls it up, the scream kills everyone within earshot. Good for passes and causeways.
- **The Hag (Candidate).** Villagers in the area wake exhausted and work at half speed for a minute. A softer alternative to Cradle Blight.
- **The Lambton Worm (Candidate).** A worm woken in a river or the sea that grows each time it feeds, and attacks whichever shore is nearest. It can't be controlled.

## Charms

Charms are positive spells, to sit alongside the curses.

- **Beltane Fire (Liked as "baby boom").** Couples leap the Beltane fire. The tribe breeds at double rate for about a minute, and new arrivals come in quickly. It's the counterpart to Cradle Blight.
- **Sword Dance (Liked as "training boost").** The longsword dance. Training at your camps and ranges runs at double speed for a minute, and any fighters trained during it come out hardened, taking a little less harm.
- **Rowan and Red Thread (Candidate).** From the old rhyme "Rowan tree and red thread / put the witches to their speed". A protective charm: the units in an area shrug off the next curse that lands on them.
- **Beating the Bounds (Candidate).** Your people walk the boundary of your village. For a time, no enemy spell can be cast on the ground inside it. A strong defensive charm with a long cooldown.
- **Well Dressing (Candidate).** Your wells are decked with flowers. Wounded people and damaged buildings near a well slowly heal.
- **Wassailing (Candidate).** Your people sing to the trees. Felled woodland around your village grows back, and wood comes in faster for a while.
- **Corn Dolly (Candidate).** The last sheaf, woven and kept. A share of your mana is stored safely in the doll, beyond the reach of spells and of the All-against-all reset, until you burn it to release it.
- **Witch Bottle (Candidate).** A ward buried under a building. It turns the next spell aimed at that building back on the caster.

- **Glamour (Liked).** A charm with a small area that can include the Cunning Woman herself. For 30 seconds everyone inside it is disguised in the colours of the nearest rival tribe, which works as a cloak of invisibility: rivals don't attack or take them. It's useful for slipping a raid or the Cunning Woman past a village, or getting her out of trouble.
  - **Open:** does attacking break the glamour early? Does Pricking reveal it?

## Counters

- **Pricking (Candidate).** Reveals hidden things in an area: changelings, familiars and poppets. The answer to stealth.
- **Need-fire (Candidate).** Cleanses your village of every curse. The cost is that every fire you have burning goes out, including a wicker man being lit.

## Acts and events

- **The Witch Trial (Candidate).** Your Osses capture a rival Cunning Woman and bring her to your altar. She's burned, and you gain her most powerful spell for the rest of the game.
- **The Willing Sacrifice (Candidate).** From *The Wicker Man*. An outsider (a stranger, a constable, a fool) occasionally wanders onto the map. He's worth a great deal of mana, but only if he's lured, not captured, and every tribe competes for him.

## Quality of life: late-game automation

The problem: late in a game you forget to train Osses, and sending them out after broken rivals, deserters and wild men becomes a chore.

- **Training menu (Built in v123; from v124 opened by building a Cunning Woman's Cottage: 80 wood and 300 mana, one per village, rebuildable).** A Train tab, like the Tribe tab. It has one row per unit type that you have a working building for. Each row shows how many you have, how many are queued and the mana cost, with buttons for one and for five.
  - Queued training goes to whichever building of that type is least busy, so you don't need to select buildings.
  - **Keep N (Built in v123).** A standing order on each row: "keep 4 Osses". Training queues automatically whenever the count drops below N and you have mana above a small reserve. Combined with roaming, this handles the late-game Oss cycle entirely.
- **Roaming Osses (Built in v123, as a Roam toggle).** Osses idle at home go out on their own and capture without being told. They respond to:
  - wild men nearby;
  - a rival tribe breaking (its stragglers at the stone circle);
  - deserters fleeing a village;
  - captives freed when a fold falls;
  - sleepers from Briar Sleep, and stragglers from Keening Wail.

  They should avoid targets with enemy fighters close by, and come home when their target is gone. The AI already has Oss-hunt logic (its `ossHunt` behaviour) that this could share.
- **Default or command? (Open.)** My suggestion is a **Roam** toggle on the Oss House, in the same spirit as the Post command for guards. It covers every Oss from that house plus idle Osses at home.
  - Making roaming the default would send Osses into danger early in a game, where you want them under control.
  - A toggle keeps that control, but once it's set you never need to think about it again.
  - An alternative is for it to switch on by itself once a rival breaks, since that's the moment the chore begins.
- **Unlock or always available? (Open.)** These are quality-of-life features rather than power, so they could be available from the start of the campaign, or at least from the level that introduces Osses, instead of being gated behind level 20.

## Other post-campaign directions

- **Multiplayer (Candidate).**
  - **Model.** Host-authoritative over WebRTC data channels: the host's browser runs the game, and guests send commands and receive state. The other approach, lockstep, would need the whole simulation made deterministic.
  - **Connection.** Introduce players through a tiny relay on indelicates.xyz, or with no server at all by swapping copy-and-paste codes, as keepsakes do.
  - **Modes.**
    - Two players sharing one tribe: one plays the Cunning Woman, the other commands the village.
    - Two humans against AI rivals.
    - Asynchronous challenges: a seed plus a recorded set of commands for someone else to beat.
- **Observances (Candidate).** Opt-in folk customs that add difficulty for a higher score, built on the scenario flags. Examples:
  - no altar;
  - dread doubled;
  - rivals start with their oak awake;
  - permanent winter;
  - no rebirth for the Cunning Woman;
  - no Osses.
- **The Daily Rite (Candidate).** A shared seed each day with fixed observances, and a result you can paste that gives nothing away. No server needed.
- **The Turning Year (Candidate).** A roguelike run of linked maps through the seasons. You choose boons from barrows, seasons force banes, and survivors carry over from map to map.
- **The Witchfinder (Candidate).** An outside faction (the Church) arrives late in long games. It converts rather than sacrifices, its steeples suppress spells, and it pressures the rivals to fight together.
- **Truce and tribute (Candidate).** Diplomacy through the sacrifice economy: captives as tribute, a May Queen to bind a tribe to you, and dread if you break faith.
- **Three marks per level (Candidate).** Optional challenges for each campaign level, such as no wicker, a time limit, or no buildings lost.
- **Level editor (Candidate).** The scenario flags in a form, with finished levels shared as codes.
- **The Chronicle (Candidate).** An end-of-game account written in the game's own voice, as a ballad or a tapestry-style scroll of the key moments.
- **Photo mode (Candidate).** Build on Hide UI with a free camera, depth of field, and a still export with the film grade applied.
