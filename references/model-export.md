# MiniMax H3 Official Prompt Export

Use this reference whenever the requested video model is MiniMax H3. Creative planning may be model-neutral, but the final prompt must use the official mode logic, field names, ordering, timing rules, reference duties, and audio classification below.

## 1. Choose the Input Mode First

- **T2VA:** text alone defines the complete audiovisual timeline.
- **I2VA:** an approved opening image is fixed at 0.00 seconds and the action develops forward.
- **FL2VA:** approved opening and closing images define a continuous, reachable transformation. This is the default for the continuous-keyframe paper-collage workflow.
- **L2VA:** an approved closing image is the only essential anchor; infer a plausible earlier state and converge precisely to it. Use only when the user actually supplies no approved opening frame.
- **Ref2VA:** several image, video, or audio references carry distinct subject, keyframe, motion, timing, editing, or sound duties.

Do not choose a richer mode merely because files were uploaded. One reference gets one clear primary duty. A still used only for identity is a subject reference, not automatically a picture keyframe.

One generation must be 4–15 seconds and the written timeline must end at the requested duration. This workflow defaults to 5 seconds per adjacent-frame FL2VA segment and joins the segments in order with direct cuts.

## 2. T2VA, I2VA, FL2VA, and L2VA Structure

T2VA begins directly with the three fields. I2VA, FL2VA, and L2VA place the corresponding keyframe time-alignment instruction first, followed by one blank line and exactly these fields in this order:

```text
integrated_multimodal_description: [Shot 1] ...

overall_soundscape: ...

non_diegetic_music: ...
```

The keyframe instruction must identify each supplied image and its exact role and time. Map an opening image to 0.00 seconds and a closing image to the requested end time. Use the target interface's actual picture identifiers; do not invent uploaded files.

Path logic:

- I2VA: anchored opening state → action begins → continuous development → result or reaction.
- FL2VA: opening state → observable intermediate changes → shrinking difference → exact closing state.
- L2VA: plausible preceding state → explicit action or transition → gradual convergence → exact closing state.

## 3. Main Description

`integrated_multimodal_description` follows playback order and includes the visual style, composition, subjects and positions, environment, lighting, physical actions, state changes, camera, dialogue or singing, synchronized diegetic sounds, and the moment each reference becomes visible or operative.

- Start with `[Shot 1]` and no timestamp.
- Write later cuts as `[Shot N] At MM:SS.mmm, ...`; times must be strictly increasing and inside the duration.
- Add a cut only when it introduces a new subject, space, state, viewpoint, or time. Prefer camera movement when only distance or angle changes.
- Use natural camera language and distinguish Zoom from Push/Pull, Pan from Truck, and Tilt from Pedestal.
- State both what changes and what remains invariant. End in a clearly observable final state.
- For paper collage, use discrete physical verbs and the official motion pattern: appear or slide in → slight rebound → press flat → pause → lock.
- Put essential prohibitions briefly in the main description only when they prevent a likely failure; H3 has no separate negative-prompt field in this format.

### Required FL2VA Density

For every `F(n)→F(n+1)` prompt, write the full runnable English prompt rather than a synopsis. The main description must:

1. identify the exact Picture 1 state and enumerate every identity- or continuity-critical visible element, including exact counts;
2. name the global paper field, material treatment, palette, paper thickness, light, shadow direction, carrier token, and handoff elements that must remain stable;
3. state `Motion begins immediately` and cover the complete 5 seconds through several ordered time windows;
4. give each time window concrete actors, physical paper verbs, spatial directions, and observable results;
5. keep the continuity carrier visible and intact while old elements exit and new elements assemble;
6. converge all object positions, counts, poses, scale, palette, lighting, shadows, and framing precisely to Picture 2 by roughly 4.70–4.75 seconds;
7. hold the exact Picture 2 state only for the final 0.25–0.30 seconds;
8. specify one restrained camera behavior and stop it before the final lock;
9. end with a compact `No ...` clause covering the likely failures for that segment;
10. provide synchronized tactile events in `overall_soundscape` and normally use `non_diegetic_music: N/A`.

Use this exact delivery skeleton:

```text
Reference timing:
Picture 1 is the opening image at 0.00 seconds.
Picture 2 is the closing image at 5.00 seconds.

integrated_multimodal_description: [Shot 1] ...full opening inventory and invariants... Motion begins immediately. From 0.00 to ... seconds, ... From ... to 4.70 seconds, ... All ... converge precisely to Picture 2. Hold the exact Picture 2 composition only from 4.70 to 5.00 seconds. ...camera... No ...

overall_soundscape: ...synchronized physical sounds... No voices.

non_diegetic_music: N/A
```

Do not replace this with bullets, a table, a generic timeline manifest, terse instructions, or explanatory prose. When several segments are requested, output one complete standalone block or `.txt` file per segment.

## 4. Sound, Dialogue, and Visible Text

`overall_soundscape` is 1–4 English sentences summarizing ambience, physical action sounds, and nonverbal human sounds. Do not repeat dialogue, singing, or diegetic music. Use `N/A` only when the entire film is intentionally silent.

`non_diegetic_music` is 1–3 English sentences describing audience-only music through instrumentation, tempo, rhythm, and dynamics. Use `N/A` when there is no score. Music audible to characters belongs in the main description.

- Assign `(S1)`, `(S2)`, and so on only to actual sound sources; keep the same speaker number across shots.
- Write dialogue and lyrics as `<d>[Language] original content</d>`. Preserve user or reference wording and punctuation; write `[unclear]` instead of guessing.
- For off-screen narration, state `says in an off-screen voiceover` and specify that visible characters' lips remain fully closed.
- Use `<scenetrans>` when speech continues across a cut and `<cutoff>` when it is intentionally cut off at the end.
- Put truly visible signs, titles, labels, or captions in English double quotes and preserve their wording exactly.
- Structural prose is English; dialogue, lyrics, and visible text remain in their original language.

## 5. Ref2VA Fixed Structure

Ref2VA uses exactly these six sections in this order:

```text
subject_definitions:
summary:
retention_analysis:
detailed_description:
overall_soundscape:
non_diegetic_music:
```

Reference labels are duties, not upload-order aliases:

- `<Subject N>`: visible people, animals, objects, scenes, clothing, props, interfaces, actions, poses, styles, or effects reused or modified in the target.
- `<Picture N>`: an image acting as an opening, key, closing, editing, composition, or storyboard anchor.
- `<Video N>`: an entire source video used for direct editing, continuation, or whole-video camera, edit, rhythm, or timing structure.
- `<Audio N>`: an audio signal copied or referenced for track content, timbre, rhythm, music style, dialogue, lyrics, or sound quality.

Do not create `<Audio N>` merely because a reference video contains sound. `<Video N>` and `<Audio N>` number independently. Keep every label's meaning stable across all six sections.

Begin `summary` with the task types that actually apply: `keyframe completion`, `reference generation`, `video editing`, `video continuation`, `audio reuse`, or `audio reference`. Uploading media alone does not imply editing, continuation, or audio reuse.

In `retention_analysis`, use only these relation markers:

- visual: `fully_preserved`, `partially_preserved`, `attribute_transfer`, `weak_reference`;
- audio: `fully_copy`, `partially_copy`, `reference`, `weak_reference`.

Give each independent label one line stating where it appears, what is retained, and what changes. New target-story content is not automatically a reference-fidelity loss.

Start `detailed_description` with 1–2 English sentences establishing the whole-film style, then use the official shot syntax. Generation tasks normally use 350–500 English words, but a complete timeline and intact dialogue take priority over a mechanical word count. Insert each label where its duty first becomes clearly active. Do not reduce the section to a synopsis or reference inventory.

Reference audio used only for voice, rhythm, emotion, or delivery does not authorize reuse of its dialogue. Reproduce reference dialogue or lyrics only when direct reuse or re-performance is explicitly requested.

## 6. Final Compliance Check

Before delivery, verify mode choice, duration, keyframe times, field order, shot numbering, strictly increasing cut times, stable speaker IDs, exact dialogue and visible wording, reference-label duties, retention markers, sound classification, invariants, and the terminal state. Run `scripts/validate_export.py` for structural checks.

If the target is not H3, retain the approved creative logic but use that model's real syntax. Never present a generic manifest as an official H3 prompt.
