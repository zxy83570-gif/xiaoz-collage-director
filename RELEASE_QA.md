# Release QA

Version: `0.3.0`
Review date: 2026-09-03

## Completed Checks

- Skill frontmatter and structure pass the bundled skill validator.
- All Python scripts compile.
- H3 basic and Ref2VA exports pass field, order, reference-time, label, retention, task-type, placeholder, and 4–15 second duration checks.
- Fifteen validator regressions cover valid basic and Ref2VA prompts, missing and duplicate fields, fixed field order, official task types, retention coverage, opening and closing reference times, malformed reference mappings, out-of-range shot time and duration, unfinished placeholders, and empty input.
- Package preflight confirms required files, MIT license, ten unique benchmark cases, supported file types, and absence of machine-specific paths.
- The release archive has no absolute or parent-traversal paths, reproduces the same SHA-256 digest on consecutive builds, verifies against its checksum file, and passes all checks after extraction into a fresh temporary directory.

## Bugs Found and Fixed

1. Python bytecode caches could have caused a false binary-file failure on a second preflight run. Cache files are now ignored by inspection and excluded from releases.
2. Git metadata could have caused a false unknown-file failure after cloning. The `.git` directory is now ignored by inspection and excluded from releases.
3. The earlier H3 adapter validated only the basic three-field format and deferred multi-reference structure to the interface. It now encodes and validates the official six-section Ref2VA structure.
4. The intermediate v0.2 logic incorrectly preferred a single final frame and L2VA. The workflow now matches the approved official example: F0–Fn continuous keyframes and one full 5-second FL2VA prompt per adjacent pair.

## Limits of This QA

These checks establish structural integrity but do not establish visual-quality parity. Media performance must be tested with the included ten-case blind A/B protocol.
