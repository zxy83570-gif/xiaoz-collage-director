#!/usr/bin/env python3
"""Validate structural invariants of supported collage-video prompt exports."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


BASIC_H3_FIELDS = (
    "integrated_multimodal_description",
    "overall_soundscape",
    "non_diegetic_music",
)

REF2VA_FIELDS = (
    "subject_definitions",
    "summary",
    "retention_analysis",
    "detailed_description",
    "overall_soundscape",
    "non_diegetic_music",
)

TASK_TYPES = (
    "keyframe completion",
    "reference generation",
    "video editing",
    "video continuation",
    "audio reuse",
    "audio reference",
)

RETENTION_MARKERS = {
    "fully_preserved",
    "partially_preserved",
    "attribute_transfer",
    "weak_reference",
    "fully_copy",
    "partially_copy",
    "reference",
}


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


def _section_text(text: str, field: str, fields: tuple[str, ...]) -> str:
    start = re.search(rf"(?m)^{re.escape(field)}\s*:\s*", text)
    if not start:
        return ""
    later = [
        match.start()
        for other in fields
        if other != field
        for match in [re.search(rf"(?m)^{re.escape(other)}\s*:", text[start.end() :])]
        if match
    ]
    end = start.end() + min(later) if later else len(text)
    return text[start.end() : end].strip()


def validate_h3(text: str, expected_duration: float | None = None) -> list[str]:
    errors: list[str] = []
    stripped = text.strip()
    if not stripped:
        return ["prompt is empty"]

    is_ref2va = bool(re.search(r"(?m)^subject_definitions\s*:", text))
    fields = REF2VA_FIELDS if is_ref2va else BASIC_H3_FIELDS
    _, field_errors = _field_positions(text, fields)
    errors.extend(field_errors)

    for field in fields:
        if not _section_text(text, field, fields):
            errors.append(f"field '{field}' has no content")

    if "[Shot 1]" not in text:
        errors.append("main or detailed description must include [Shot 1]")

    if re.search(r"(?i)\b(?:TODO|TBD|PLACEHOLDER)\b|\[insert[^\]]*\]", text):
        errors.append("prompt contains an unfinished placeholder")

    if is_ref2va:
        if re.search(r"(?m)^integrated_multimodal_description\s*:", text):
            errors.append("Ref2VA must use detailed_description, not integrated_multimodal_description")

        definitions = _section_text(text, "subject_definitions", fields)
        defined_labels = set(re.findall(r"<(?:Subject|Picture|Video|Audio)\s+\d+>", definitions))
        used_labels = set(re.findall(r"<(?:Subject|Picture|Video|Audio)\s+\d+>", text))
        if not defined_labels:
            errors.append("Ref2VA subject_definitions must define at least one reference label")
        undefined = sorted(used_labels - defined_labels)
        if undefined:
            errors.append(f"Ref2VA uses undefined reference labels: {', '.join(undefined)}")

        summary = _section_text(text, "summary", fields).lower()
        if summary and not any(summary.startswith(task) for task in TASK_TYPES):
            errors.append("Ref2VA summary must begin with an official task type")

        retention = _section_text(text, "retention_analysis", fields)
        found_markers = set(re.findall(r"\b[a-z_]+\b", retention)) & RETENTION_MARKERS
        if retention and not found_markers:
            errors.append("Ref2VA retention_analysis has no official retention marker")
        missing_retention = sorted(label for label in defined_labels if label not in retention)
        if missing_retention:
            errors.append(f"Ref2VA retention_analysis omits labels: {', '.join(missing_retention)}")

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
        if not 4 <= expected_duration <= 15:
            errors.append("H3 expected duration must be between 4 and 15 seconds")
        if any(value > expected_duration + 0.001 for value in times):
            errors.append("a shot time exceeds expected duration")
        shot_times = [
            int(minutes) * 60 + float(seconds)
            for minutes, seconds in re.findall(
                r"(?i)\[Shot\s+\d+\]\s+At\s+(\d{1,2}):(\d{2}(?:\.\d{1,3})?)",
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
