import unittest
import main


class FormatTest(unittest.TestCase):
    def test_valid_record(self):
        record = {"shot_id": "S1", "duration": 2, "subject": {}, "camera": {"shot_type": "medium"}}
        self.assertEqual(main.validate(record), [])


if __name__ == "__main__":
    unittest.main()
