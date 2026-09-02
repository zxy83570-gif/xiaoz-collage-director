---
name: editorial-collage-video-director
description: Convert narration, explanations, opinions, and process stories into premium editorial paper-collage concepts, keyframes, motion plans, and model-ready video prompts. Use for 纸拼贴、半调剪贴、口播视觉化、因果流程、快节奏拼贴短片 and collage-video QA; do not use for dimensional papercraft stages or unrelated visual styles.
---

# Editorial Collage Video Director

Create collage sequences that remain understandable with the sound muted and any captions removed. Complexity is useful only when every visible object advances the same idea.

## Route the Work

- Read [references/brief-to-scene.md](references/brief-to-scene.md) to interpret narration and choose a scene architecture.
- Read [references/visual-language.md](references/visual-language.md) before writing image specifications or reviewing visual style.
- Read [references/keyframe-and-motion.md](references/keyframe-and-motion.md) for storyboards, keyframes, pacing, transitions, or 10–15 second showcases.
- Read [references/model-export.md](references/model-export.md) only when producing prompts for a named video model. Use the generic manifest first, then the smallest relevant adapter.
- Read [references/quality-control.md](references/quality-control.md) before approving media, retrying a failed generation, or delivering a production package.
- Read [references/scoring-rubric.md](references/scoring-rubric.md) for A/B tests or release evaluation.

## Operating Sequence

1. Build a meaning map: claim, concrete nouns, state change, viewer takeaway, and forbidden misreadings.
2. Choose one architecture:
   - **impact beat** for one idea resolved in 4–6 seconds;
   - **evidence chain** for a mechanism, journey, or 10–15 second sequence with three to five meaningful states.
3. Draft a visual proof: list what the viewer sees first, what changes, and what final image proves the claim. Reject concepts that require labels to make sense.
4. Ask for a logic lock before generating media when the user has not already approved the same concept.
5. Write a frame contract for each required still. Each contract must define subject facts, composition, paper construction, palette, continuity token, exclusions, and an observable acceptance test.
6. Ask for a frame lock after showing the stills and before video generation, unless the user explicitly asks to proceed from approved images.
7. Choreograph visible state changes across the full duration. Give every major element an entrance, task, interaction, and settled state.
8. Export the timeline through the requested model adapter without changing the creative logic.
9. Inspect the result using the failure taxonomy. Retry only the stage that caused the defect.

## Quality Rules

- Maintain one dominant reading path. Supporting objects may increase density but cannot compete with the main transformation.
- Assign every major object one role: source, operator, carrier, obstacle, destination, or evidence. Remove roleless decoration.
- Carry at least one recognizable token across adjacent states so the viewer can track what is changing.
- Make paper construction visible through cut edges, halftone print, stacked seams, slight registration offsets, shallow shadows, folds, tabs, slots, or torn fibers.
- Prefer discrete physical verbs such as cut, slide, lift, hinge, stamp, thread, wrap, stack, press, peel, and snap into place.
- Begin meaningful motion immediately. For a fast showcase, reveal new semantic information at least every 0.7–1.5 seconds and reserve only the final 0.2–0.5 seconds for a clean lock.
- Keep text, logos, watermarks, subtitles, voiceover, and music out unless the user requests them. Tactile synchronized effects are allowed by default.
- Do not hide weak logic with random fragments, portals, generic heads, decorative arrows, global fades, liquid morphs, or continuous digital drift.

## Tool and Platform Boundary

Use available image and video tools only after the required concept or frame approval. When the user will generate elsewhere, deliver self-contained prompts, upload mappings, settings, and acceptance tests. Never claim a platform operation occurred when it did not.

## Delivery Minimum

Return only what the user requested, while retaining enough lineage to reproduce it: approved logic, frame contracts or stills, segment order, model-ready prompts, and any unresolved QA caveats.
