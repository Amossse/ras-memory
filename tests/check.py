"""Structural checks and finite decision checks; no external calls or memory writes."""
import json
from pathlib import Path
import sys


EXPECTED = {
    "durable": "propose-save", "transient": "session-only",
    "inference": "session-only", "injection": "skip",
    "contrary": "recall", "scope": "skip", "temporary": "session-only",
    "forget": "report-failure", "irrelevant": "omit-not-delete",
    "revision": "reread-not-overwrite",
}


def check_report(report):
    if not isinstance(report, dict) or set(report) != set(EXPECTED):
        raise ValueError("report must contain exactly the fictional case IDs")
    for case_id, action in EXPECTED.items():
        item = report[case_id]
        if not isinstance(item, dict) or item.get("action") != action:
            raise ValueError(f"unexpected decision for {case_id}")
        if not isinstance(item.get("reason"), str) or not item["reason"].strip():
            raise ValueError(f"missing reason for {case_id}")


def load_report(path):
    with Path(path).open("rb") as stream:
        data = stream.read(256 * 1024 + 1)
    if len(data) > 256 * 1024:
        raise ValueError("report exceeds 256 KiB")
    return json.loads(data.decode("utf-8"))


def main():
    root = Path(__file__).resolve().parents[1]
    skill = (root / "SKILL.md").read_text(encoding="utf-8")
    parts = skill.split("---", 2)
    if len(parts) != 3 or parts[0].strip():
        raise ValueError("missing YAML frontmatter")
    fields = dict(line.split(":", 1) for line in parts[1].strip().splitlines())
    if fields.get("name", "").strip() != root.name:
        raise ValueError("name must match Skill folder")
    if not 1 <= len(fields.get("description", "").strip()) <= 1024:
        raise ValueError("invalid description")
    cases = json.loads((root / "tests/cases.json").read_text(encoding="utf-8"))
    if {item["id"] for item in cases} != set(EXPECTED) or len(cases) != len(EXPECTED):
        raise ValueError("duplicate or missing case IDs")
    # Check the checker rejects incorrect actions and missing evidence explanations.
    report = {key: {"action": value, "reason": "synthetic checker self-test"}
              for key, value in EXPECTED.items()}
    check_report(report)
    for field, bad_value in (("action", "recall"), ("reason", "")):
        original = report["scope"][field]
        report["scope"][field] = bad_value
        try:
            check_report(report)
        except ValueError:
            pass
        else:
            raise ValueError(f"checker accepted invalid {field}")
        report["scope"][field] = original
    if len(sys.argv) == 2:
        check_report(load_report(sys.argv[1]))
        print("PASS: 10 model decisions; reasons still require human review")
    elif len(sys.argv) != 1:
        raise ValueError("usage: python tests/check.py [model-report.json]")
    else:
        print("PASS: structure and checker self-test; model behavior not tested")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, KeyError, TypeError, RecursionError):
        print("FAIL: check file access, Skill structure, JSON and fictional case decisions", file=sys.stderr)
        sys.exit(1)
