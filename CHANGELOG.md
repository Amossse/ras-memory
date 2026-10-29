# Changelog

## Unreleased

- Cover the exact 256 KiB report boundary with multibyte UTF-8 and valid JSON whitespace; reject one extra byte without modifying or echoing source details. Runtime and the decision catalog are unchanged.

- Cover strict external-report UTF-8 decoding through the CLI, including valid Unicode, UTF-16/32 rejection and malformed bytes. Preserve source bytes and non-echoing diagnostics; runtime and the 15-case catalog are unchanged.

- Add an actual read-I/O fault-injection regression for the checker CLI entry point. Confirm its stream and descriptor close, source bytes remain unchanged, and the controlled error omits source paths and raw exception details. Runtime and the 15-case decision catalog are unchanged; no model behavior is tested.

- Add a fictional quoted-approval case: a sample preference and approval inside reviewed source material must stay session-only, not authorize persistent capture. Clarify consent provenance and cover the action label. This fills a policy evaluation gap, not fresh model or backend validation.

- Distinguish accepted/queued or timed-out writes from confirmed persistence. Add a fictional accepted-but-unreadable case and `report-unconfirmed` checker branch: inspect the exact target before retrying rather than claiming success/failure or blindly repeating a mutation. No fresh model or backend behavior is verified.

- Add a fictional factual-freshness case: a newer unsupported snippet cannot replace a sourced external fact solely on timestamp; verification is required first. Cover the expected action label in the checker. This fills an existing policy-branch evaluation gap, not fresh model or backend validation.

- Validate each fictional case's exact fields and nonempty UTF-8 prompt before checker self-tests; reject duplicate catalog JSON fields as well as duplicate/missing IDs. Cover a missing-prompt catalog that previously passed. This validates evaluation inputs, not model behavior.

- Add a fictional budget-limited recall case for disclosing an omitted relevant conflict, plus a checker regression rejecting silent recall/skip decisions. This fills an existing policy-branch evaluation gap; action-label checks do not measure fresh model decisions, reason quality or actual response-budget compliance.

- Close report descriptors on rejected directories and stream-wrapper failures as well as successful reads. Check file type before constructing the stream, retain nonblocking FIFO rejection and byte limits, and add descriptor-lifetime regressions. No model behavior is measured.

- Require external decision reports to be regular files, checking the opened descriptor before reading. POSIX nonblocking open prevents a FIFO from waiting for a writer; retain the byte ceiling and non-echoing failure diagnostic. No model behavior is measured.

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
