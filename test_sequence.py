import unittest

import main
import sequence


class OpenShotSpecSequenceTest(unittest.TestCase):
    def test_invalid_schema_version_is_reported(self):
        issues = main.validate({
            "schema_version": 0,
            "shot_id": "S1",
            "duration": 2,
            "subject": {},
            "camera": {"shot_type": "medium"},
        })
        self.assertTrue(any(item["type"] == "invalid_version" for item in issues))

    def test_duplicate_ids_are_reported(self):
        records = [
            {"shot_id": "S1", "duration": 2, "subject": {}, "camera": {"shot_type": "wide"}},
            {"shot_id": "S1", "duration": 3, "subject": {}, "camera": {"shot_type": "close-up"}},
        ]
        issues = sequence.validate_sequence(records)
        self.assertTrue(any(item["type"] == "duplicate_id" for item in issues))

    def test_missing_reference_is_reported(self):
        records = [
            {
                "shot_id": "S1",
                "duration": 2,
                "subject": {},
                "camera": {"shot_type": "wide"},
                "continuity": {"next_id": "S2"},
            }
        ]
        issues = sequence.validate_sequence(records)
        self.assertTrue(any(item["type"] == "missing_reference" for item in issues))

    def test_valid_reciprocal_sequence(self):
        records = [
            {
                "shot_id": "S1",
                "duration": 2,
                "subject": {},
                "camera": {"shot_type": "wide"},
                "continuity": {"next_id": "S2"},
            },
            {
                "shot_id": "S2",
                "duration": 2,
                "subject": {},
                "camera": {"shot_type": "medium"},
                "continuity": {"previous_id": "S1"},
            },
        ]
        self.assertEqual(sequence.validate_sequence(records), [])


if __name__ == "__main__":
    unittest.main()
