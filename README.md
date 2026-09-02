# Editorial Collage Video Director

Turn narration, opinions, and concrete processes into high-density editorial paper-collage storyboards and video prompts.

The workflow builds a semantic plan, keyframe contracts, and a timed motion manifest before exporting to a supported video model. It includes a MiniMax H3 prompt-format adapter.

## Included

- Impact-beat and evidence-chain planning modes
- Visual-density and continuity controls
- Still-frame and motion specifications
- Generic timeline manifest and H3-compatible export
- Prompt and package validators
- Ten-case A/B evaluation kit

## Workflow

1. Provide the narration, opinion, explanation, or process story together with the target duration and aspect ratio.
2. Build a meaning map covering the central claim, concrete objects, visible state change, intended takeaway, and likely misreadings.
3. Choose an impact-beat structure for one compact idea or an evidence-chain structure for a multi-stage mechanism or journey.
4. Turn the meaning map into a visual proof and lock the logic before generating media.
5. Write frame contracts that define composition, paper construction, palette, continuity anchors, exclusions, and acceptance checks.
6. Generate and approve the required keyframes so identity, layout, and the start or end state remain controlled.
7. Choreograph every entrance, interaction, transition, sound cue, and settled state across the full duration.
8. Export the approved timeline through the requested model adapter, including MiniMax H3 when selected.
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
