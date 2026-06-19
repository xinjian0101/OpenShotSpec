import copy
import unittest

import migrate


class OpenShotMigrationTest(unittest.TestCase):
    def test_legacy_fields_are_migrated(self):
        source = {
            "shot_id": "S1",
            "duration": 3,
            "subject": {},
            "camera": {"type": "wide"},
            "scene_description": "A corridor",
            "lighting_description": "Cool practical light",
            "continuity": {"locked_attributes": ["subject.id", "subject.id"]},
        }
        original = copy.deepcopy(source)
        migrated, changes = migrate.migrate_record(source)
        self.assertEqual(source, original)
        self.assertEqual(migrated["schema_version"], 1)
        self.assertEqual(migrated["camera"]["shot_type"], "wide")
        self.assertEqual(migrated["scene"]["description"], "A corridor")
        self.assertEqual(migrated["lighting"]["description"], "Cool practical light")
        self.assertEqual(migrated["continuity"]["locked_attributes"], ["subject.id"])
        self.assertGreaterEqual(len(changes), 5)

    def test_existing_shared_fields_are_not_overwritten(self):
        source = {
            "schema_version": 1,
            "shot_id": "S1",
            "duration": 3,
            "subject": {},
            "camera": {"shot_type": "medium", "type": "legacy"},
            "scene": {"description": "Current"},
            "scene_description": "Legacy",
        }
        migrated, _ = migrate.migrate_record(source)
        self.assertEqual(migrated["camera"]["shot_type"], "medium")
        self.assertEqual(migrated["scene"]["description"], "Current")
        self.assertIn("scene_description", migrated)

    def test_array_migration_tracks_record_indexes(self):
        records = [
            {"shot_id": "S1", "duration": 1, "subject": {}, "camera": {"type": "wide"}},
            {"shot_id": "S2", "duration": 1, "subject": {}, "camera": {"type": "close-up"}},
        ]
        migrated, changes = migrate.migrate_document(records)
        self.assertEqual(len(migrated), 2)
        self.assertEqual({item["record"] for item in changes}, {0, 1})

    def test_unsupported_source_version_is_rejected(self):
        with self.assertRaises(ValueError):
            migrate.migrate_record({"schema_version": 99})

    def test_non_object_record_is_rejected(self):
        with self.assertRaises(ValueError):
            migrate.migrate_record("invalid")


if __name__ == "__main__":
    unittest.main()
