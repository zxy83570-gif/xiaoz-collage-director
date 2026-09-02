# Model Export

Create a model-neutral timeline first. Apply a platform adapter only after the creative plan is stable.

## Generic Timeline Manifest

Record:

- target model and generation mode;
- duration and aspect ratio;
- reference-file bindings and their duties;
- global visual construction;
- invariant subject and token anchors;
- ordered motion beats;
- camera behavior;
- synchronized physical sounds;
- music, narration, dialogue, and visible-text policy;
- exact terminal state;
- prohibited failures.

The manifest is the source of truth. An adapter may translate syntax but must not invent new story actions or remove continuity anchors.

## MiniMax H3 Compatibility Adapter

Use this section only when the user requests MiniMax H3.

### Mode choice

- Use text-only generation when no image identity or composition needs anchoring.
- Use an opening image when the first frame must be preserved.
- Use opening and closing images when the path between two approved states is the main task.
- Use a closing image when the exact final composition matters more than the inferred start.
- Use a reference-rich mode only when multiple media files carry distinct identity, motion, timing, or audio duties.

For dense collage journeys, prefer several short opening/closing-image segments over one overloaded 15-second interpolation. One segment should express one dominant transformation.

### Basic export structure

For a text-only request, output these fields in this order:

```text
integrated_multimodal_description: [Shot 1] ...

overall_soundscape: ...

non_diegetic_music: ...
```

When images anchor the start or end, place a plain-language reference timing block before the fields. Name each uploaded picture and its exact time, for example:

```text
Reference timing:
Picture 1 is the opening image at 0.00 seconds.
Picture 2 is the closing image at 5.00 seconds.

integrated_multimodal_description: [Shot 1] ...

overall_soundscape: ...

non_diegetic_music: N/A
```

Write the structural prose in English. Preserve user-supplied dialogue or visible wording exactly when it must appear.

### Main description

The main field must cover the complete duration in playback order. Include:

- editorial collage construction and composition;
- which elements remain fixed;
- the tracked token and its retained anchors;
- each physical action and its result;
- purposeful camera behavior;
- synchronized contact sounds at the action that produces them;
- progressive convergence to the closing image when one is supplied.

Do not use a separate negative-prompt field. State essential exclusions briefly inside the main description only when they prevent a likely failure.

### Sound fields

Use `overall_soundscape` for a concise summary of ambience, physical effects, and nonverbal human sound. Do not repeat dialogue. Use `N/A` only for deliberate total silence.

Use `non_diegetic_music` for music heard by the audience but not produced inside the scene. Write `N/A` when music is not requested.

### Duration and cuts

Keep target duration within the currently supported model range. Timed beats must end at the requested duration. If the prompt contains multiple shots, later cut times must be strictly increasing and must introduce meaningful new information.

### Opening/closing-image path

Describe an observable route:

1. identify the exact opening arrangement;
2. start the first physical action immediately;
3. preserve the continuity token during intermediate changes;
4. reduce the visible difference from the closing image beat by beat;
5. match the closing composition, count, palette, and token anchors precisely.

Do not request an unrelated transition merely because it looks dramatic.

### Reference-rich export

When the selected H3 interface requires a structured multi-reference prompt, follow the interface's current schema exactly. Define each reference once and give it one primary duty. Separate identity, keyframe, motion, timing, and audio responsibilities; do not assume that a file's upload order defines its role.

## Other Models

For another video model, retain the generic manifest and translate only:

- reference notation;
- supported duration;
- keyframe capabilities;
- prompt field syntax;
- audio support;
- model-specific prohibited combinations.

If the target format is unknown, deliver the manifest rather than guessing syntax.
