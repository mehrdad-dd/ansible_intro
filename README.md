# Ansible Tutorial bilingual - English & Persian
# آموزش انسیبل 0 تا 100 - دوزبانه، فارسی و انگلیسی
**Learn Ansible deeply, without fluff. آموزش مفهومی، کوتاه و کاربردی Ansible با مثال‌های قابل اجرا.**

[![Ansible](https://img.shields.io/badge/Ansible-Playbooks-EE0000?logo=ansible&logoColor=white)](https://docs.ansible.com/)
[![Language](https://img.shields.io/badge/Languages-فارسی%20%7C%20English-0069B5)](README.md)
[![CI](https://github.com/mehrdad-dd/ansible_intro/actions/workflows/ci.yml/badge.svg)](.github/workflows/ci.yml)
[![MIT](https://img.shields.io/badge/License-MIT-brightgreen)](LICENSE)

**فارسی:** یک دوره متن‌باز Ansible برای DevOps و Linux: از Playbook و YAML تا Inventory، Jinja2، Roles، Ansible Vault، Idempotency، تست خودکار و GitHub Actions.

**English:** A bilingual, hands-on Ansible learning path for DevOps and Linux. Learn YAML playbooks, inventory, variables, Jinja2, roles, Vault, idempotency, testing, and GitHub Actions with compact examples.

> [!TIP]
> **قاعده آموزشی / Learning contract:** **یک مسئله → یک اصل مفهومی → یک مثال قابل اجرا → یک آزمایش کوتاه.** One problem → one mental model → one runnable example → one small experiment.

## مسیر ۲۰ درس | 20-lesson curriculum

### شروع سریع · Getting started

| # | آموزش فارسی | English tutorial |
|---|---|---|
| 1 | [Playbook، Task و Handler](1st_day/1st_day_Persian.md) | [First playbook and Nginx](1st_day/1st_day_English.md) |
| 2 | [فایل و قالب Jinja2](2nd_day/2nd_day_Persian.md) | [Files and Jinja2 templates](2nd_day/2nd_day_English.md) |
| 3 | [کاربر و امنیت پایه](3rd_day/README.md) | [User management and safe access](3rd_day/README_EN.md) |
| 4 | [Role و استفاده مجدد](4th_day/README.md) | [Reusable Ansible roles](4th_day/README_EN.md) |
| 5 | [Ansible Vault](5th_day/README.md) | [Encrypting secrets with Vault](5th_day/README_EN.md) |

### درک هسته · Core mental models

| # | آموزش فارسی | English tutorial |
|---|---|---|
| 6 | [Inventory و اولویت متغیرها](6th_day/README.md) | [Inventory and variable precedence](6th_day/README_EN.md) |
| 7 | [Facts و شرط‌ها](7th_day/README.md) | [Facts and when conditions](7th_day/README_EN.md) |
| 8 | [Loops و Filters](8th_day/README.md) | [Loops and Jinja2 filters](8th_day/README_EN.md) |
| 9 | [Blocks و مدیریت خطا](9th_day/README.md) | [Blocks, rescue, and always](9th_day/README_EN.md) |
| 10 | [Import و Include](10th_day/README.md) | [Static imports and dynamic includes](10th_day/README_EN.md) |
| 11 | [Idempotency و Check Mode](11th_day/README.md) | [Idempotency and dry runs](11th_day/README_EN.md) |

### مهارت‌های پیشرفته · Advanced Ansible

| # | آموزش فارسی | English tutorial |
|---|---|---|
| 12 | [Secrets و No Log](12th_day/README.md) | [Secure variable handling](12th_day/README_EN.md) |
| 13 | [Delegation و Run Once](13th_day/README.md) | [Delegation and run_once](13th_day/README_EN.md) |
| 14 | [Retry و Async](14th_day/README.md) | [Retries and async execution](14th_day/README_EN.md) |
| 15 | [Collections و Galaxy](15th_day/README.md) | [Collections and Galaxy](15th_day/README_EN.md) |
| 16 | [Dynamic Inventory](16th_day/README.md) | [Dynamic inventory with Python](16th_day/README_EN.md) |

### تست و کار عملی · Quality and capstone

| # | آموزش فارسی | English tutorial |
|---|---|---|
| 17 | [Testing و Assert](17th_day/README.md) | [Testing Ansible playbooks](17th_day/README_EN.md) |
| 18 | [Performance و Serial](18th_day/README.md) | [Rolling updates and concurrency](18th_day/README_EN.md) |
| 19 | [Security as Code](19th_day/README.md) | [Verifying file permissions](19th_day/README_EN.md) |
| 20 | [پروژه پایانی](20th_day/README.md) | [Configuration pipeline capstone](20th_day/README_EN.md) |

## شروع در ۶۰ ثانیه | Quick start

```bash
git clone https://github.com/mehrdad-dd/ansible_intro.git
cd ansible_intro
python3 -m venv .venv
source .venv/bin/activate
python -m pip install 'ansible-core>=2.19,<2.21'
ansible-playbook -i 6th_day/inventory.yml 6th_day/playbook.yml --syntax-check
ansible-playbook -i 6th_day/inventory.yml 6th_day/playbook.yml
```

**فارسی:** روزهای ۶ تا ۲۰ برای تمرین بدون دسترسی Root روی میزبان محلی طراحی شده‌اند. روزهای ۱ تا ۴ ممکن است فایل‌ها، بسته‌ها یا کاربران سیستم را تغییر دهند؛ فقط در ماشین مجازی آزمایشی و پس از بررسی اجرا شوند.

**English:** Days 6–20 are designed to run locally without root. Days 1–4 can change packages, services, users, or system files; run those only in a disposable VM after reviewing their playbooks.

## چرا این دوره متفاوت است؟ | What makes it different?

- **مفهوم قبل از حفظ دستور / Concepts before commands:** هر دستور پاسخ یک مسئله مشخص است.
- **کد یکتا / One source of code truth:** نمونه YAML و کامنت‌ها در هر دو زبان یکسان‌اند؛ متن آموزشی ترجمه می‌شود.
- **خروجی قابل بررسی / Verifiable results:** بررسی Syntax، اجرای آزمایشی و تست اجرای مجدد.
- **ایمن از ابتدا / Secure by default:** بدون رمز واقعی، کلید خصوصی، IP زیرساخت یا اجرای شبکه‌ای در CI.
- **مختصر، اما نه سطحی / Short, not shallow:** تفاوت‌های کلیدی، اشتباه رایج و یک تمرین عملی در هر درس.

## کیفیت و تست خودکار | GitHub Actions

Workflow: [`.github/workflows/ci.yml`](.github/workflows/ci.yml)

```bash
python3 tools/check_course.py
python3 tools/run_examples.py --syntax
python3 tools/run_examples.py --smoke
```

CI کارهای زیر را بررسی می‌کند: تطابق کد در نسخه فارسی و انگلیسی، لینک‌های داخلی، فرمت YAML، `ansible-lint`، Syntax همه Playbookها و اجرای واقعی مثال‌های بی‌خطر روزهای ۶ تا ۲۰ روی Runner. برای روزهای ۱۱، ۱۹ و ۲۰ اجرای دوم باید `changed=0` باشد.

CI checks bilingual code parity, documentation links, YAML lint, `ansible-lint`, playbook syntax, and safe local smoke tests. Second-run idempotence is verified for days 11, 19, and 20.

## پرسش‌های رایج | FAQ

**آیا برای یادگیری Ansible به چند سرور نیاز دارم؟ / Do I need multiple servers?**  
خیر؛ مثال‌های محلی با `ansible_connection: local` اجرا می‌شوند. No: local inventory is enough for most concepts.

**فرق Playbook و Role چیست؟ / Playbook vs role?**  
Playbook جریان اجرا را تعریف می‌کند؛ Role واحدی قابل‌استفاده‌مجدد از Tasks و فایل‌های مرتبط است. A playbook orchestrates; a role packages reusable behavior.

**Idempotency یعنی چه؟ / What is idempotency?**  
اگر وضعیت مطلوب برقرار باشد، اجرای مجدد نباید تغییر اضافی ایجاد کند. A repeat run should not make unnecessary changes.

**آیا این مثال‌ها برای Production هستند؟ / Production-ready?**  
خیر؛ این‌ها Labهای قابل‌فهم‌اند. پیش از استفاده عملی، Inventory، دسترسی‌ها، نسخه‌ها و روش Rollback را بررسی کنید. No: review and adapt before production.

## امنیت، مشارکت و مجوز | Security, contributing, license

- [Security policy / سیاست امنیتی](SECURITY.md)
- [Contribution guide / راهنمای مشارکت](CONTRIBUTING.md)
- [FA/EN glossary / واژه‌نامه](docs/GLOSSARY.md)
- [Curriculum audit / گزارش بازنگری](AUDIT.md)
- [MIT License / مجوز MIT](LICENSE)

**License note / نکته مجوز:** MIT اجازه استفاده، تغییر و بازنشر را می‌دهد، مشروط به حفظ اعلان حق نشر و متن مجوز. استفاده از مطالب اشخاص ثالث همچنان به داشتن مجوز مناسب نیاز دارد.

**Keywords (naturally covered):** Ansible tutorial, learn Ansible, Ansible playbook examples, Ansible for beginners, Ansible DevOps, Ansible inventory, Ansible Jinja2, Ansible Vault, Ansible roles, Infrastructure as Code, آموزش انسیبل، آموزش Ansible فارسی، آموزش DevOps، اتوماسیون لینوکس.
