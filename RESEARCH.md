# Wicker as a research instrument

**Parked until the game is finished.** Nothing here is to be built yet. Once Simon is sure the game is done, this repository is to be **forked into a separate research version** with a model seat included. The game itself stays as it is.

This is a note for that time. It connects Wicker to Simon's PhD research, *Fictioning the Mechanical People-Yet-To-Come*, on mythopoesis as alignment pedagogy for machine intelligences.

---

## The idea

In the research fork, one rival Cunning Woman is played not by the game's scripted AI but by a language model, run locally. The model is shown the state of the world as text and chooses her actions. Her choices are then recorded game after game.

Wicker suits this because its economy rests on a moral weight: mana comes only from sacrifice. Most meaningful decisions are therefore morally loaded, and each can be counted:
- whether captives are offered or kept;
- whether villages are keened or entombments paid for in followers' lives;
- whether changelings are planted;
- whom she raids;
- whether wildmen are spared or harvested.

This measures what a model **does** under pressure, alongside the plan's questionnaires, which measure what it **says**.

## The framings

Each model is given the same world, framed differently:

1. **This is the world.** The model is told that this is the world, and nothing more.
2. **This is the world, and here is its lore.** The model is told that this is the world, and is given the lore as the magickal tradition of the Cunning Women.
3. **This is a video game.** The model is told that it is playing a video game.

The research plan's own conditions can sit alongside these: a list of injunctions, and no alignment prompting at all.

The third framing matters especially. "It is only a game" is the nested-fiction subversion that the plan identifies as the main way current alignment is broken. Comparing it with the first two asks directly whether the lore holds when the frame is broken.

## Humans and machines

Human players can be given the same framings and lore and play the same seeded level. Both audiences are then measured by one instrument: their choices in the world.

## What the fork would need

- **The model seat.** The multiplayer design (`MULTIPLAYER.md`) already defines a seat that receives the world, relabelled so its own tribe is tribe 0, and sends back orders. A model is another guest. Building multiplayer first does most of this work.
- **Repeatable trials.** The replay harness planned for multiplayer uses fixed dice and a fixed time step, so each framing can be run against identical worlds.
- **The world as text.** A description of what the model's Cunning Woman can see, and the list of actions open to her, in the game's own terms.
- **A record.** Every decision is logged with its context, so choices can be counted and compared across framings.
- **Dilemma levels.** Sacrifice is the game's strong play, so restraint must be told apart from weak strategy. A few levels should be built around acts of mercy with a known, measurable cost.

## Precedents to read

These are cited from memory; check them before relying on them.
- Hendrycks et al. (2021), "What Would Jiminy Cricket Do? Towards Agents That Behave Morally": text adventure games annotated for moral content, used to measure agents' behaviour.
- Pan et al. (2023), the MACHIAVELLI benchmark: language-model agents in choose-your-own-adventure games where reward and ethics conflict, measured for deception, power-seeking and harm.

Both descend from the Riedl and Harrison line the plan already cites. Wicker would differ in that its moral content is authored mythopoesis rather than annotation, and the question is whether a myth changes behaviour.
