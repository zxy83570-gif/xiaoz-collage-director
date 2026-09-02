# Quality Control and Repair

Inspect concept, stills, prompts, and generated media separately. A later stage cannot reliably repair a broken earlier stage.

## Concept Check

Pass only when:

- the claim can be stated in one sentence;
- the first state, change engine, and final evidence agree with that claim;
- every major object has a narrative role;
- the sequence works without captions;
- a continuity token can be tracked through all adjacent states.

If this fails, revise the meaning map or architecture. Do not generate more detail.

## Still Check

Pass only when:

- the dominant subject reads at thumbnail size;
- paper construction is visibly physical;
- palette and light direction are consistent across frames;
- token anchors are present and identifiable;
- adjacent frames differ enough to express progress;
- no fake lettering, unwanted logos, duplicated subjects, or incompatible style appears.

If this fails, revise only the affected frame contract and regenerate that still.

## Prompt Check

Pass only when:

- duration, reference timing, and motion beats agree;
- references have explicit duties;
- changes and invariants are both stated;
- every action produces an observable result;
- the closing image is described as an exact terminal state;
- sound effects are synchronized and music policy is explicit;
- platform fields are complete and ordered correctly.

Use `scripts/validate_export.py` for supported structural checks.

## Media Check

Watch once muted, once with audio, and once at half speed.

Score:

- semantic legibility;
- continuity;
- visual hierarchy;
- paper-material credibility;
- pace and action density;
- reference fidelity;
- sound synchronization;
- ending accuracy.

## Failure Taxonomy

### Logic failure

Symptoms: attractive images but the claim is unclear; objects feel unrelated.

Repair: reduce roles, replace the metaphor, or rebuild the state ladder. Do not add arrows or labels as the first fix.

### Identity failure

Symptoms: tracked object changes color, count, shape, or motif without reason.

Repair: strengthen the token anchors in the affected frame contracts and prompt. Regenerate from the last correct state.

### Material failure

Symptoms: glossy CGI, vector-flat motion, liquid morphing, or invisible paper depth.

Repair: specify construction and contact mechanics; replace abstract motion verbs with paper actions.

### Density failure

Symptoms: too many simultaneous focal points, fragments move without a job, or the viewer cannot follow the main action.

Repair: group repeated elements, stagger entrances, and restore one dominant action per beat.

### Pace failure

Symptoms: empty opening, long holds, slow camera drift, or all changes happen at once.

Repair: move the first action to the opening 0.15 seconds, shorten inactive intervals, distribute semantic changes, and keep only a brief final lock.

### Endpoint failure

Symptoms: final composition is approximate, cropped, unstable, or arrives too late.

Repair: simplify the last transformation, begin convergence earlier, and reserve the final 0.2–0.5 seconds for exact settling.

### Audio failure

Symptoms: generic cinematic music dominates, effects are late, or separately generated voices drift.

Repair: remove unwanted music, attach each effect to contact, or replace segment voices with one post-production track.

## Retry Limit

After two attempts fail for the same reason, stop repeating the same prompt. Change the relevant concept, frame contract, segment boundary, or generation mode and explain the tradeoff.
