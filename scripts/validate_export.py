#!/usr/bin/env python3
"""Validate structural invariants of supported collage-video prompt exports."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


H3_FIELDS = (
    "integrated_multimodal_description",
    "overall_soundscape",
    "non_diegetic_music",
)


def _field_positions(text: str, fields: tuple[str, ...]) -> tuple[list[int], list[str]]:
    positions: list[int] = []
    errors: list[str] = []
    for field in fields:
        matches = list(re.finditer(rf"(?m)^{re.escape(field)}\s*:", text))
        if len(matches) != 1:
            errors.append(f"field '{field}' must appear exactly once; found {len(matches)}")
        else:
            positions.append(matches[0].start())
    if len(positions) == len(fields) and positions != sorted(positions):
        errors.append("fields are not in the required order")
    return positions, errors


def _time_values(text: str) -> list[float]:
    values: list[float] = []
    for minutes, seconds in re.findall(r"\b(\d{1,2}):(\d{2}(?:\.\d{1,3})?)\b", text):
        values.append(int(minutes) * 60 + float(seconds))
    return values


def validate_h3(text: str, expected_duration: float | None = None) -> list[str]:
    errors: list[str] = []
    stripped = text.strip()
    if not stripped:
        return ["prompt is empty"]

    _, field_errors = _field_positions(text, H3_FIELDS)
    errors.extend(field_errors)

    for field in H3_FIELDS:
        match = re.search(rf"(?m)^{re.escape(field)}\s*:\s*(.*)$", text)
        if match and not match.group(1).strip():
            errors.append(f"field '{field}' has no inline content")

    if "[Shot 1]" not in text:
        errors.append("main description must include [Shot 1]")

    if re.search(r"(?i)\b(?:TODO|TBD|PLACEHOLDER)\b|\[insert[^\]]*\]", text):
        errors.append("prompt contains an unfinished placeholder")

    picture_lines = re.findall(
        r"(?mi)^Picture\s+(\d+)\s+is\s+the\s+(opening|closing)\s+image\s+at\s+(\d+(?:\.\d+)?)\s+seconds?\.\s*$",
        text,
    )
    if "Reference timing:" in text:
        block = re.search(
            r"(?ms)^Reference timing:\s*\n(.*?)\n\s*\nintegrated_multimodal_description\s*:",
            text,
        )
        if not block:
            errors.append("Reference timing block must directly precede the main field")
        else:
            mapping_pattern = re.compile(
                r"Picture\s+\d+\s+is\s+the\s+(?:opening|closing)\s+image\s+at\s+\d+(?:\.\d+)?\s+seconds?\."
            )
            invalid_lines = [
                line.strip()
                for line in block.group(1).splitlines()
                if line.strip() and not mapping_pattern.fullmatch(line.strip())
            ]
            if invalid_lines:
                errors.append("Reference timing block contains an invalid picture mapping")
        if not picture_lines:
            errors.append("Reference timing block has no valid picture mapping")
        numbers = [int(number) for number, _, _ in picture_lines]
        if len(numbers) != len(set(numbers)):
            errors.append("picture numbers must be unique")
        roles = [role.lower() for _, role, _ in picture_lines]
        if roles.count("opening") > 1 or roles.count("closing") > 1:
            errors.append("reference timing may define at most one opening and one closing image")

    if picture_lines:
        opening_times = [float(time) for _, role, time in picture_lines if role.lower() == "opening"]
        if opening_times and any(abs(value) > 0.001 for value in opening_times):
            errors.append("opening image must be mapped to 0.00 seconds")
        if expected_duration is not None:
            closing_times = [float(time) for _, role, time in picture_lines if role.lower() == "closing"]
            if closing_times and any(abs(value - expected_duration) > 0.001 for value in closing_times):
                errors.append("closing image time does not match expected duration")

    times = _time_values(text)
    if expected_duration is not None:
        if expected_duration <= 0:
            errors.append("expected duration must be positive")
        if any(value > expected_duration + 0.001 for value in times):
            errors.append("a shot time exceeds expected duration")
        shot_times = [
            int(minutes) * 60 + float(seconds)
            for minutes, seconds in re.findall(
                r"(?mi)^\[Shot\s+\d+\]\s+At\s+(\d{1,2}):(\d{2}(?:\.\d{1,3})?)",
                text,
            )
        ]
        if shot_times != sorted(set(shot_times)):
            errors.append("later shot times must be unique and strictly increasing")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--adapter", choices=("h3",), default="h3")
    parser.add_argument("--duration", type=float)
    args = parser.parse_args()

    if not args.path.is_file():
        print(f"ERROR: file not found: {args.path}", file=sys.stderr)
        return 2

    text = args.path.read_text(encoding="utf-8")
    errors = validate_h3(text, args.duration)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"OK: {args.adapter} export is structurally valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
