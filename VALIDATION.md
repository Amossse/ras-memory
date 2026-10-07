# Validation record

Date: 2026-10-07. All evaluation inputs were fictional. No real memory store, transcript, account data, or internal asset was used or published. Raw host logs are not distributed.

- `python3 tests/check.py`: passed structural checks and checker negative self-tests. These are not model behavior tests.
- Official Skill Creator `quick_validate.py`: passed. Its optional YAML dependency was supplied only in the validation environment; the Skill has no runtime dependencies.
- Fresh Codex CLI session: read the Skill and the ten fictional cases, without reading checker expectations; all ten decisions matched the acceptance labels. Explanations were reviewed for scope, inference, contrary evidence, backend failure, and revision conflicts. This was explicit loading, not automatic discovery. Only one model/session was evaluated; there is no general accuracy claim.
- Backend failure probe: a symlink-containing database path was rejected by Agent Mem. The model reported the block without attempting mutations or claiming success. A physical database path is required for recovery; backend validation was not disabled.
- Live synthetic integration: a fresh Codex CLI session explicitly loaded RAS Memory and Agent Mem's card schema, then used an isolated, approved fictional cooking scope. It saved only a metric-units preference (revision 1), recalled and read it, corrected it to cups (revision 2), and forgot that exact record with revision checks. Read-back showed the record unavailable, empty search, and zero active records. Weather was not saved. The active-store workflow passed; backups, automatic discovery, other hosts, and real personal data were not tested.
- Gitleaks directory scan and internal-marker/local-path review: no findings in the publication files. Static inspection is not proof that all future user inputs are safe.
- Chinese document review: numeric limits, commands, technical terms, and claim boundaries preserved. Half-width Chinese punctuation, em-dash, and empty meta-phrase scan: zero findings in the Chinese README and launch draft. No structural rewrite or new efficacy claim added.

Not established: automatic loading on every host, production prompt-injection resistance, clinical effects, privacy guarantees, or measured improvements over another memory system. CI runs structural checks only; live model calls are deliberately excluded from CI.
