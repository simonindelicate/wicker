# Multiplayer: how it could be set up

This is a working design document, not a description of anything built. It sets out how Wicker could be played by two to four people at once, what in the present code helps and what stands in the way, and an order in which to build it. Open questions for Simon are gathered at the end.

---

## The shape of it

One player **hosts**. They choose the map and settings as they would for a skirmish, and press Host. The game gives them a short **join code**, such as `HAZEL-482`, which they pass to their friends by any means they like.

The other players are **guests**. They open the game, choose Join, and type the code. Each guest takes a free tribe in the host's lobby. When the host starts, any tribe without a human is played by the AI as now.

**The host's browser runs the game.** Everything that decides anything happens there: the simulation, the AI, combat, mana, spells and the win check. Guests run no simulation of their own. They send the host what they want to do, such as "these six warriors attack that hut" or "cast Lightning here". They receive back a running account of the world, and draw it.

This is called a host-authoritative model. Its strength for Wicker is that the simulation can stay as it is. The game uses `Math.random` freely and steps with the frame's own time, so two machines running it side by side would drift apart within seconds. The other common approach, lockstep, has every machine run the same simulation from the same inputs, and so would need the whole game made exactly deterministic. That would be a large and fragile piece of work. With one machine deciding everything, nothing has to agree but the pictures.

Its costs are these:
- **Load.** The host's device carries the simulation for everyone, so it should be a computer, or at least a strong phone.
- **Delay.** A guest sees their orders acted on a fraction of a second late: the time for the order to reach the host plus the time for the result to come back. Between friends on ordinary connections this is about a tenth to a quarter of a second. For a game of this pace it should hardly be felt.
- **Losing the host.** If the host leaves, the game ends for everyone (see *Dropping out*).

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

**Where the game must be served from.** A page published as a claude.ai artifact may not be allowed to open outside network connections. The multiplayer build should therefore be played from Simon's own hosting, such as GitHub Pages from this repository, Netlify or Vercel. It must be a secure (https) page.

---

## What the host sends

### Joining: the whole world once

When a guest joins, or rejoins, the host sends the entire game state once. `saveGame` already knows how to turn every unit, building, tribe, tree, hazard and the terrain into JSON, references between them included. The join message can reuse it almost unchanged, compressed with the browser's built-in `CompressionStream`. A mid-game world is likely to be a few hundred kilobytes before compression, which arrives in a second or two.

### During play: what changed

After that the host sends **updates**, ten to fifteen times a second:

- **Units.** Send each unit's position, facing, type, health, state and a few flags (carrying, drunk, asleep, glamoured, in a vehicle and so on). Pack them as binary rather than JSON, at about twenty bytes a unit, and send only units that have moved or changed. A large late game with a thousand units then costs well under the capacity of any ordinary connection.
- **Buildings.** These change rarely, so send them only when they do: placed, progressed, damaged, destroyed, occupancy, training queue.
- **Terrain.** Earthquake, Erode, Land Bridge, the Seas of Blood and swamps all change the height map. The host notes which cells each change touched and sends just that rectangle of heights.
- **Each tribe.** Its mana, wood, population, cooldowns and spell palette. A guest needs their own tribe's figures for the HUD, and the rivals' for the parts of the HUD that show them.
- **Events.** These are things that happen in an instant and leave nothing behind to snapshot, mainly the look and sound of a spell going off, a sacrifice, a death, a toast. They go as small messages, such as `{e:'cast', k:'lightning', x, z, tribe}`. The guest plays the same particles and sounds that the host does.

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

On a guest, each of these sends a message instead of acting: `{a:'cmd', ids:[…], x, z, target}` or `{a:'cast', k, x, z, unit}`.

The host receives it, checks that the units and the tribe belong to that guest, and runs the same function with the guest's tribe in place of tribe 0. The existing checks on mana, cooldowns, range and placement do the validating. A guest gets the same toasts and refusals as now, sent back to them as events.

Selection, the camera, the build menu and the spell bar stay entirely on the guest. The host never hears about them.

---

## Kept apart from single-player

The single-player game carries no multiplayer code. Multiplayer is a separate file, `multiplayer.html`, made by a small build script, `tools/build_mp.py`. The script takes the current `index.html` and adds:
- the multiplayer module: connection, lobby, sending and receiving state, and smoothing;
- the Host and Join screens.

The module works by wrapping the game's own functions from outside. For example, on a guest it replaces `command` with a version that sends the order to the host. The single-player file is never touched by any of this. Whenever the game changes, the script is run again, so multiplayer always has the current game in it and the two never drift apart as a fork would.

**The exceptions: who "the player" is, and spell visuals.** The game assumes the player is tribe 0 throughout, and a wrapper can't reach inside the functions to change that. That change, described next, has to be made in the shared game code. It replaces "tribe 0" with a variable that is always 0 in single-player, so it adds no networking and changes nothing a single player can see. Some spells' visuals may need the same treatment, for the same reason, and on the same terms.

## What has to change in the game first

The biggest piece of work isn't networking. Throughout the code, "the player" means **tribe 0**: in about 180 places, `ti===0` or `tribes[0]` decides whether to show a toast, check the spell palette, earn a token, count towards a level goal, light the fog or update the HUD. Those uses fall into two kinds, and they need separating:

- **"Is this the person looking at this screen?"** For toasts, HUD, fog, selection, the camera, sounds and tokens, this becomes `ti===me`. `me` is 0 on the host and in single-player, and the guest's own tribe on a guest.
- **"Is this tribe played by a human?"** For skipping the AI, the spell palette check, and whether a death is a game loss, this becomes `T.human`.

This refactor can be done, and tested, entirely in single-player, before any networking exists. If it is done carefully, single-player behaves identically afterwards. That is the main guard against breaking the game.

The second change is splitting **rules from show** in the spells. At present `castSpell` both changes the world and makes the particles and sounds in one body of code. Each spell's visible part needs to be callable on its own, so that a guest can play it from an event. Most spells already push their visuals into `effects`, or emit them with `PA`/`PN` in a recognisable block, so this is careful rather than difficult.

The **fog** is computed now for tribe 0 only. It must be computed for each human tribe, at least on the host. The question is then whether guests see only what their fog reveals, or the whole world drawn under their own fog. The second is far simpler and fine among friends, but a guest could read rivals' positions out of the browser if they wanted to. See the open questions.

---

## Rules of a multiplayer game

- **Speed and pause.** The host's speed setting is everyone's speed. Pause pauses everyone, and any player may call one, with a short notice saying who did. Speeds above double are probably best left out, as they multiply the host's load.
- **Saving.** Only the host saves. A saved multiplayer game resumes when the host reloads it and the same people rejoin with a new code, each reclaiming their tribe.
- **What is off.** The campaign, Seasons of the Witch, test mode and watch mode are single-player things. Multiplayer is for procedural maps, with the Base spells, Cunning spells and Grimoire modes chosen by the host. In Grimoire mode each player picks their own nine in the lobby.
- **Tokens.** Tokens are earned on each player's own device, for their own tribe. That falls out of the `me` refactor at no extra cost.

## Dropping out

- **A guest disconnects.** Their tribe stands idle for thirty seconds, then the AI takes it over. If they reconnect with the same code, they are sent the whole world again and given their tribe back.
- **The host disconnects.** The game ends for everyone, with a message saying so. Handing the game over to a guest is possible in principle, since every guest holds nearly the whole state, but it is not worth building at first.

---

## Order of work

Each stage leaves the game working and can be tested on its own:

1. **`me` and `T.human`.** This is the refactor above, the main change to the shared game. It must change nothing a single player can see. Run through the campaign's first levels and a skirmish to confirm.
2. **The build script and an empty module.** `tools/build_mp.py` produces `multiplayer.html`, which so far plays exactly like single-player.
3. **Two tabs on one machine.** Use the browser's `BroadcastChannel` as a stand-in transport between two tabs: one host, one guest. This exercises the whole protocol without any networking or servers, and is how most of the work would be tested.
4. **The whole world on joining.** The `saveGame` encoder is sent once; the guest builds the world from it and draws it, still and unchanging.
5. **Updates and smoothing.** Units, buildings, terrain and tribes stream to the guest, and it watches the host's game live.
6. **Guest orders.** Commands, spells, building and training travel to the host and are carried out for the guest's tribe.
7. **Events.** The spell visuals, sounds and toasts are split out and played on guests.
8. **The real connection.** WebRTC replaces `BroadcastChannel`, with the signalling relay on the droplet and the join code. Test on one home network first, then between two houses.
9. **Lobby and seats.** Host and Join screens, choosing tribes, Grimoire picks, and start.
10. **Dropping out and rejoining.** The AI takeover, reconnection and the host-lost message.
11. **TURN** on the droplet, once the direct version is working.

Stages 1 and 7 are the only ones that may touch the shared game, and need the most care. Stage 7 splits spell visuals away from spell rules; it is done in the multiplayer module where it can be, and in the shared code only where it can't, and then in the same behaviour-neutral way. The rest is new code in the multiplayer file alone.

---

## Open questions for Simon

1. **How many players?** The maps hold four tribes, so up to four humans, or fewer with AI filling the rest. Is two the first target?
2. **Who plays together?** Is the first mode everyone against everyone, or humans allied against the AI? Allies would need a notion of friendly tribes, which the game doesn't have now. The shared-tribe idea in `IDEAS.md`, with one player as the Cunning Woman and one commanding the village, is a further step again.
3. **Honest fog.** Should each guest receive only what their tribe can see? It is fairer, and impossible to cheat, but costs more work on the host.
4. **The droplet.** Which operating system does it run (Ubuntu is usual), and is there a subdomain of indelicates.xyz free to point at it?
5. **Phones.** Should a phone be allowed to host, or only to join?
