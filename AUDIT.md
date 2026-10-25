# Curriculum audit | گزارش بازنگری

## Scope | محدوده

This repository is a 20-lesson bilingual Ansible learning track. Each lesson aims for a concise explanation, a runnable example, a quick experiment, and a common pitfall.

این مخزن یک مسیر آموزشی ۲۰ درسی است: هر درس مسئله، یک نکته مفهومی، مثال اجرایی کوتاه و یک تمرین دارد.

## Quality rules | قواعد کیفیت

- Days 1–4 modify operating system state and are **not** executed on GitHub Actions runners.
- Days 5–20 focus on non-privileged localhost concepts; smoke tests run days 6–20 automatically.
- Both languages must embed identical YAML and commands.
- The current CI checks syntax and selected idempotence, not production suitability.
- No actual infrastructure credentials or third-party copyrighted samples belong in the repository.
- GitHub repository About description/topics are proposed in [Discovery guidance](docs/GITHUB_DISCOVERY.md) and may require manual configuration.

## Limits | محدودیت‌ها

Automated tests do not prove complete security, universal OS support, or behavior under real production workloads. Review the code, lock dependencies where required, and use isolated lab environments.
