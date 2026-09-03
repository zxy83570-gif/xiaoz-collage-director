# Editorial Collage Video Director

Turn narration, opinions, and concrete processes into high-density editorial paper-collage storyboards and video prompts.

The workflow creates a continuous sequence of photographed analog paper-collage keyframes and exports one complete 5-second MiniMax H3 FL2VA prompt for every adjacent frame pair.

## Included

- Continuous F0–Fn keyframe-chain design
- Default 5-second FL2VA generation for every adjacent frame pair
- Visual-density and continuity controls
- High-end photographed physical paper-relief prompting and Gate 2 chain lock
- T2VA, I2VA, FL2VA, L2VA, and fixed six-section Ref2VA export
- Prompt and package validators
- Ten-case A/B evaluation kit

## Workflow

1. Provide the narration, opinion, explanation, or process story together with the target duration and aspect ratio.
2. Build a meaning map covering the central claim, concrete objects, visible state change, intended takeaway, and likely misreadings.
3. Create and approve Gate 1: meaning, metaphor, paper-collage direction, duration, aspect ratio, sound policy, exclusions, and acceptance criteria.
4. Write the still prompt in official responsibility order: duty, preserved facts, style/material, composition, background/space, lighting/shadows, visible text, exclusions, and acceptance test.
5. Generate and approve all actual F0–Fn frames together at Gate 2, including their shared carrier and edge handoffs.
6. Pair adjacent frames and default to one 5-second FL2VA clip per pair.
7. Write full English prompts with the exact opening inventory, timed physical transformations, Picture 2 convergence, camera, prohibitions, tactile soundscape, and music policy.
8. Export using the official three-field basic structure or fixed six-section Ref2VA structure.
9. Review meaning, continuity, material quality, pace, timing, and endpoint accuracy; retry only the stage that caused the defect.

## Install

Copy this folder into a compatible agent's skills directory. The entrypoint is `SKILL.md`.

## Validate

```bash
python3 scripts/preflight.py .
python3 scripts/test_validators.py
python3 scripts/validate_export.py path/to/prompt.txt --adapter h3
python3 scripts/build_release.py . --output-dir dist
```

## Evaluation

Use `benchmarks/README.md` and `benchmarks/cases.json` to compare this skill with an existing workflow under identical generation settings. Structural validation does not prove equal visual quality; the release decision should use blind media scoring.

## License

Released under the MIT License. See `RELEASE_QA.md` for completed validation.
