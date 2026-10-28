# Wicker: a retrospective changelog

This is a history of how Wicker was built, reconstructed from the commit log, the waypoint builds kept in `waypoints/`, and the design decisions recorded from the earliest conversations. It doesn't list every commit. It follows the significant steps: each feature as it arrived, and each round of balance work, with the reasoning where the history records it. Dates are those of the commits. The repository opens on 9 October 2026 with a build that already carried most of the core game, so the first section describes that inheritance from the waypoints rather than from commits.

---

## Prehistory: from Populous clone to Wicker

Wicker began as **Worldshaper**, a browser god game modelled closely on Populous: The Beginning. It was 3D, with water and cliffs, touch controls and a folk-horror mood, but in its mechanics it was essentially a Populous remake: a shaman, a spell list borrowed wholesale, tribes, and priests and temples converting followers.

The break came when the game was redesigned around one idea: **mana comes only from sacrifice**. That rule pulled the rest of the design after it:

- **Tiers of sacrifice.** There are three places to give people to the fire: the forest altar, the wicker man, and the ram-headed Wicker God.
- **Dread.** Sacrificing your own followers builds dread, and dread makes villagers desert. Feeding the fire with your own people becomes a real cost rather than a free conversion.
- **Captives over converts.** Captured enemies are worth more than converts and carry no dread, so taking prisoners becomes the efficient path. Populous's priests and temples were reimagined as a capturing unit: the **Oss**, trained at the Oss House.
- **Hollow-hill attainment.** It became a permanent late-game boost rather than a win condition. The shaman is entombed in a destructible wicker fortress, so the power she gains is also a target.
- **The tribes.** A palette of Ochre, Blood, Forest and pale Ash.

At that point the sacrifice-economy version became its own project, Wicker. Worldshaper was kept as a separate game. Multiplayer was noted as a possibility for later.

## Before the repository: the core game (to 9 October)

The earliest kept build, `wicker-2026-10-08-rook-tree.html`, is already a complete god game in the tradition of Populous: The Beginning. It is a single HTML file using three.js, played on a wrapping 128-square heightmap world.

- **Mana comes only from sacrifice.** A tribe of villagers breeds in huts, chops wood and builds. Mana comes from giving people to the fire: at a forest altar, inside a wicker man or a Wicker God, or as captives dragged home by Osses and penned in thrall folds. This is the game's defining economic rule, and nearly every later balance decision follows from it.
- **The shaman and her spells.** A shaman (later the Cunning Woman) casts sixteen spells: Blast, Lightning, Plague of Flies, Shield, Ghost Army, Land Bridge, Flatten, Hypnotise, Whirlwind, Swamp, Erode, Earthquake, Firestorm, Angel of Death, Volcano and Armageddon.
- **Buildings.** Huts, a warrior camp, an archery range, an Oss house, a rook nest, a thrall fold, an altar, the wicker man and Wicker God, a tomb, Herne's Oak, balloons and boats. There are also the stone circle where the shaman is reborn, the barrows, and a neutral Moot at the centre of the world.
- **Rival tribes.** AI rivals breed, build, train, raid and cast against you and against each other.

The second waypoint, `wicker-2026-10-09-pre-campaign.html`, adds the **maypole and May Queen** and the **blackthorn hedge**, together with the sacrifice spectacles, before any campaign existed.

## 9 October: the campaign begins

- **The twenty-level campaign.** It arrives with the first commit. It teaches the systems one at a time, from The Strait and The Grove through to The Last Harvest.
- **Level 1 reworked.** You start at zero mana and must build an altar before anything else. Mana from sacrifice becomes the very first lesson.
- **Level 5, The Long Watch.** A walled valley where rivals attack only the player. A test mode arrives with it, for jumping to any level during development.
- **Boats removed.** Boats and the boathouse were cut. Level 6 became The High Places, and levels 6–13 were reworked around the remaining tools.
- **Spell rebalancing.** Flatten was widened, Volcano made deadlier, and shamans given guards.
- **Salted ground and broken tribes.** A tribe that is driven out leaves salted ground behind it. A tribe reduced far below its peak is *broken*: its people gather at its stone circle while its buildings crumble. A rival finder was added so you can locate the tribes you're fighting. Level 6 was moved onto one small island.
- **`AUDIO-CUES.md`.** A list of the sounds the game wants, with suggested lengths.

## 10 October: the folk register and the living village

- **Renaming.** The game was renamed into a folk register. Shaman became Cunning Woman, braves became villagers, Swamp became Bog, and Armageddon became All-against-all, "the battle of all-against-all" in event messages.
- **Villages that look lived in.** This took several passes in one day:
  - idle pastimes for villagers;
  - flowers growing in still rings round settled buildings, in maypole pink, yellow and white;
  - front gardens, patches of wild flowers in spare ground, and a well for every cluster of six huts, roofed in its tribe's thatch colour;
  - bunting strung hub-and-spoke from the maypole, the stone circle, a well or a central hut.

  Worn paths were tried three ways: traffic mud, laid lanes, and narrow translucent paths. In the end they were removed entirely, because none of them looked right.
- **Dressing the sacred places and remembering the dead.** Entombed hollow hills got five strings of bunting running from a centre pole to five flower beds. This look later informed the game's wider visual direction. Memorials began to mark where people died.
- **New spell: Scrying Torch.** A destructible beacon that keeps the fog of war lifted around it.
- **The model workshop.** It replaced the gallery as an in-game editor for every model, with multi-select and groups. Export is by copying only, because file saves are blocked inside the artifact viewer. Most of the game's look now comes from Simon's edits made here and "baked in". This day brought:
  - the hut, the hollow hill, the stone circle, the Wicker God, the Cunning Woman, the May Queen, the Rider and the archery range;
  - a new wicker man, which now carries its own kindling, replacing the separate kindling piles;
  - a new Wicker God made from the wicker man's kindling heap at 1.8× scale;
  - a new forest altar: a split slab, a horned post, a knife and blood.
- **Burnings as spectacle.** Fire catches the kindling first, then climbs. The Wicker God's hands burn, and its head, built from the current model, falls, lands with a thud and smoulders.
- **Fighters spare raid victims.** Fighters no longer kill enemies that their own Osses are in the middle of capturing.
- **Third waypoint.** `wicker-2026-10-10-settlements.html` was kept.

## 11 October: models, spells reimagined, and the Surrounded problem

- **Text export.** Every piece of player-facing text was numbered for editing, with a map back to where it lives in the code. This is how Simon's later rewrites came back into the game.
- **Surrounded, level 15.** A hub map where rival islands join yours by narrow causeways. The awake oak and the Wild Hunt were tried as the player's head start, then replaced with two full thrall folds and a finished Wicker God.
  - **Balance lesson.** A general rule was written so the AI noticed when every land route was cut and bridged out instead. It was undone, because it changed play everywhere. The fix was narrowed to this level: on Surrounded, an attacking rival is given its Land Bridge when it can't afford one, and rival balloons are capped at two. This was the first appearance of a principle that runs through the rest of the history: fix the level, not the whole game.
- **Spells reimagined in the folk register.**
  - Firestorm became **Day o' the Stones**: boulders that kill villagers outright and break buildings, over ten seconds.
  - **Whirlwind** now carries away the building it's aimed at. The Wicker God, Herne's Oak and tombs are exempt.
  - Angel of Death became **St Anthony's Fire**: a slow green blight that gives three seconds of fits before death.
- **The blackthorn hedge.** It got its own model: a dark mound, crooked black stems with pale thorns, sloes, blossom and a tribe rag. Each length is turned differently, the stems grow from the ground, and arching briar joins link neighbouring lengths.
- **A wave of new models.**
  - **Buildings:** the warrior camp (a stone roundhouse inside a palisade, with a campfire and cauldron), the archery range (a stone tower with butts and targets), the Oss house (a long barn with a horse skull on the gable), the balloon and the Balloon Works.
  - **People:** the archer, the warrior (sword, studded round shield, tribe-coloured helm band), the villager and the Oss, and a reworked May Queen.
- **Buildings face home.** Every building turns its door towards its tribe's stone circle, slightly unevenly. Gardens, chimney smoke, the people inside wicker figures, and the God's eyes, hands and falling head all turn with it.
- **Broken raids.** Attackers caught on the defenders' ground are seized and dragged to the nearest altar for captive mana, with no dread. A routed tribe's next wave is smaller and comes later.
- **Fix.** The Scrying Torch crashed on unbuildable ground. Crash messages now name where the error happened.

## 12 October: endurance, tokens, film, and campaign tuning

This was the busiest day in the history.

- **Guarding.** A Post button stations selected warriors or archers around a tribe banner. Guards chase no more than nine paces before returning, and take 25% less damage at their post. "+5" buttons select the five nearest units of a kind.
- **The no-villagers rule, tried and withdrawn.** A button to free every captive into your tribe, and a defeat when you had no villagers and no way to get more, were both added and then taken out the same day for a rethink.
- **Ättestupa.** This became the answer to that rethink. With very few villagers left, the Cunning Woman raises a crag at the edge of the village and climbs it while her people watch. She goes over, six villagers rise from the stones, and no rival attacks for thirty seconds. The crag stays.
  - **Balance passes on the terror.** The rivals' terror went through four versions: dread filled to maximum, dread held at maximum through the truce, a capped fifth of villagers fleeing, and finally a steady loss of 60% of their villagers over the truce, which gives back roughly half their numbers. It was later weakened when you hold a standing army of more than five.
  - **Closing the cheese.** It was too easy to over-train by accident and qualify for Ättestupa. Training was first stopped from taking the last two villagers, then the floor was raised: training always leaves three villagers, and Ättestupa only opens below three. Training can no longer make you eligible.
- **Tokens.** Sixty-four achievements across campaign waypoints, spells, buildings, rites, growth, endurance, victories, deeds and curiosities. They can only be earned in live play. A Tokens sheet has keepsake copy and paste that carries both tokens and campaign progress. `ACHIEVEMENTS.md` was added for naming them.
- **Late to the Feast, level 16.** It was tried with two rivals and a smaller head start, then put back to three. The answer was structure: no fog, and each rival sends one scripted raid (3, 5 and 7 fighters at 1:40, 4:00 and 6:00) with nothing else before 8:00. A beaten raid sends its tribe's dread surging, so villagers desert, and an annihilated raid shames the attacker.
- **A difficulty ramp for the campaign's end.** Levels 17–19 were eased below full Hard and escalate towards 20 across mana, breeding, wave growth, fighter share, casting pace and attack timing. They are named **Stern** rather than Hard, and count as Normal wins for tokens. Victory and defeat titles dropped the difficulty name, and end-of-game stats became richer.
- **Models.** A new Rook Tree (a dead tree with a lookout platform, ladder, ivy and rooks), plus revisions to the Cunning Woman, wild man, maypole, torch, fold, oak, hut chimney and hedge. A fix keeps the hanging Cunning Woman under the oak's rope whichever way the oak faces.
- **The film look.** An optional 1970s folk-horror grade:
  - It started as Off, 35mm or 16mm, with grain and dust-and-scratches sliders. Weave and flicker were rejected as nauseating, and 16mm was dropped as unnecessary.
  - The grade was rebuilt around the reference stills: land drained to khaki and grey, deep reds, fire held orange, firmer contrast.
  - Its first version read as night rather than an English day. Every number was exposed on a live Tune panel so Simon could tune it by eye.
  - Tribe colours were exempted, with their own brightness and strength sliders.
  - Red depth was made hue-based so browns and skin stopped turning orange, with a Red range slider.
  - Simon's tuned numbers became the defaults, and the panel moved behind a small "Advanced film grade settings" link.
  - Fire is now identified by a mark the fire particles carry themselves. That way only real fire is held orange, and the Cunning Woman's halo no longer reads as fire.
- **Memorials as sacrifice stakes.** Altar memorial ribbons were floating, so they were first tied round the stone circle's post. They were then replaced by coloured stakes spiralling out from the post. After a look at the first version, the spiral was tightened to wind in towards the post, and finally given five looser arms, plain blocks, random lean and short outliers further out.
- **Fire from the Sky, level 7.** It was too easy.
  - Each rival's first raid now goes for the player.
  - From 2:30, each rival trains a balloon ahead of everything else and flies it straight at you, bombing buildings before people.
  - Entombment is allowed for the player only. Simon found winning from a tomb a funny route that ignores the level's intended path, and kept it.
  - It is a one-life level, so a fallen tomb means defeat.
- **Balloon ferrying.** Embark and disembark had been fiddly and nearly invisible. Now, ordering people somewhere they can't walk sends idle balloons to fetch them, carry them over and shuttle back for the rest.
  - **Edge cases handled:**
    - stranded Osses with captives are flown home;
    - entombing at a hill across water ferries the Cunning Woman and her twenty followers, stragglers included;
    - with no balloons, the rite is refused instead of walking her into the sea;
    - the oak rite ferries her too.
- **Three new Deeds tokens.** Winning Fire from the Sky from a tomb, three full thrall folds, and three wicker men burning together.
- **May Morning, level 8.** Burning three May Queens was trivially easy.
  - First, two rivals raise maypoles early and send every free Oss, with fighters, after each queen you crown.
  - That was still trivial, so wicker men and fog were removed.
  - Then the decisive change: the goal became gathering 1,000 mana, a new goal type with progress shown in the top bar. Without wicker men, you have to keep your queens alive long enough to earn from them.
  - The level got a new intro.

## 13 October: words, seasons and wind

- **Simon's text edits.** Thirty-two entries were applied, covering menu and help wording, every spell description, the campaign subtitle and the goal wording. A slimmer current export followed (`text/wicker-words.txt`, 210 entries) with its map and generator. All twenty level intros were then rewritten by Simon, and the intro panel now keeps paragraph and verse line breaks.
- **Seasons.**
  - **Spring:** wild flowers.
  - **Summer:** warmer greens.
  - **Autumn:** leaves in four muted brown shades, brown lowlands under green mid-slopes.
  - **Winter:** frost, a snowline with white trees above it, falling snow, and a slowdown for anyone in the wilds.

  Seasons are random for one-off games and set to fit each campaign level. After a first look, autumn was made less red, and winter's white was toned down for the film grade. Hollow hill mounds now take the colour of the ground around them in every season.
- **The wind.** Simon's recording was looped seamlessly under the drone, cut down and embedded, and gets louder as you zoom out. It was then made intermittent so it wouldn't tire: it comes in for a minute or so in the calm after a fight involving you, or after a long quiet, and fighting sends it away.

## 14 October: the endgame, fairness at the Moot, and Extreme

- **The rivals' sortie rule, narrowed.** The first fix for the last level changed rival behaviour across every level, and it was rolled back: the emergent play, such as rivals wiping each other out for settling too close, or retaliation you provoke yourself, was too good to lose. What remained was a narrower rule for all levels:
  - a villager or May Queen merely passing a rival's buildings no longer sets off a sortie;
  - one who stops, to stand, chop or build, does, and is dealt with quickly.
- **The Last Harvest, level 20, reimagined.** It was first eased with a later first attack and capped early waves, then rebuilt on Simon's brief. It was never meant to be "Surrounded part two" but a standard Hard level begun at a small disadvantage.
  - The four villages sit evenly spaced at the corners of a square, and every village is always in sight.
  - The Moot, the hollow hills and the wild men lie in the fogged ground between.
  - Everyone starts with an army: you with six warriors and three archers, the rivals with eight and four. The result is big, bloody battles.
- **All-against-all made fair.** A late defeat showed the problem. Invoking the Moot cost the invoker the full mana bar, while rivals arrived with as much as 3,000 banked, and the Moot cuts off nearly all income. A rival Cunning Woman could therefore throw every big spell in the first minute. Now:
  - every tribe arrives with exactly enough for one Lightning, one Shield and four Blasts;
  - rival Cunning Women cast only those spells at the Moot;
  - the Hunt earns no mana during it.

  The battle is decided by the armies.
- **End screen.** Singular labels for one captive, raider or May Queen.
- **Extreme.** A fourth rival skill for one-off games, unlocked by finishing the campaign.
  - Every tribe, yours included, starts bare: a Cunning Woman, five villagers, and no mana, wood, huts, altar or fold. Everyone has to start their own economy.
  - The rivals are faster and greedier:
    - more mana from sacrifice and faster breeding;
    - quicker building, with a hut every 55 seconds;
    - attacks from 3:30 and every 100 seconds after;
    - a larger fighter share and quicker casting;
    - a keener eye for your Cunning Woman.
  - Rivals build their altar straight after their first huts, since they have nothing else to run on.
  - A fallen tomb is permadeath.
  - A "Win on Extreme" token was added.

## 15 October: film by default, and the Blood–Forest feud

- **35mm on by default.** The button carries a small caption: "higher performance devices".
- **Forest's dominance, measured.** Forest seemed to win most AI-versus-AI battles. Forty headless Watch-mode games on Hard confirmed it and explained it. Forest is the least warlike tribe, keeps more villagers, runs the strongest Oss game and gets a little more from each sacrifice. It won 9 of 20 baseline games with an average peak population of 86, against about 60 for the others. Most of that came from preying on Blood, the most aggressive tribe, which it eliminated eight times for every two the other way.
- **The grudge.** Instead of flattening Forest towards the average, Simon proposed giving Blood a grudge against Forest: double weight when choosing Forest as a target on Hard and above. Over thirty games:
  - Forest's wins fell to 9 of 30 (30%), level with Ochre, the tribe with no personality;
  - Blood rose to 8 wins;
  - the feud became even, at seven eliminations to six;
  - Forest kept the largest population.

  The personalities are intact, and the balance fix doubles as a story the player can see.

## 16 October: test-mode tools and a phone top bar

- **Hide UI (test mode).** A button in the top bar clears every control off the screen, for screenshots and footage. H, or a three-finger tap on a phone, brings them back.
- **The top bar on phones.** The control buttons became compact and wrap instead of overflowing, and the minimap and messages now sit below the bar whatever its height.

## 18 October: the Grimoire, livestock and a second campaign

The day began as brainstorming about what comes after the campaign. Simon set the rule that shaped everything since: the base game stays as it is, and the new material lives in a separate mode. IDEAS.md was written to hold the plans.

- **The Train tab and the Cottage.** A Train tab queues any unit type from one place, with Keep-N standing orders that top up while mana allows and a Roam toggle that sends idle Osses after wild men and deserters. It was too effective to give away, so it is unlocked by building the Cunning Woman's Cottage (80 wood, 300 mana, one per village), which arrives in the campaign with the Oss House. Simon built the cottage model in the workshop.
- **Livestock.** Each settled well now keeps a black goat, a few chickens and a rabbit hutch. Animals can be offered at altars and wicker figures without raising dread: a goat is worth a captive, a chicken 0.3 of a villager and a rabbit 0.2, balanced by how fast each breeds back. They show as animal silhouettes inside the wicker figures. Simon built the goat model.
- **Grimoire mode.** A procedural mode in which you choose your spells before the game, now nine. Each rival tribe carries its own nine, which set its style: Blood for war, Forest for magic and defence, Ash for beasts and disease, Ochre a little of everything.
- **Thirteen new spells**, all for the Grimoire and the challenge campaign:
  - **Changeling**, a saboteur that kindles fires inside a rival village (reworked on 20 October).
  - **Murrain**, a plague on a herd. While the carcasses lie, the tribe's dread is held one altar sacrifice below the desertion line. It comes with green vapour, sickly motes and flies.
  - **Black Phillip**, cast on a rival's goat. It goes unnoticed until its first backward kick, which kills outright, then rampages for thirty seconds. If it survives, it escapes to the wilds and earns a token.
  - **The Familiar**, cast on your own goat. It is unseen by every rival except through Pricking, drinks mana from each rival altar it can reach, and lifts the fog where it walks.
  - **The Fetch**, a slow black double of your Cunning Woman that walks straight for a chosen rival Cunning Woman over sea and hill and cannot be harmed. In practice it mostly drives her off rather than catching her.
  - **Glamour**, ninety seconds in a rival's colours. Nobody targets you, and only a blow you strike breaks it.
  - **Pricking**, which reveals glamours, changelings and familiars.
  - **Beltane Fire**, a stone-ringed fire pit that couples leap before going home to breed twice as fast for a minute.
  - **Sword Dance**, which trains twice as fast for a minute, with those trained taking a fifth less harm.
  - **Cradle Blight**, which stops births in a rival village for a minute, cast with a sickly mist.
  - **Keening Wail**, which reaches sixty paces and drives villagers into the wilds.
  - **Briar Sleep**, a ring of thorns whose sleepers include Cunning Women, until a blow wakes her.
  - **Seas of Blood**, at 2,900 mana. After a thirty-second blood tide the sea rises and drowns the low ground. It can be cast again and again, and each casting leaves the sea permanently redder.
- **Rivals learn the new craft.** Rivals cast from their palettes with their own rules. They prick only on suspicion, keep their goats for Phillip and the familiar, build cottages once they have mana to spare, and offer small stock before villagers.
- **A fix for being stuck.** Units standing on a steep cell could report "no way across". The pathing now steps them off onto walkable ground. A camera lift tried the same day was taken straight back out.
- **Seasons of the Witch.** Simon decided the shape of the post-campaign progression:
  - finishing the campaign opens a challenge campaign;
  - its first level humbles you, so it is won by surviving five minutes against three fully stocked rivals casting everything;
  - the levels after that put you on even terms with the rivals;
  - each new spell is unlocked for the Grimoire when its season teaches it;
  - Extreme is available in the Grimoire;
  - the last level is a winnable rematch of the first;
  - finishing it all will open a victory-lap NG+ of the original campaign with the Grimoire.

  Each season is lit and coloured slightly wrong. The Grimoire opened outside test mode, starting from the base spells.
- **Writing.** prompts.md was added, with Krea 2 prompts for a tarot deck matched to the game's models.

## 19 October: ten seasons, played through

- **The seasons.**
  1. The Humbling.
  2. The Herd: livestock from the start, little mana and a free Familiar.
  3. May Eve: grow to 160 people against two rivals who raid only you and carry Cradle Blight.
  4. The Sickness: both Cunning Women start entombed, with one hut and 300 mana each and no Blast or Lightning, so the plagues decide it.
  5. Harvest.
  6. The Fair.
  7. The Long Nights.
  8. The Hunt: won when a rival Cunning Woman dies by any means while your fetch is hunting her.
  9. The Flood: you start on a raised mountain, with the rivals low.
  10. The Answer.

  The rest of the day was spent tuning these as Simon played them. May Eve went from far too easy to unwinnable on Hard and settled on Normal.
- **Spell sets by season.** At first each teaching season carried only the basic spells and its own new ones. Simon pointed out that this was a default, not a rule, and seasons can now also carry earlier spells for both sides: St Anthony's Fire in the Sickness, for example. Pricking now comes after the Changeling, with the Fair moved after Harvest, rather than as an eleventh season, which was briefly and wrongly added.
- **Fixes.**
  - Beltane Fire now calls villagers out of the huts to make up the line; before, it gathered nobody early in a game.
  - Rivals now find huts to blight from much further away.
- **A token.** End it in hemp: win while your Cunning Woman hangs from the tree.
- **Models.** Simon's rabbit and hutch were built in. The barrow's change in the same export was reverted, because its mound takes the colour of the ground beneath it.
- **The menu and the opening line.**
  - The menu now shows unlocked options on first load.
  - The Grimoire picker opens outside test mode; one gate had been missed.
  - The old "rivals usually first attack after N minutes" toast was replaced with one of Simon's six opening lines, picked at random.
- **Writing.** prompts-film.md was added: twelve gameplay scenes as stills and fifteen-second shots from a lost 1973 Eastmancolor folk horror film.

## 20 October: the Changeling remade

- **The Changeling, cast on your own.** Simon redesigned it:
  - you cast it on one of your own people and choose a rival village;
  - it walks there in their colours while one of theirs of the same rank runs to your thrall fold (your altar if the folds are full, or it goes wild if you have neither);
  - neither can be touched on the road;
  - once there it lifts the fog around it, can be walked about, and can be set to kindle a particular building;
  - when left alone it keeps clear of the Cunning Woman it lives among.

  At 70 mana it farmed captives, so it went up to 200. As Simon put it, the real value is seeing into their camp, which is worth trading mana for nearly one to one.
- **Plague of Flies, strengthened.** It now drives everyone out of any hut it settles on. This changes the base spell, at Simon's request, because it had always been underpowered.
- **Glamour, less easily seen through.** Rivals grow suspicious only after a glamoured stranger lingers about twelve seconds near their Cunning Woman, not on sight.
- **Season tuning.**
  - Harvest carries Plague of Flies.
  - The Fair carries Hypnotise, Earthquake and Scrying Torch, under a bright pinkish sun. A garish palette was tried first and rejected.
  - The Long Nights carries the Changeling and starts with changelings already planted in every camp.
- **The interface.**
  - A game timer was added to the top bar.
  - The Box and Cunning Woman buttons were made compact on phones.
- **Audio.** AUDIO-CUES.md gained cues for the Grimoire spells and the livestock.

## 20–21 October (night): the Inn, and catching a crash

- **The Inn and the Landlord's Daughter.**
  - **What she is.** After a round of unit ideas that Simon found no gold in, he proposed a building of his own: the Inn, with a name drawn from a list as each one is built, which trains the Landlord's Daughter.
  - **What she does.** She is a lure, not a fighter. Enemy warriors, Osses and villagers who come close gather round her. After a few seconds they are drunk and follow her home, six at most. They then sleep around her inn until she dies or they are killed or carried off. Archers, Cunning Women and the like are not taken in. Rivals build inns too, and send their daughters out to meet raiders.
  - **Cost.** The Inn costs 90 wood and 100 mana. She is dear and slow to train: 260 mana and 45 seconds.
  - **Into the base game.** She was built behind test mode first. In play she made little difference to battles, but helped with captives and gave a modest boost to defence. She then joined the base game, arriving in the campaign at May Morning beside the Maypole.
  - **Names.** The inn names are Simon's, from films, television, books and games: the Slaughtered Lamb, the Winchester, Dorry's Tavern, the Green Man, Jamaica Inn, the Crow and Crown, the Mother Black Cap, the World's End, the Grendel's Head, the Red Lion, the Cloven Hoof, the Broken Drum, the Nag's Head, the Kebab and Calculator, the Bloody Stump, the Swamp Rot Inn and more, plus the Bannered Mare, the Queen Vic, the Dog in the Pond, Lassiter's and the Bronze.
  - **Models.** Simon built the inn and daughter models in the workshop; a duplicated arm on the daughter was removed.
- **Models.**
  - Simon also reworked the hut: a door frame and a ring round the eaves.
  - Workshop Export now lists only models that differ from those built into the game. The full list had grown past what could be copied on a phone, or sent in one message.
- **Test-mode tools.**
  - **Free camera.** It sits beside Hide UI and allows zooming from a few paces to twice the usual distance, with a tilt slider from ground level to overhead, for screenshots.
  - **Watch mode.** Tapping a unit or building now names it: tribe, type or inn name, health, and states such as drunk, asleep, entombed, glamoured or a hidden changeling.
- **Crashes.**
  - **The start-of-game crash.** Gating the Inn behind test mode had broken the check on which buildings are allowed. Starting any game with test mode off crashed, from v178 until it was found in v181.
  - **The error record.** Simon had been seeing an occasional "reading 'x'" crash too briefly to catch. The game now records the last error with its function, line and what was being played, and shows it on the main menu with Copy and Clear.
  - **What it caught.** The first record pointed at wild-flower patches carried over from a previous game. A patch that had begun fading late in one game could ask for more flowers than it had in the next.
  - **The fix.** Flower patches, bunting, tomb beds, fetches, fire pits, carcass stains, livestock and pending changeling choices are now all cleared when a new world is built or a save is loaded.

## 21–22 October: village character, the song, and the Hunt

- **Rival villages.** Simon asked why rival Cunning Women spread their buildings so widely. The site-finder took the first good spot anywhere within reach. It now follows personality.
  - Forest still takes the first good site anywhere.
  - Ash, Ochre and Blood try sites nearer their stone circle more often, and weigh their choice towards them. Ash huddles a little, Ochre a good deal and Blood the most.
- **"O Woman of the Cunning".**
  - **The prompts.** `prompts-song.md` illustrates Simon's song with nine fifteen-second H3 sequences, one for each half-verse and chorus, following the song's arc from barred doors to the bloody waters.
  - **No singing on screen.** The first draft had villagers singing. Mouths that move could never match his recording, so the villagers are now silent and the song plays over them.
  - **Queuing.** `tools/queue_prompts.py` sends every prompt in a prompts file to ComfyUI's queue in one go, with fresh seeds and output files named after each section.
- **Models.** Simon's Cunning Woman and Beltane fire pit were built in. The same export carried a balloon edit he had never made: an older change saved in his browser. The built-in balloon was kept.
- **The Hunt.**
  - **The opening.** Both rivals send a fetch after your Cunning Woman three seconds in.
  - **The goal.** It is won by bringing down both rival Cunning Women. No Cunning Woman is reborn in this level, and losing yours loses it. The top bar counts the rivals left.
  - **Mana.** Starting mana was doubled to 2,400, so a second fetch can be sent.

## 23–24 October: modes, and the hollow hills

- **The Answer eased.** Simon judged it unwinnable. Rivals now start with 1,000 mana and lighter garrisons. Their first attack comes at four minutes and then every two, only their first two waves are aimed at you, and they are a little less warlike and slower to cast.
- **Spell modes.** The start screen now offers three:
  - Base spells, previously called All;
  - Cunning spells, in which you and every rival carry every spell, as in the Answer; it opens once Seasons of the Witch is finished;
  - the Grimoire.
- **Models.** Simon's Rider of the Hunt was built in.
- **The hollow hills.**
  - **The problem.** A barrow modelled as a mound always sat awkwardly on the land, its curves sticking out of the slope.
  - **The fix.** The mound is now raised from the terrain itself, a dome set just behind the stonework. It shares the land's faces, light, snow and colour, and trees stand round its sides and back to soften the edges.
  - **The doorway.** The first version buried the stonework. The dome now sits further back and the ground in front is left at its own level, so the doorway and its black entrance stand fully clear.
  - **The models.** The barrow model is now the stonework alone, with Simon's larger doorway. The tomb is the same stonework with the entrance sealed, plus its pole, stakes, pennants and bunting.
- **The entombment rite.** The Cunning Woman no longer simply vanishes.
  - Her twenty followers fling pink, yellow and white flowers into the air, then fall dead where they stand. Their bodies lie in pools of blood for fifteen seconds.
  - She walks to the doorway and down into the hill, and only then is it sealed.

## 26 October: the words, and the daughter

- **The text workshop.** Editing the game's writing in text files was a chore. Test mode now has a text workshop beside the model workshop.
  - It lists every piece of writing, grouped: level titles and intros, spell names and descriptions, the opening lines, inn names, the Rejoice! lines and the tokens.
  - Edits take effect at once and are kept on the device. Export gives only the changed lines, to be built in as models are.
- **Simon's words.** The first export was built in:
  - all ten Seasons of the Witch intros;
  - two renamed seasons, The Long Night and The Inundation;
  - Seas of Blood renamed Blood-Running-Sea;
  - nine spell descriptions;
  - a longer Rejoice! list.
  
  Obvious slips are corrected when words are built in; deliberate archaisms are kept.
- **The Landlord's Daughter.** She was underpowered for her cost. Huts of her tribe within ten paces of her now breed half as fast again. Two daughters don't double it, but she does stack with Beltane. Covered huts give off a faint pink mote.
- **Multiplayer.** Design work began, in `MULTIPLAYER.md`.

## 28 October: three spells reworked from play

Simon's experience of three spells, rather than their numbers, drove these changes.

- **Blast.** It felt slow, though its cooldown is short.
  - **Stays armed.** Each cast used to need two taps, the spell and then the target. Blast now stays armed after casting, so each tap fires another, until the tile is tapped again or the player right-clicks.
  - **Faster flight.** The shot flies twice as fast, so it lands before a running unit has moved on.
- **Hypnotise.** It used to feel like setting up a problem for half a minute later, because the hypnotised turned back wherever they stood, often in the middle of your village. They still fight for you for 25 seconds, which lets you turn an attack and regroup. When it wears off, they now flee in a panic in random directions for a further thirty seconds.
- **Keening Wail.** It never felt noticeable, because its payoff happened far from where it was cast.
  - **The drift.** The afflicted now float a little above the ground, leaning forward, and drift in a straight line to the casting Cunning Woman, wherever she is: to her hill if she is entombed, or her stone circle if she is waiting to be reborn.
  - **Seen and unseen.** They cannot be harmed or ordered on the way. Each carries a small halo in the caster's colour, so a rival's keening against you is as plain as your own. Your own afflicted also clear a little fog around them.
  - **Release.** They stand about her in a daze for ten seconds, then wake as wildmen.
  - **First play.** Simon found the drift too quick to be eerie, so it was halved. The wildmen also seemed to vanish a second or two after waking. A wildman wanders around a home point, and only wildmen born in the wild had one. Any villager turned wild, by the keening or by other routes, wandered towards a position that wasn't a number, and was lost. Wildmen without a home now take the spot where they woke.
- **Two Hypnotise bugs from play.**
  - **The May Queen in your own fold.** A rival Oss carrying your May Queen, once hypnotised, carried her home to your own fold, where she became a "captive" of her own people. An Oss that changes sides while carrying one of its new people now lets them go.
  - **A one-second panic.** A rival's Oss panicked only for a moment before going back to hunting. The rival AI's own orders, such as a hunt for a May Queen, were overriding the panic. Panic now overrides any order until its thirty seconds are up.
- **The text workshop takes in the messages.** Toasts, hints and the end-of-game lines are now in it too: about two hundred of them, read from the game's own code. Each is labelled with where it comes from, and its live parts, such as a number or a tribe's name, are shown as {1}, {2} and so on to keep in place. An edited message replaces the original as it appears, without touching the code that sends it.

---

## Threads that run through the history

A few principles recur often enough to be worth stating.

- **The sacrifice economy decides everything.** Starting mana, folds full of captives, mana goals and the bare start of Extreme are all levers on one rule.
- **Fix the level, not the game.** When a general AI rule was used to solve one level's problem, it usually damaged the emergent play elsewhere and was withdrawn: the bridging rule on Surrounded and the sortie rules for The Last Harvest. The fixes that lasted were scoped to the level that needed them.
- **Cheese gets closed at its source.** Ättestupa's eligibility, a lone villager provoking an assault, and the Moot's mana asymmetry were each fixed by removing the exploitable condition rather than by punishing the player.
- **The base game stays pure.** From 18 October the post-campaign material lives apart: in the Grimoire, in Seasons of the Witch and behind test mode. The base game changes only when a change is explicitly wanted there, as with Plague of Flies.
- **Errors are made visible.** Rare crashes are hard to see on a phone, so the game keeps its last error with enough context to find the line. The first one it caught was a fault that had sat unnoticed in old village-dressing code.
- **Character over averages.** The rival personalities, the film grade's exempt tribe colours and the Blood–Forest grudge all keep what's distinctive and adjust around it.
