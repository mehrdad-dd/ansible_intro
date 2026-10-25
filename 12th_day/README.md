# روز 12 | Secrets و No Log بدون افشای رمز در Ansible

[English](README_EN.md) · [فهرست دوره](../README.md) · [منبع رسمی](https://docs.ansible.com/projects/ansible-core/stable-2.22/playbook_guide/index.html)

> **مسئله در یک جمله:** امنیت با مخفی‌کردن یک پیام در لاگ تمام نمی‌شود؛ راز نباید وارد Git شود.

### نکته عمیق
`lookup('ansible.builtin.env',...)` فقط وضعیت وجود یک متغیر محیطی را بررسی می‌کند؛ مقدار آن چاپ یا ذخیره نمی‌شود.

### مثال کوتاه و واقعی
```yaml
---
# Shared example: avoid exposing a secret's contents.
- name: Check secret availability safely
  hosts: lab
  gather_facts: false
  tasks:
    - name: Detect whether an environment token exists
      ansible.builtin.set_fact:
        demo_token_provided: "{{ (lookup('ansible.builtin.env', 'ANSIBLE_DEMO_TOKEN') | length) > 0 }}"
      no_log: true

    - name: Report only a Boolean status
      ansible.builtin.debug:
        msg: "Example token configured: {{ demo_token_provided | bool }}"
```

### اجرا و نتیجه
```bash
ansible-playbook -i 12th_day/inventory.yml 12th_day/playbook.yml --syntax-check
ansible-playbook -i 12th_day/inventory.yml 12th_day/playbook.yml
```

**خروجی مورد انتظار:** Playbook بدون تغییر حساس روی سیستم اجرا می‌شود و پیام یا Assertion واضح نشان می‌دهد.

### اشتباه رایج
`no_log` رمزگذاری نیست؛ برای داده ذخیره‌شده از Vault و برای CI از Secrets مخزن استفاده کن.

**تمرین ۱ دقیقه‌ای:** یک متغیر محیطی ساختگی تعریف کن و فقط مقدار بولی خروجی را ببین.

<sub>نمونه آزمایشی است؛ هیچ رمز، IP واقعی یا دسترسی مدیریتی نیاز ندارد.</sub>
