# Multiplayer: how it could be set up

This is a working design document, not a description of anything built. It sets out how Wicker could be played by two to four people at once. The design rests on two rules.

- **The single-player game is not refactored for multiplayer.** Multiplayer lives in a separate file, and adapts the game from outside.
- **Any change to shared code must be proved to change nothing.** If multiplayer ever needs one, it is accepted only once a byte-for-byte replay test shows single-player behaving identically.

Open questions for Simon are gathered at the end.

---

## The shape of it

One player **hosts**. They choose the map and settings as they would for a skirmish, and press Host. The game gives them a short **join code**, such as `HAZEL-482`, which they pass to their friends by any means they like.

The other players are **guests**. They open the multiplayer page, choose Join, and type the code. Each guest takes a free tribe in the host's lobby. When the host starts, any tribe without a human is played by the AI as now.

**The host's browser runs the game.** Everything that decides anything happens there: the simulation, the AI, combat, mana, spells and the win check. Guests run no simulation of their own. They send the host what they want to do, such as "these six warriors attack that hut" or "cast Lightning here". They receive back a running account of the world, and draw it.

This is called a host-authoritative model. Its strength for Wicker is that the simulation can stay exactly as it is. The game uses `Math.random` freely and steps with the frame's own time, so two machines running it side by side would drift apart within seconds. The other common approach, lockstep, has every machine run the same simulation from the same inputs, and so would need the whole game made exactly deterministic. With one machine deciding everything, nothing has to agree but the pictures.

Its costs are these:
- **Load.** The host's device carries the simulation for everyone, so it should be a computer, or at least a strong phone.
- **Delay.** A guest sees their orders acted on a fraction of a second late: the time for the order to reach the host plus the time for the result to come back. Between friends on ordinary connections this is about a tenth to a quarter of a second. For a game of this pace it should hardly be felt.
- **Losing the host.** If the host leaves, the game ends for everyone (see *Dropping out*).

---

## Kept apart from single-player

Multiplayer is a separate file, `multiplayer.html`, made by a small build script, `tools/build_mp.py`. The script takes the current `index.html` and adds two things after the game's own script:
- the **multiplayer module**: connection, lobby, sending and receiving state, smoothing, and the adaptations described below;
- the **Host and Join screens**.

Nothing is edited inside the game's code. Whenever the game changes, the script is run again, so multiplayer always carries the current game and the two never drift apart as a hand-kept copy would.

**How the module reaches the game.** The game's functions are declared at the top level of its script. A second script on the same page can therefore replace them, for example swapping `command` for a version that sends the order to the host, and the game's own calls then go through the replacement. Variables the game declares with `const` can be read but not replaced, so the module works through functions wherever it can.

**Checking the build.** Each adaptation in the module names the game function it relies on. The build script checks that every one of them still exists in the current `index.html`, and refuses to build if one has gone or been renamed. A change to the game then can't quietly break multiplayer; the build says what needs updating.

---

## Each guest sees itself as tribe 0

Throughout the game, "the player" means **tribe 0**. In about 180 places, `ti===0` or `tribes[0]` decides whether to show a toast, check the spell palette, earn a token, light the fog or update the HUD. Rather than change those lines, each guest **relabels the tribes** in everything it receives.

If you are tribe 2 in the host's game, your browser swaps 2 and 0 in every unit, building, tribe and event as it arrives. It swaps them back in every order it sends. On your screen, your tribe is tribe 0, and the game's own code runs as if you were playing single-player:
- the HUD, the spell bar and the palette check;
- the fog, which the guest computes from its own units, as now;
- selection, the build menu and the camera;
- toasts, sounds and tokens, all for your tribe.

**What the swap has to cover.** Tribe numbers appear in unit and building `tribe` fields, the tribes array itself, terrain ownership arrays (hazards and salt), banners, and a few references inside units and tribes, such as a captive's original tribe. The swap is one function applied to each incoming message, and its inverse is applied to each outgoing order. A unit test can check it by swapping a whole saved game there and back and comparing the result with the original.

---

## The host's side

The host is the one place where the game's tribe-0 assumptions meet other humans. Every adjustment there is made from the module, by wrapping a known function. None of them is a scattered edit.

- **No AI for guests.** The AI runs only for a tribe that has one attached (`if(T.ai)aiThink(T)`). The module leaves `ai` empty on each guest's tribe.
- **The player's automatic upkeep.** Tribe 0 gets `playerAuto`, the everyday behaviour that keeps villagers working once a Cottage stands. The module calls it for guest tribes as well. It also wraps `hasCottage`, which looks only at tribe 0, so that each tribe's own Cottage counts.
- **Spells.** `tryCast` checks the spell palette only for tribe 0. The module makes the same check for a guest's tribe before passing the cast on.
- **Winning and losing.** `checkEnd` decides the game from tribe 0's point of view. In multiplayer, the module decides when each human is out, tells that guest, and ends the game when one side is left.
- **Toasts for guests.** Many messages are shown only when the tribe involved is 0. The module wraps `toast`, notes which tribe the message concerns, and forwards it to that guest as an event.

**What can wait.** In a few places the AI prefers to attack tribe 0, so in multiplayer it will lean slightly towards the host. That is acceptable at first, and can be balanced later from the module.

---

## Connecting: the join code

Players' browsers talk to each other directly over **WebRTC data channels**, the browser's built-in peer-to-peer connection. Once they are connected, no server sits in the middle. The one thing a server is needed for is the introduction. Two browsers can't find each other unaided, so each has to hand the other a short description of how to reach it, called an offer and an answer. Carrying those is called **signalling**.

**Signalling lives on Simon's DigitalOcean droplet.** indelicates.xyz is shared hosting on Hostinger, and Vercel and Netlify only run short-lived functions. None of them can later carry a TURN relay (see below), so the droplet is the one home for all the server parts.
- **The relay.** A small Node program, about forty lines, holds the host's offer under the join code and passes a guest's answer back. It stores nothing for longer than a lobby lasts and carries no game traffic.
- **The address.** It is served at a subdomain such as `mp.indelicates.xyz`, pointed at the droplet with one A record in the domain's DNS. Caddy gives it HTTPS and renews the certificate itself.
- **Restarts.** A systemd service restarts it after a reboot.
- **The fallback.** If the relay is ever down, the offer and answer can be swapped by hand as copy-and-paste text or a QR code, as keepsakes are shared now. That route needs no server at all.

**The first version: direct connections only.** WebRTC's direct connection covers two cases with the same code:
- **On the same network.** Two devices on the same Wi-Fi or home network connect to each other directly. This is the LAN case, and it needs no outside help beyond the introduction.
- **Across the internet.** Players on ordinary home broadband connect directly too, once a public STUN server has told each browser its outside address. Google's free STUN servers are the usual choice.

**TURN comes later.** Some networks won't allow a direct connection at all, such as some mobile carriers and strict office, university or hotel networks. Players on them need a **TURN** server, coturn, on the droplet, relaying all their game traffic. Until it exists, the game says plainly when a connection can't be made. Adding it later is a change to the connection settings only; nothing else in the design depends on it.

**Where the game must be served from.** A page published as a claude.ai artifact may not be allowed to open outside network connections. `multiplayer.html` should therefore be played from Simon's own hosting, such as GitHub Pages from this repository, Netlify or Vercel. It must be a secure (https) page.

---

## What the host sends

### Joining: the whole world once

When a guest joins, or rejoins, the host sends the entire game state once. `saveGame` already knows how to turn every unit, building, tribe, tree, hazard and the terrain into JSON, references between them included. The module can produce the same encoding by calling the game's own functions, then compress it with the browser's built-in `CompressionStream`. A mid-game world is likely to be a few hundred kilobytes before compression, which arrives in a second or two.

`saveGame` writes to the browser's storage as it goes, and refuses to run in some states. If its encoding can't be reached without that, the module carries its own copy of the encoder, checked against the game's by the build script.

### During play: what changed

After that the host sends **updates**, ten to fifteen times a second:

- **Units.** Send each unit's position, facing, type, health, state and a few flags (carrying, drunk, asleep, glamoured, in a vehicle and so on). Pack them as binary rather than JSON, at about twenty bytes a unit, and send only units that have moved or changed. A large late game with a thousand units then costs well under the capacity of any ordinary connection.
- **Buildings.** These change rarely, so send them only when they do: placed, progressed, damaged, destroyed, occupancy, training queue.
- **Terrain.** Earthquake, Erode, Land Bridge, the Blood-Running-Sea and swamps all change the height map. The host compares the height map with the last one it sent and sends just the rectangle that differs.
- **Each tribe.** Its mana, wood, population, cooldowns and spell palette.
- **Events.** These are things that happen in an instant and leave nothing behind to snapshot, mainly the look and sound of a spell going off, a sacrifice, a death, a toast. They go as small messages, such as `{e:'cast', k:'lightning', x, z, tribe}`, and the guest plays the same particles and sounds that the host does.

### Spell visuals

A spell's rules and its look are written together inside `castSpell`. The module can catch every cast by wrapping `castSpell` and forward it as an event. Replaying the look on a guest is less simple, because the visual part can't be called without the rules part. There are three ways round this, tried in this order:

1. **Forward what the host draws.** Many spells make their look through the shared particle systems and the `effects` list. The module can watch what the host adds to those during a cast and send it on.
2. **Replay the cast in a sandbox.** The guest can run `castSpell` against a throwaway copy of the nearby state, keep the particles and sounds, and discard the changes to the world.
3. **A small shared change.** For a spell neither of those handles, its visual block is moved into a function of its own. This is the one place multiplayer may need to touch the shared code, and only under the replay test below.

### Smoothing

Guests draw the world a tenth of a second behind the latest update, sliding each unit between its last two known positions. Movement then looks continuous rather than stepping ten times a second. Particles, wind, snow, water and the camera all run locally on each guest at full frame rate, as they do now.

---

## What guests send

Everything a player can do already passes through a small number of functions:
- `command` for orders to selected units;
- `tryCast` for spells;
- `placeBuilding` and the training queue for building;
- `startRitual` for the hollow hills;
- the May Queen and Changeling choices, which are taps that set a target.

On a guest, the module replaces each of these with a version that sends a message instead of acting, such as `{a:'cmd', ids:[…], x, z, target}` or `{a:'cast', k, x, z, unit}`. The tribe numbers are swapped back to the host's numbering as it goes.

The host receives the message, checks that the units belong to that guest's tribe, and calls the game's own function with the guest's tribe. The game's checks on mana, cooldowns, range and placement do the validating. Refusals and toasts come back to the guest as events.

Selection, the camera, the build menu and the spell bar stay entirely on the guest. The host never hears about them.

---

## The replay test

This is the safeguard for the single-player game. Any change to `index.html` made for multiplayer's sake has to pass it.

- **Fixed dice and time.** The test harness replaces `Math.random` with a seeded generator, and steps the simulation with a fixed time step, so the same run gives the same result every time.
- **The runs.** It plays a stretch of each of these, before and after the change:
  - several campaign levels;
  - several Seasons of the Witch levels;
  - skirmishes with every rival personality, in Base, Cunning and Grimoire modes, with the AI casting everything it has.
- **The comparison.** At the end of each run, it takes the complete saved state and compares the two byte for byte.

If one villager stands half a pace differently, the comparison catches it. A change that alters anything is rejected or fixed before it is published.

---

## Rules of a multiplayer game

- **Speed and pause.** The host's speed setting is everyone's speed. Pause pauses everyone, and any player may call one, with a short notice saying who did. Speeds above double are probably best left out, as they multiply the host's load.
- **Saving.** Only the host saves. A saved multiplayer game resumes when the host reloads it and the same people rejoin with a new code, each reclaiming their tribe.
- **What is off.** The campaign, Seasons of the Witch, test mode and watch mode are single-player things. Multiplayer is for procedural maps, with the Base spells, Cunning spells and Grimoire modes chosen by the host. In Grimoire mode each player picks their own nine in the lobby.
- **Tokens.** Tokens are earned on each player's own device, for their own tribe. On guests this follows from the relabelling at no extra cost.

## Dropping out

- **A guest disconnects.** Their tribe stands idle for thirty seconds, then the AI takes it over. If they reconnect with the same code, they are sent the whole world again and given their tribe back.
- **The host disconnects.** The game ends for everyone, with a message saying so. Handing the game over to a guest is possible in principle, since every guest holds nearly the whole state, but it is not worth building at first.

---

## Order of work

Each stage leaves both games working and can be tested on its own.

1. **The replay test.** Build it first, and run it on the current game, so it is ready before anything else happens.
2. **The build script and an empty module.** `tools/build_mp.py` produces `multiplayer.html`, which so far plays exactly like single-player, and checks the functions the module relies on.
3. **Two tabs on one machine.** The browser's `BroadcastChannel` stands in for the network between two tabs, one host and one guest. This exercises the whole protocol with no servers, and is how most of the work would be tested.
4. **The whole world on joining, relabelled.** The guest builds the world from the host's encoding, with its own tribe swapped to 0, and draws it, still and unchanging.
5. **Updates and smoothing.** Units, buildings, terrain and tribes stream to the guest, and it watches the host's game live.
6. **The host's side.** No AI for the guest's tribe, its upkeep, palette check, toasts and the win check.
7. **Guest orders.** Commands, spells, building and training travel to the host and are carried out for the guest's tribe.
8. **Spell visuals.** Forwarded or replayed on guests, by the routes above.
9. **The real connection.** WebRTC replaces `BroadcastChannel`, with the signalling relay on the droplet and the join code. Test on one home network first, then between two houses.
10. **Lobby and seats.** The Host and Join screens, choosing tribes, Grimoire picks, and start.
11. **Dropping out and rejoining.** The AI takeover, reconnection and the host-lost message.
12. **TURN** on the droplet, once the direct version is working.

Only stage 8 might touch `index.html`, and then only under the replay test. Everything else is new code in the multiplayer file, the build script and the relay.

---

## Open questions for Simon

1. **How many players?** The maps hold four tribes, so up to four humans, or fewer with AI filling the rest. Is two the first target?
2. **Who plays together?** Is the first mode everyone against everyone, or humans allied against the AI? Allies would need a notion of friendly tribes, which the game doesn't have now. The shared-tribe idea in `IDEAS.md`, with one player as the Cunning Woman and one commanding the village, is a further step again.
3. **Honest fog.** Should each guest receive only what their tribe can see? It is fairer, and impossible to cheat, but costs more work on the host. Sending everything and fogging on the guest is simpler, and fine among friends.
4. **The droplet.** Which operating system does it run (Ubuntu is usual), and is there a subdomain of indelicates.xyz free to point at it?
5. **Phones.** Should a phone be allowed to host, or only to join?
