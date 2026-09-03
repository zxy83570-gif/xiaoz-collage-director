---
name: editorial-collage-video-director
description: Convert narration, explanations, opinions, and process stories into premium editorial paper-collage concepts, official-style still prompts, and MiniMax H3-compliant video prompts. Use for 纸拼贴、半调剪贴、口播视觉化、因果流程、快节奏拼贴短片 and collage-video QA; do not use for dimensional papercraft stages or unrelated visual styles.
---

# Editorial Collage Video Director

Create visually continuous keyframe chains and production-ready H3 prompts in the same form as the approved official workflow example in `h3-paper-collage-silk-journey-20s`: premium photographed analog paper-collage frames followed by one full FL2VA prompt for every adjacent frame pair. Local planning and QA may add rigor, but must not replace, shorten, rename, or contradict the required output.

## Route the Work

- Read [references/brief-to-scene.md](references/brief-to-scene.md) to extract meaning and produce the official-style Gate 1 production plan.
- Read [references/visual-language.md](references/visual-language.md) before writing the complete keyframe-chain image prompts or reviewing Gate 2 frames.
- Read [references/keyframe-and-motion.md](references/keyframe-and-motion.md) before designing adjacent-frame handoffs or writing the segment motion.
- Read [references/model-export.md](references/model-export.md) whenever producing a MiniMax H3 prompt. Its mode choice, field order, reference duties, dialogue rules, and Ref2VA schema are mandatory.
- Use [examples/coffee-route-h3.txt](examples/coffee-route-h3.txt) as the minimum density and formatting example for each FL2VA segment; never return a shorter summary in place of a runnable prompt.
- Read [references/quality-control.md](references/quality-control.md) before approving media, retrying a failed generation, or delivering a production package.
- Read [references/scoring-rubric.md](references/scoring-rubric.md) for A/B tests or release evaluation.

## Operating Sequence

1. Extract the core meaning, emotion, action verb, and visual metaphor from the source.
2. Produce **Gate 1 — production plan**: target meaning, visual metaphor, paper-collage direction, aspect ratio, duration, sound policy, exclusions, and acceptance criteria. Obtain approval unless the user already approved the same plan.
3. Convert the narrative into `F0` through `Fn`. Each frame is a complete visible state, and every adjacent pair must share a physical continuity carrier plus an edge handoff that makes the next transformation reachable.
4. Write one self-contained image-generation prompt per frame in the official scene-workflow responsibility order: image duty; preserved subject facts; target visual signature; composition and aspect ratio; background and space; lighting and shadows; visible text; exclusions; acceptance test. Repeat all identity-critical facts instead of saying “same as previous.”
5. Generate or hand off all frame prompts. **Gate 2 — continuous keyframe lock** approves the actual F0–Fn images together for style, palette, material, scale, light, carrier identity, and adjacent handoffs before video prompting.
6. For this workflow, default to a chain of 5-second FL2VA clips: `S01: F0→F1`, `S02: F1→F2`, and so on. Use another H3 mode only when the available inputs genuinely require it.
7. Write every segment as a complete English H3 prompt with reference timing, the official three fields, an exact opening inventory, explicit invariants, dense sequential time windows, physical paper actions, exact convergence to Picture 2, restrained camera behavior, likely-failure prohibitions, synchronized tactile sound, and explicit music policy.
8. Inspect the result using the failure taxonomy. Retry only the stage that caused the defect.

## Quality Rules

- Maintain one dominant reading path. Supporting objects may increase density but cannot compete with the main transformation.
- Assign every major object one role: source, operator, carrier, obstacle, destination, or evidence. Remove roleless decoration.
- Carry at least one recognizable token across adjacent states so the viewer can track what is changing.
- Make paper construction visible through cut edges, halftone print, stacked seams, slight registration offsets, shallow shadows, folds, tabs, slots, or torn fibers.
- Prefer discrete physical verbs such as cut, slide, lift, hinge, stamp, thread, wrap, stack, press, peel, and snap into place.
- Begin meaningful motion immediately. Use 5 seconds per adjacent-frame transformation by default; the complete film length is the number of frame transitions multiplied by 5 seconds.
- Keep text, logos, watermarks, subtitles, voiceover, and music out unless the user requests them. Tactile synchronized effects are allowed by default.
- Do not hide weak logic with random fragments, portals, generic heads, decorative arrows, global fades, liquid morphs, or continuous digital drift.

## Tool and Platform Boundary

Use available image and video tools only after the applicable gate approval. When the user will generate elsewhere, deliver self-contained prompts, upload mappings, settings, and acceptance tests. MiniMax Hub nodes are available only when actually exposed; otherwise describe the result as an official-method handoff, not an official Hub execution.

## Delivery Minimum

When the user asks for prompts, return the full runnable prompts rather than a prompt-writing guide, abbreviated motion notes, or a generic manifest. Deliver image prompts as `F0`–`Fn` and video prompts as standalone `S01-F0-to-F1-H3-FL2VA` blocks or files, followed only by essential upload order and assembly instructions.
