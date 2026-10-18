# Changelog

## Unreleased

- Add a fictional revoked-standing-consent case and checker regression: a current conversation-only instruction requires session-only retention despite an available backend. Clarify the policy and derive report counts from the case set. This expands evaluation coverage, not verified model behavior.

- Reject unpaired Unicode surrogates in decision reasons with the existing non-echoing diagnostic; valid Unicode reasons remain accepted. This checks representation, not reasoning quality.

- Require exactly action and reason in every model decision; reject unchecked extra fields, including conflicting claimed actions. Reasons still need human review.

- Reject duplicate case IDs and nested decision fields in external JSON reports rather than validating only their last values.

- Read external model reports with a 256 KiB ceiling before JSON parsing; oversized reports fail without echoing contents or paths.
- Add a subprocess regression using an otherwise valid oversized fictional report.

- Keep checker failure diagnostics generic instead of echoing input paths or exception details, including deeply nested JSON failures.
- Add subprocess regressions for missing, malformed, deeply nested and valid fictional reports, and run them in three-platform CI. These checks do not measure model behavior.

## 0.1.0 - 2026-10-07

- Initial goal-aware memory capture, recall, correction, and forgetting policy.
- Explicit scope, consent, contrary-evidence, and prompt-injection boundaries.
- Optional existing Agent Mem backend; no separate memory database.
- Bilingual documentation and fictional evaluation cases.
