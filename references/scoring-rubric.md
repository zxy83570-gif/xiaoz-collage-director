# A/B Scoring Rubric

Use this rubric to compare two workflows on the same input. Score finished media, not the elegance of the written plan.

## Controlled Test

Keep constant:

- narration or source text;
- target duration and aspect ratio;
- image and video model versions;
- generation settings and number of attempts;
- supplied assets;
- post-production allowance;
- evaluator instructions.

Randomize labels so evaluators do not know which workflow produced a result. Use at least two evaluators when possible.

## Categories

Score each item from 0 to 5.

| Category | Weight | A 5 means |
|---|---:|---|
| Meaning accuracy | 20 | The intended claim is immediately correct without captions. |
| Causal readability | 20 | Each state visibly causes or explains the next. |
| Visual hierarchy | 15 | Dense elements remain organized around one reading path. |
| Material credibility | 15 | The work behaves and looks like constructed printed paper. |
| Continuity | 10 | Identity and token anchors survive every transition. |
| Pace | 10 | Motion starts immediately, keeps adding information, and ends cleanly. |
| Technical compliance | 10 | Duration, framing, references, sound policy, and endpoint are correct. |

Convert the weighted result to 100 points.

## Critical Failures

Mark a run as failed regardless of total score when any of these occurs:

- the output communicates a materially different claim;
- a required keyframe or main subject is missing;
- the central token cannot be tracked across a causal sequence;
- fake text, a fake logo, or disallowed content dominates the frame;
- the prompt cannot be submitted because its adapter structure is invalid.

## Release Threshold

Compare ten paired cases. The candidate skill passes parity when:

- its mean total score is no more than 3 points below the baseline;
- it wins or ties on at least 7 of 10 cases;
- its average meaning accuracy and causal readability are each no more than 0.25 points below the baseline on the 0–5 scale;
- it has no additional critical failures;
- all structural validators pass.

If results miss the threshold, revise the smallest responsible module and rerun only the affected cases plus two regression cases.
