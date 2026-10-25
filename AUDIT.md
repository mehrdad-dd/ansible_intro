# Review notes | یادداشت بازنگری

Review date: 2026-10-25

| Part | Issue | Resolution |
|---|---|---|
| Entry point | Focused only on Day 1 | Rebuilt as bilingual learning index |
| Day 1 | Verbose repeated playbook | Concise shared YAML and lab inventory |
| Day 2 | Mismatched formats and missing templates | Two aligned Markdown guides, template and working example |
| Day 3 | Risky default security changes | Safe reversible user exercise |
| Day 4 | Missing role dependencies and SSH key checking disabled | Minimal standalone role and host key checking enabled |
| Day 5 | Vault placeholders | Clear bilingual guide and ignore rules |

## Legacy cleanup
45 obsolete or incomplete files were excluded from this proposed branch: stale quick-start fragments, unusable role includes, a pseudo-production inventory, and placeholder Vault password files. They are recoverable from Git history.

## Safety and editorial guidelines
- Explain one concept with one short shared-code example and a quick verification command.
- Persian and English prose differ, while YAML and code comments are identical.
- No actual infrastructure credentials, private SSH keys, or Vault password files should be committed.
- Validate syntax and test on a disposable Debian/Ubuntu VM before production use.
- No remote playbook execution or CI verification was performed as part of this edit.
- Existing MIT license retained; preserve its required notices and check third-party rights.
