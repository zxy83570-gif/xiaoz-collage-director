# Keyframes and Motion

Use this reference to design still sequences and timed movement.

## State Ladder

For an evidence chain, write a ladder before prompts:

| State | New fact | Dominant subject | Continuity token | Entry action | Exit condition |
|---|---|---|---|---|---|

The new fact column must differ on every row. The exit condition should be a stable image that can serve as the next segment's source.

Use three states for a simple mechanism, four for a clear journey, and five only when each intermediate transformation is essential. More states inside 15 seconds usually reduce legibility.

## Segment Boundaries

Choose a boundary where the tracked subject is momentarily recognizable, not during a blur, fold, or occlusion. Adjacent frames should share:

- the same token anchors;
- compatible screen direction;
- one overlapping object or spatial landmark;
- a plausible physical path between the states.

If two states require teleportation, insert a transfer state or use a motivated editorial cut instead of pretending the motion is continuous.

## Motion Score

Write movement as beats with four parts:

`time window — actor — physical verb — result`

Example:

`0.00–0.55 — three printed beans — tumble from a torn sack — settle along the red diagonal stripe.`

Every beat must change at least one of: position, form, ownership, quantity, connection, or meaning.

### Fast 10–15 second sequence

- Start visible action within the first 0.15 seconds.
- Use 0.35–1.20 seconds for most micro-actions.
- Introduce a new semantic fact every 0.7–1.5 seconds.
- Let overlapping secondary motions bridge beats, but keep one dominant action at a time.
- Use the last 0.2–0.5 seconds as a stable visual lock.
- Avoid a long opening reveal, empty camera travel, or a final hold longer than needed for recognition.

### Short 4–6 second impact beat

- Establish the premise in less than 0.5 seconds.
- Use two to four discrete assembly actions.
- Resolve the claim by roughly 85–92% of the duration.
- End with a compact physical click, press, or settle rather than a fade.

## Physical Motion Vocabulary

Prefer motions that expose material construction:

- slide under or over;
- hinge from a paper joint;
- unfold along a scored crease;
- thread through a cut slot;
- stamp and leave an ink impression;
- peel from adhesive backing;
- stack, compress, and spring back slightly;
- split along a perforation;
- rotate on a brass fastener;
- stitch two cutouts together;
- snap into a die-cut opening.

Avoid smooth hovering, liquid transformation, particle evaporation, unrestricted 3D rotation, or camera motion that substitutes for object action.

## Camera

Default to a mostly frontal editorial composition with small purposeful moves. Use a push, pull, pan, or short track only when it reveals a new relationship. Do not combine aggressive camera motion with several simultaneous object transformations.

## Sound Map

Tie sound to contact events: paper scrape, card flick, staple click, scissor snip, thread pull, tape peel, stamp thump, or layered paper rustle. Keep sound sparse enough that each event confirms an action.

Unless requested, exclude narration, dialogue, subtitles, and music. For several generated clips under one narration, add one continuous voice track in post rather than generating a new voice per segment.

## Frame Lock

Before writing video prompts, show the keyframes in order and verify:

- the meaning is readable without captions;
- token anchors persist;
- every transition has a plausible path;
- the final frame proves the claim;
- there is enough difference between adjacent frames to justify animation.
