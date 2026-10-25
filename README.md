# Ansible Intro | آموزش کاربردی Ansible

**فارسی:** آموزش گام‌به‌گام، کوتاه و عملی Ansible؛ هر درس = یک مفهوم، یک مثال و روش اجرا.

**English:** Short, practical Ansible lessons; each day focuses on one concept, one runnable example, and verification.

![Ansible](https://img.shields.io/badge/Ansible-Learning-EE0000?logo=ansible&logoColor=white) ![License](https://img.shields.io/badge/License-MIT-blue) ![Languages](https://img.shields.io/badge/Languages-FA%20%7C%20EN-555)

## Learning path | مسیر یادگیری

| Day | فارسی | English | Focus |
|---|---|---|---|
| 1 | [روز اول](1st_day/1st_day_Persian.md) | [Day 1](1st_day/1st_day_English.md) | Playbook, tasks, variables, handlers |
| 2 | [روز دوم](2nd_day/2nd_day_Persian.md) | [Day 2](2nd_day/2nd_day_English.md) | Files, templates, Jinja2 |
| 3 | [روز سوم](3rd_day/README.md) | [Day 3](3rd_day/README_EN.md) | Users, conditions, security basics |
| 4 | [روز چهارم](4th_day/README.md) | [Day 4](4th_day/README_EN.md) | Roles and reuse |
| 5 | [روز پنجم](5th_day/README.md) | [Day 5](5th_day/README_EN.md) | Ansible Vault |

## Quick start | شروع سریع

```bash
git clone https://github.com/mehrdad-dd/ansible_intro.git
cd ansible_intro
ansible --version
ansible-playbook -i 2nd_day/inventory.ini 2nd_day/playbook.yml --syntax-check
```

**فارسی:** پیش از اجرای واقعی، Inventory، مسیرها، دسترسی sudo و تأثیر taskها را بررسی کنید. مثال‌ها برای VM آزمایشی Debian/Ubuntu طراحی شده‌اند. دستور `--syntax-check` اجرای واقعی نیست.

**English:** Review inventory, paths, sudo access, and task effects before execution. Examples target a disposable Debian/Ubuntu VM. `--syntax-check` does not execute tasks.

> [!CAUTION]
> Never commit tokens, SSH private keys, passwords, Vault password files, or actual infrastructure addresses. / رمزها، کلیدهای خصوصی و اطلاعات واقعی زیرساخت را منتشر نکنید.

## Scope | محدوده

**فارسی:** این مخزن یک مسیر آموزشی در حال توسعه است، نه ادعای پوشش تمام قابلیت‌های Ansible. دروس بعدی می‌توانند Inventory پیشرفته، Facts، Collections، Testing و CI را پوشش دهند.

**English:** This is a growing learning path, not yet a complete reference. Planned next topics include advanced inventory, facts, collections, testing, and CI.

## License | مجوز

[MIT License](LICENSE) — free reuse with copyright and license notice preserved.
