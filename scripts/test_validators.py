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


class H3ValidatorTests(unittest.TestCase):
    def test_valid_prompt(self) -> None:
        self.assertEqual(validate_h3(VALID, 5.0), [])

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


if __name__ == "__main__":
    unittest.main(verbosity=2)
