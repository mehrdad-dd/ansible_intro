# Review notes | یادداشت بازنگری

**Review date:** 2026-10-25

| Area | Finding | Current handling |
|---|---|---|
| Root README | Previously described only Day 1 | Replaced with bilingual learning index |
| Day 1 | Repeated, lengthy embedded source | Shortened and synchronized with a shared playbook |
| Day 2 | English file was raw YAML while Persian was Markdown | Both now Markdown, with one shared runnable playbook |
| Day 2 | Original relied on missing Jinja2 templates | Added local template, inventory, and bounded lab example |
| Day 3 | Default workflow changed SSH, sudo, firewall, and accounts | Replaced with a reversible training user example |
| Day 4 | Original included missing role dependencies and file references | Replaced active entrypoint with one minimal Nginx role |
| Day 4 | Host-key checking disabled in ansible.cfg | Enabled host-key checking in active configuration |
| Day 5 | Vault guidance incomplete; tracked placeholder files existed | Added bilingual guide and ignore rules for secret files |
| License | MIT license present | Retained unchanged |

## Remaining considerations

- Older deep-dive notes under `3rd_day/Quick_Start` and `4th_day/Quick Start` and legacy role fragments remain in Git history/current tree. They are **historical, not validated exercises**.
- `4th_day/ansible-roles-demo/inventory/production/hosts.yml` is a **legacy example**. Do not deploy against it.
- The `5th_day/ansible-vault-demo` directory contains placeholder files only; use the new Vault lessons.
- No external server or CI environment was used to execute Ansible tasks; run syntax checks and test on a disposable VM before adopting any example.
- GitHub MIT licensing grants broad reuse but still requires preserving its notice and having permission to include third-party content.

## Editorial rules | اصول نگارش

- One concrete objective, one shared code example, minimal explanation per lesson.
- Persian and English prose can differ, but shared code, commands, identifiers, and comments must match.
- Use documentation-only IPs and domains for examples; never publish credentials or private infrastructure details.
- Keep destructive security operations out of default beginner paths.
