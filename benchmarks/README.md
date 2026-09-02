# Ten-Case A/B Test

This suite compares the candidate skill with a baseline workflow. It is not a prompt-writing contest; judge the generated stills and videos.

## Procedure

1. Run every case once through each workflow without showing either workflow the other's answer.
2. Keep model version, aspect ratio, duration, reference assets, generation settings, retry count, and post-production allowance identical.
3. Permit the same number of still and video generations for both workflows. Recommended limit: two attempts per required still and two attempts per video segment.
4. Rename outputs with random identifiers before evaluation.
5. Score both outputs using `references/scoring-rubric.md` and record critical failures.
6. Enter results in `scorecard.csv`. Do not average away a critical failure.

## What to Save

- original input;
- selected architecture;
- meaning map or equivalent plan;
- frame contracts and generated keyframes;
- final model prompts;
- raw generated clips;
- retry reason and changed instruction;
- blind scores and evaluator notes.

## Pass Decision

Use the release threshold in `references/scoring-rubric.md`. A structural validator pass is mandatory but does not count as evidence of visual parity.
