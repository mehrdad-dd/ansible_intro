# Security policy | سیاست امنیتی

## Scope | محدوده

This is an educational Ansible repository, **not a hardening baseline or production deployment framework**.

این مخزن آموزشی است؛ اجرای مثال‌ها روی سیستم واقعی، بدون بررسی مستقل توصیه نمی‌شود.

- Use disposable virtual machines for lessons 1–4; those lessons can modify packages, services, users, and system paths.
- Days 6–20 use harmless localhost demonstrations and do not require root or real infrastructure.
- Never commit API tokens, passwords, private keys, Vault password files, real infrastructure inventory, or confidential logs.
- Use Ansible Vault for secrets at rest and approved secret stores for CI. `no_log` only suppresses task output: it does **not** encrypt secrets.
- Keep SSH host-key verification enabled. Limit CI token permissions to read-only, avoid privileged PR workflows, and review dependencies before upgrading.
- When a credential is exposed, revoke/rotate it immediately. Removing it from the latest commit does not remove it from Git history.
- If you discover a security issue, do **not** publish secret material in a public issue. Use GitHub private vulnerability reporting if enabled or a private channel offered by the maintainer.

## Reporting | گزارش‌دهی

Include a minimal reproducible example, affected lesson, Ansible version, and expected behavior—but redact secrets and personal information.

Maintainers should review contributions and workflow changes before merging.
