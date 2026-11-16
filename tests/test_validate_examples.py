import json
import sys
import unittest
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from validate_examples import validate_record, validate_file


class SyntheticSchemaTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = [json.loads(line) for line in (ROOT / 'examples/synthetic_examples.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]

    def test_all_examples_pass_shape_check(self):
        self.assertEqual(len(self.rows), 4)
        for row in self.rows:
            self.assertEqual(validate_record(row), [])

    def test_file_check(self):
        count, problems = validate_file(ROOT / 'examples/synthetic_examples.jsonl')
        self.assertEqual(count, 4)
        self.assertEqual(problems, [])

    def test_wrong_excerpt_fails(self):
        row = deepcopy(self.rows[0])
        row['evidence_spans'][0]['text'] = 'not in the original passage'
        self.assertTrue(any('mismatches' in e for e in validate_record(row)))

    def test_inappropriate_action_fails(self):
        row = deepcopy(self.rows[1])
        row['recommended_action'] = 'answer'
        self.assertTrue(any('requires action=abstain' in e for e in validate_record(row)))

    def test_non_synthetic_origin_fails(self):
        row = deepcopy(self.rows[0])
        row['origin'] = 'human_subjects'
        self.assertTrue(any('synthetic_constructed' in e for e in validate_record(row)))


if __name__ == '__main__':
    unittest.main()
