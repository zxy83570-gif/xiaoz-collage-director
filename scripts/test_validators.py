#!/usr/bin/env python3
"""Regression tests for export validation."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from validate_export import validate_h3


VALID = """Reference timing:
Picture 1 is the opening image at 0.00 seconds.
Picture 2 is the closing image at 5.00 seconds.

integrated_multimodal_description: [Shot 1] A red paper token slides through a cut slot and locks into the closing composition with synchronized paper contact.

overall_soundscape: Dry paper scrapes and one precise card click.

non_diegetic_music: N/A
"""

VALID_REF2VA = """subject_definitions:
<Subject 1>: The red paper token from the supplied image.
<Picture 1>: The approved closing composition at 4.00 seconds.
summary:
keyframe completion and reference generation. Build a paper-collage assembly into the approved ending.
retention_analysis:
<Subject 1>: fully_preserved in Shot 1; retain its red color and punched corner.
<Picture 1>: fully_preserved as the closing composition; only the inferred preceding state changes.
detailed_description:
Premium editorial paper collage with tactile stop-motion construction and shallow physical shadows. [Shot 1] <Subject 1> slides across a matching paper field, rebounds slightly, and presses flat as surrounding pieces assemble. The arrangement converges precisely to <Picture 1> at 4.00 seconds.
overall_soundscape:
Dry paper slides, soft taps, and one crisp final press.
non_diegetic_music:
N/A
"""


class H3ValidatorTests(unittest.TestCase):
    def test_valid_prompt(self) -> None:
        self.assertEqual(validate_h3(VALID, 5.0), [])

    def test_valid_ref2va_prompt(self) -> None:
        self.assertEqual(validate_h3(VALID_REF2VA, 4.0), [])

    def test_ref2va_fixed_field_order(self) -> None:
        invalid = VALID_REF2VA.replace(
            "summary:\nkeyframe completion and reference generation. Build a paper-collage assembly into the approved ending.\nretention_analysis:",
            "retention_analysis:\n<Subject 1>: fully_preserved.\n<Picture 1>: fully_preserved.\nsummary:",
        )
        errors = validate_h3(invalid, 4.0)
        self.assertTrue(any("required order" in error for error in errors))

    def test_ref2va_requires_task_type(self) -> None:
        invalid = VALID_REF2VA.replace("keyframe completion and reference generation.", "Make a collage.")
        errors = validate_h3(invalid, 4.0)
        self.assertTrue(any("official task type" in error for error in errors))

    def test_ref2va_requires_retention_for_each_label(self) -> None:
        invalid = VALID_REF2VA.replace(
            "<Picture 1>: fully_preserved as the closing composition; only the inferred preceding state changes.\n",
            "",
        )
        errors = validate_h3(invalid, 4.0)
        self.assertTrue(any("omits labels" in error for error in errors))

    def test_missing_field(self) -> None:
        errors = validate_h3(VALID.replace("overall_soundscape:", "soundscape:"), 5.0)
        self.assertTrue(any("overall_soundscape" in error for error in errors))

    def test_duplicate_field(self) -> None:
        errors = validate_h3(VALID + "\nnon_diegetic_music: N/A\n", 5.0)
        self.assertTrue(any("exactly once" in error for error in errors))

    def test_wrong_closing_time(self) -> None:
        errors = validate_h3(VALID.replace("closing image at 5.00", "closing image at 4.00"), 5.0)
        self.assertTrue(any("closing image time" in error for error in errors))

    def test_wrong_opening_time(self) -> None:
        errors = validate_h3(VALID.replace("opening image at 0.00", "opening image at 1.00"), 5.0)
        self.assertTrue(any("opening image" in error for error in errors))

    def test_wrong_field_order(self) -> None:
        reordered = VALID.replace(
            "overall_soundscape: Dry paper scrapes and one precise card click.\n\nnon_diegetic_music: N/A",
            "non_diegetic_music: N/A\n\noverall_soundscape: Dry paper scrapes and one precise card click.",
        )
        errors = validate_h3(reordered, 5.0)
        self.assertTrue(any("required order" in error for error in errors))

    def test_invalid_reference_block(self) -> None:
        errors = validate_h3(VALID.replace("Picture 1 is the opening image", "Image A opens"), 5.0)
        self.assertTrue(any("picture mapping" in error for error in errors))

    def test_shot_time_exceeds_duration(self) -> None:
        prompt = VALID.replace(
            "[Shot 1] A red paper token",
            "[Shot 1] A red paper token [Shot 2] At 00:06.000, it settles;",
        )
        errors = validate_h3(prompt, 5.0)
        self.assertTrue(any("exceeds expected duration" in error for error in errors))

    def test_placeholder(self) -> None:
        errors = validate_h3(VALID.replace("A red paper token", "TODO A red paper token"), 5.0)
        self.assertTrue(any("placeholder" in error for error in errors))

    def test_empty_prompt(self) -> None:
        self.assertEqual(validate_h3("", 5.0), ["prompt is empty"])

    def test_duration_outside_h3_range(self) -> None:
        errors = validate_h3(VALID, 3.0)
        self.assertTrue(any("between 4 and 15" in error for error in errors))


if __name__ == "__main__":
    unittest.main(verbosity=2)
