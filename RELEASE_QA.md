# Release QA

Version: `0.1.0`  
Review date: 2026-09-02

## Completed Checks

- Skill frontmatter and structure pass the bundled skill validator.
- All Python scripts compile.
- H3-compatible example export passes field, order, reference-time, placeholder, and duration checks.
- Ten validator regressions cover a valid prompt, missing and duplicate fields, field order, opening and closing reference times, malformed reference mappings, out-of-range shot time, unfinished placeholders, and empty input.
- Package preflight confirms required files, MIT license, ten unique benchmark cases, supported file types, and absence of machine-specific paths.
- The release archive has no absolute or parent-traversal paths, reproduces the same SHA-256 digest on consecutive builds, verifies against its checksum file, and passes all checks after extraction into a fresh temporary directory.

## Bugs Found and Fixed

1. Python bytecode caches could have caused a false binary-file failure on a second preflight run. Cache files are now ignored by inspection and excluded from releases.
2. Git metadata could have caused a false unknown-file failure after cloning. The `.git` directory is now ignored by inspection and excluded from releases.

## Limits of This QA

These checks establish structural integrity but do not establish visual-quality parity. Media performance must be tested with the included ten-case blind A/B protocol.
