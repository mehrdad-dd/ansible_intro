# روز 10 | Import و Include؛ تفاوت استاتیک و داینامیک در Ansible

[English](README_EN.md) · [فهرست دوره](../README.md) · [منبع رسمی](https://docs.ansible.com/projects/ansible-core/stable-2.22/playbook_guide/index.html)

> **مسئله در یک جمله:** فایل‌های Task را برای خوانایی جدا کن؛ تفاوت اصلی Import و Include زمانِ بارگذاری آن‌هاست.

### نکته عمیق
`import_tasks` هنگام پردازش Playbook گسترش می‌یابد؛ `include_tasks` هنگام اجرا تصمیم می‌گیرد چه فایلی بار شود.

### مثال کوتاه و واقعی
```yaml
---
# Shared example: static and dynamic task inclusion.
- name: Reuse task files
  hosts: lab
  gather_facts: false
  vars:
    show_optional: true
  tasks:
    - name: Load tasks statically
      ansible.builtin.import_tasks: tasks/prepare.yml

    - name: Load optional tasks at runtime
      ansible.builtin.include_tasks: tasks/optional.yml
      when: show_optional | bool
```

**فایل‌های Task:** [`prepare.yml`](tasks/prepare.yml) · [`optional.yml`](tasks/optional.yml)

### اجرا و نتیجه
```bash
ansible-playbook -i 10th_day/inventory.yml 10th_day/playbook.yml --syntax-check
ansible-playbook -i 10th_day/inventory.yml 10th_day/playbook.yml
```

**خروجی مورد انتظار:** Playbook بدون تغییر حساس روی سیستم اجرا می‌شود و پیام یا Assertion واضح نشان می‌دهد.

### اشتباه رایج
رفتار `--list-tasks` و `--tags` برای Include و Import یکسان نیست.

**تمرین ۱ دقیقه‌ای:** `show_optional=false` را با `-e` ارسال کن و حذف مرحله اختیاری را ببین.

<sub>نمونه آزمایشی است؛ هیچ رمز، IP واقعی یا دسترسی مدیریتی نیاز ندارد.</sub>
