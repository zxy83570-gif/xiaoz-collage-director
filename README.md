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
