# Contributing | مشارکت در Ansible Intro

**فارسی:** هدف ما یادگیری سریع و عمیق است، نه افزودن متن بیشتر. **English:** Improve clarity and correctness, not word count.

## Before a PR | پیش از ارسال تغییر

1. One real problem per lesson; describe why it matters.
2. Keep both `README.md` (Persian) and `README_EN.md` (English) synchronized.
3. Never translate YAML, command flags, variable names, or source-code comments between languages.
4. Do not add real hostnames, public/private credentials, tokens, SSH keys, or copied proprietary examples.
5. Prefer built-in Ansible modules, FQCN, explicit file modes, and safely repeatable tasks.
6. Avoid sudo, SSH/firewall changes, external scripts, and side effects in CI examples.
7. Include one failing edge case or one small verification exercise where appropriate.

## Check locally | بررسی محلی

```bash
python3 tools/check_course.py
python3 tools/run_examples.py --syntax
python3 tools/run_examples.py --smoke
```

Install `ansible-core` to run the latter commands. Report the Ansible version when filing a bug.

## Attribution | حقوق نشر

Contribute only material you have the right to license under [MIT](LICENSE). Do not paste protected books, documentation, or code without proper permission and attribution. The MIT notice must remain with copies or substantial portions.

For security concerns, use the guidance in [SECURITY.md](SECURITY.md) rather than posting secrets publicly.
