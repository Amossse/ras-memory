# Changelog

## Unreleased

- Keep checker failure diagnostics generic instead of echoing input paths or exception details, including deeply nested JSON failures.
- Add subprocess regressions for missing, malformed, deeply nested and valid fictional reports, and run them in three-platform CI. These checks do not measure model behavior.

## 0.1.0 - 2026-10-07

- Initial goal-aware memory capture, recall, correction, and forgetting policy.
- Explicit scope, consent, contrary-evidence, and prompt-injection boundaries.
- Optional existing Agent Mem backend; no separate memory database.
- Bilingual documentation and fictional evaluation cases.
