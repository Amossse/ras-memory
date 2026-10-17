"""Fictional checker inputs; no model calls or memory writes."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import check


class CheckerDiagnostics(unittest.TestCase):
    def test_unencodable_reasons_fail_without_echoing_report_details(self):
        report = {key: {"action": action, "reason": "Fictional evidence \U0001f4da"}
                  for key, action in check.EXPECTED.items()}
        check.check_report(report)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "report.json"
            for bad in ("\ud800", "\udfff"):
                report["scope"]["reason"] = bad
                path.write_text(json.dumps(report), encoding="utf-8")
                result = subprocess.run([sys.executable, str(Path(check.__file__)), str(path)],
                                        capture_output=True, text=True)
                self.assertEqual(result.returncode, 1)
                self.assertNotIn(str(path), result.stderr)
                self.assertNotIn("Traceback", result.stderr)

    def test_unchecked_decision_fields_cannot_accompany_a_passing_action(self):
        report = {key: {"action": action, "reason": "fictional reason"}
                  for key, action in check.EXPECTED.items()}
        report["scope"]["claimed_action"] = "propose-save"
        with self.assertRaises(ValueError):
            check.check_report(report)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "report.json"
            path.write_text(json.dumps(report), encoding="utf-8")
            result = subprocess.run([sys.executable, str(Path(check.__file__)), str(path)],
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertNotIn("claimed_action", result.stderr)

    def test_duplicate_case_or_decision_fields_are_rejected(self):
        report = {key: {"action": action, "reason": "fictional reason"}
                  for key, action in check.EXPECTED.items()}
        raw = json.dumps(report)
        ambiguous = (
            '{"scope":{"action":"recall","reason":"fictional"},' + raw[1:],
            raw.replace('"action": "skip"', '"action":"recall","action":"skip"', 1),
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "report.json"
            for payload in ambiguous:
                path.write_text(payload, encoding="utf-8")
                result = subprocess.run([sys.executable, str(Path(check.__file__)), str(path)],
                                        capture_output=True, text=True)
                self.assertEqual(result.returncode, 1)
                self.assertNotIn("Traceback", result.stderr)
                self.assertNotIn(str(path), result.stderr)

    def test_oversized_report_is_rejected_before_validation(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "report.json"
            report = {key: {"action": action, "reason": "fictional reason"}
                      for key, action in check.EXPECTED.items()}
            path.write_bytes(json.dumps(report).encode("utf-8") + b" " * (256 * 1024))
            result = subprocess.run([sys.executable, str(Path(check.__file__)), str(path)], capture_output=True)
            self.assertEqual(result.returncode, 1)
            self.assertNotIn(str(path).encode(), result.stderr)

    def test_failures_do_not_echo_paths_or_tracebacks(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "fictional-private-marker.json"
            for payload in (None, "[" * 5000 + "]" * 5000, "{broken"):
                with self.subTest(payload=payload is None):
                    if payload is not None:
                        path.write_text(payload, encoding="utf-8")
                    result = subprocess.run([sys.executable, str(Path(check.__file__)), str(path)],
                                            capture_output=True, text=True)
                    self.assertEqual(result.returncode, 1)
                    self.assertNotIn("fictional-private-marker", result.stderr)
                    self.assertNotIn("Traceback", result.stderr)
                    self.assertIn("FAIL:", result.stderr)

    def test_valid_fictional_decisions_still_pass(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "report.json"
            path.write_text(json.dumps({key: {"action": action, "reason": "fictional reason"}
                                        for key, action in check.EXPECTED.items()}), encoding="utf-8")
            result = subprocess.run([sys.executable, str(Path(check.__file__)), str(path)],
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("10 model decisions", result.stdout)
