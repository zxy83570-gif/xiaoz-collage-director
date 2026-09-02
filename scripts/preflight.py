#!/usr/bin/env python3
"""Run deterministic release checks for the skill package."""

from __future__ import annotations

import json
import py_compile
import re
import sys
from pathlib import Path


REQUIRED = (
    "SKILL.md",
    "README.md",
    "LICENSE",
    "RELEASE_QA.md",
    "VERSION",
    "agents/openai.yaml",
    "references/brief-to-scene.md",
    "references/visual-language.md",
    "references/keyframe-and-motion.md",
    "references/model-export.md",
    "references/quality-control.md",
    "references/scoring-rubric.md",
    "benchmarks/README.md",
    "benchmarks/cases.json",
    "benchmarks/scorecard.csv",
    "examples/coffee-route-h3.txt",
    "scripts/build_release.py",
    "scripts/validate_export.py",
    "scripts/test_validators.py",
)

TEXT_SUFFIXES = {".md", ".txt", ".py", ".yaml", ".yml", ".json", ".csv"}
FORBIDDEN_NAMES = {"NOTICE"}
MACHINE_PATH_MARKERS = ("/" + "Users/", "/var/" + "folders/")


def fail(message: str) -> None:
    raise ValueError(message)


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    try:
        for relative in REQUIRED:
            if not (root / relative).is_file():
                fail(f"missing required file: {relative}")

        if not (root / "LICENSE").read_text(encoding="utf-8").startswith("MIT License"):
            fail("LICENSE is not MIT")

        files = [
            path
            for path in root.rglob("*")
            if path.is_file()
            and ".git" not in path.parts
            and "__pycache__" not in path.parts
            and path.suffix != ".pyc"
        ]
        for path in files:
            relative = path.relative_to(root)
            if path.is_symlink():
                fail(f"symlink is not allowed: {relative}")
            if path.name in FORBIDDEN_NAMES:
                fail(f"unexpected licensing artifact: {relative}")
            if "snapshot" in path.name.lower():
                fail(f"source snapshot is not allowed: {relative}")
            if path.suffix.lower() not in TEXT_SUFFIXES and path.name not in {"LICENSE", "VERSION"}:
                fail(f"unexpected binary or unknown file type: {relative}")
            if path.suffix.lower() in TEXT_SUFFIXES or path.name in {"LICENSE", "VERSION"}:
                text = path.read_text(encoding="utf-8")
                if re.search(r"(?m)^\s*\[TODO:[^\]]*\]\s*$", text):
                    fail(f"unfinished scaffold placeholder: {relative}")
                if any(marker in text for marker in MACHINE_PATH_MARKERS):
                    fail(f"machine-specific absolute path detected: {relative}")

        cases = json.loads((root / "benchmarks/cases.json").read_text(encoding="utf-8"))
        if not isinstance(cases, list) or len(cases) != 10:
            fail("benchmark suite must contain exactly 10 cases")
        identifiers = [case.get("id") for case in cases]
        if any(not identifier for identifier in identifiers) or len(identifiers) != len(set(identifiers)):
            fail("benchmark case ids must be present and unique")
        required_case_keys = {"id", "category", "input", "duration_seconds", "expected", "critical_failures"}
        for case in cases:
            missing = required_case_keys - set(case)
            if missing:
                fail(f"benchmark {case.get('id')} missing keys: {sorted(missing)}")

        for script in (root / "scripts").glob("*.py"):
            py_compile.compile(str(script), doraise=True)

    except (OSError, ValueError, json.JSONDecodeError, py_compile.PyCompileError) as exc:
        print(f"ERROR: {exc}")
        return 1

    print(f"OK: preflight passed for {root.name} ({len(files)} files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
