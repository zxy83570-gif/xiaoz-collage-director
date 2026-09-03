# Visual Language

Use this reference for still specifications and style review.

## Material Signature

Editorial paper collage should look assembled from photographed or printed matter, not like flat vector art with a paper texture overlay.

The target default is a high-end studio photograph of a real tabletop paper relief: warm fibrous handmade-paper ground, macro material detail, physically cut silhouettes, visible thickness, tactile overlaps, shallow directional contact shadows, and restrained cinematic depth. Combine selectively colored photoreal subject cutouts with black-and-white halftone human elements when people or hands appear. The result should feel materially real and editorially art-directed, not illustrated, CGI-rendered, or assembled from generic scrapbook stickers.

Use a deliberate mix of:

- black-and-white or selectively colored halftone photo cutouts;
- matte colored stock with visible fibers;
- warm off-white cut borders around important silhouettes;
- shallow, directionally consistent paper shadows;
- torn or scissor-cut edges chosen by narrative function;
- overlaps, tabs, slots, folds, stitches, staples, tape, and small registration offsets;
- sparse ink marks or diagram fragments that behave as physical print.

Choose three or four signature devices for a project. Using all devices at once makes the surface noisy. Preserve those exact devices, paper stock, shadow direction, camera height, and color treatment across every keyframe.

## Hierarchy

Build three depth bands:

1. **Field:** a quiet paper plane or one broad tonal division.
2. **Story layer:** the main cutouts and the transformation path.
3. **Accent layer:** small evidence pieces, texture, or directional cues.

The story layer must remain legible at thumbnail size. Use contrast, overlap, scale, and isolation before adding outlines or arrows.

## Palette

Use one neutral base, one structural dark, and one or two active colors. Assign active colors to stable narrative functions and carry those assignments through every frame.

Avoid:

- equal saturation across the whole image;
- unrelated color changes between keyframes;
- glossy gradients that erase paper character;
- brown kraft texture as a universal shorthand for handmade work.

## Official-Style Keyframe Prompt Order

MiniMax H3 has an official video-prompt grammar, but there is no equivalent universal official still-prompt field syntax. For this paper-collage workflow, write each still prompt as continuous, self-contained generation prose in the same responsibility order used across the official scene workflows:

1. **Image duty:** name the frame (`F0`, `F1`, and so on), its narrative state, and whether it opens, closes, or bridges a segment.
2. **Preserved subject facts:** identity, count, shape, orientation, color, material facts, and any continuity token. State what must not change.
3. **Style and material:** editorial collage treatment, selected paper stocks, halftone behavior, cut edges, seams, folds, fasteners, and registration offsets.
4. **Composition and aspect ratio:** camera view, reading direction, scale hierarchy, placement, crop, and empty space.
5. **Background and space:** paper field, depth bands, overlaps, and spatial relationship between elements.
6. **Lighting and shadows:** light direction, softness, shallow contact shadows, and consistent layer depth.
7. **Visible text:** reproduce user-approved wording exactly in double quotes, or explicitly require no readable text.
8. **Exclusions:** logos, watermarks, fake interfaces, duplicated subjects, wrong materials, unrelated styles, or other likely failures.
9. **Handoff interface:** identify the exact carrier, prop edge, partial next-stage object, or spatial landmark that exits toward or enters from the adjacent frame.
10. **Acceptance test:** one or more visible yes/no conditions, including exact object counts when continuity depends on them.

This order is an official-method synthesis, not a fabricated universal MiniMax image schema. Do not output invented field names unless the target image tool requires them. Do not rely on “same style as before”; repeat identity-critical details in every prompt.

## Target Image Look

Unless the user explicitly supplies another art direction, make every F0–Fn prompt target this same production look:

- one standalone wide 16:9 frame, preferably 1672 × 941 when the image tool supports that size;
- premium analog editorial paper collage staged as a real handcrafted tabletop relief and photographed in a controlled studio;
- warm cream or warm ivory handmade-paper ground with highly visible natural fibers and subtle tonal variation;
- a hybrid of selectively colored photoreal material cutouts, paper-built objects, and black-and-white newspaper-halftone hands or human fragments;
- real cut edges, torn fibers where appropriate, visible paper thickness, layered overlaps, shallow relief, tiny registration imperfections, thread, stitching, brass fasteners, folds, slots, or woven paper construction where relevant;
- strong macro material fidelity and realistic contact between elements, with soft directional shadows falling consistently down-right;
- one structural dark plus a restrained group of deep natural active colors such as forest green, vermilion, mustard, ivory, aged copper, and ink black; adapt the hues to the subject while keeping the restrained editorial balance;
- dense, cinematic, museum-craft art direction with one dominant reading path and generous control of negative space;
- no flat vector illustration, glossy CGI, plastic 3D, children's craft aesthetic, generic scrapbook stickers, fake typography, labels, UI, watermark, collage grid, or split screen.

Do not merely list these style words. Tie the material treatment to each concrete subject: specify what is halftone, what is real fibrous paper, what is woven, what is torn, which edge is raised, what casts a shadow, and how the tracked carrier physically connects the process.

## Image-Prompt Delivery Form

Return each keyframe as a named full English prompt, not as a specification table alone:

```text
F0 — [short state name]
Create one standalone 16:9 keyframe for a premium analog editorial paper-collage film, staged as a real handcrafted tabletop relief and photographed in a controlled studio. [Describe the exact narrative state, subjects, counts, poses, materials, and preserved carrier.] [Describe the target image look using concrete material assignments.] [Describe composition, crop, hierarchy, and reading direction.] [Describe the fibrous paper field, depth layers, incoming and outgoing handoff elements.] [Describe light direction and shallow contact shadows.] No readable text, letters, numbers, logos, subtitles, UI, watermark, grid, split screen, flat vector illustration, glossy CGI, plastic 3D, duplicated subjects, or unrelated decoration. Acceptance: [visible yes/no conditions].
```

For F1 and later, repeat the complete shared visual system and all identity-critical facts. Explicitly describe both the incoming remnant from the previous state and the outgoing preview of the next state. The prompt must be usable directly in the image generator without consulting the storyboard table.

## Continuity Token

A token is a recognizable feature that survives transformation. It may change form but must retain at least two anchors such as color, edge pattern, printed motif, position of a notch, thread path, or distinctive silhouette.

Examples:

- a red diagonal stripe moves from bean sack to shipping label to cup sleeve;
- a blue bottle cap becomes blue polymer flakes and then a blue zipper pull;
- a punched circular hole persists through ticket, data packet, and destination card.

Do not use a generic arrow as the only token.

## Continuous Keyframe Construction

- Generate every keyframe as a separate full-frame image, never as a grid, contact sheet, split screen, or storyboard page.
- Keep one photographed physical world across F0–Fn: identical aspect ratio, paper field, camera height, lens character, material scale, light direction, shadow softness, palette logic, and print treatment.
- Carry one unmistakable physical token through the whole chain. Preserve at least two stable anchors such as color plus stitching, shape plus notch, or strand plus printed motif.
- At the outgoing edge of each frame, preview a small but concrete component of the next state. In the next frame, retain that component at the incoming side so the FL2VA path is spatially and materially plausible.
- Make every frame dense enough to feel finished but give it one dominant process state. The still must remain readable at thumbnail size.
- Prompts must specify exact counts for duplicated-risk elements such as hands, subjects, cocoons, reels, spools, stitches, tools, or containers.

## Gate 2 — Continuous Keyframe Lock

Show or identify the actual generated F0–Fn images in order, not only their prompts. Approve the complete chain before writing video prompts. Reject the set if a frame is individually attractive but breaks the shared material world or lacks a plausible incoming/outgoing handoff.

## Still QA

Reject a still when:

- the main action cannot be described from the image alone;
- paper depth is absent or physically inconsistent;
- the tracked token is missing or ambiguous;
- the scene contains fake lettering or a pseudo-interface;
- adjacent frames change palette, lighting, scale logic, or subject identity without narrative cause;
- visual density comes from decorative fragments rather than evidence.
