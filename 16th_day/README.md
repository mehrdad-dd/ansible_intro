# روز 16 | Dynamic Inventory با Python در Ansible

[English](README_EN.md) · [فهرست دوره](../README.md) · [منبع رسمی](https://docs.ansible.com/projects/ansible-core/stable-2.22/playbook_guide/index.html)

> **مسئله در یک جمله:** وقتی سرورها دائم عوض می‌شوند، Inventory را می‌توان هنگام اجرا از یک برنامه تولید کرد.

### نکته عمیق
اسکریپت باید خروجی JSON برای `--list` بدهد و اجرای آن هیچ تغییری در سیستم ایجاد نکند.

### مثال کوتاه و واقعی
```yaml
---
# Shared example: consume a dynamic inventory.
- name: Use generated inventory groups
  hosts: lab
  gather_facts: false
  tasks:
    - name: Identify dynamically generated hosts
      ansible.builtin.debug:
        msg: "Dynamic inventory host: {{ inventory_hostname }}"
```

**اسکریپت Inventory:** [`inventory.py`](inventory.py)

### اجرا و نتیجه
```bash
ansible-playbook -i 16th_day/inventory.py 16th_day/playbook.yml --syntax-check
ansible-playbook -i 16th_day/inventory.py 16th_day/playbook.yml
```

**خروجی مورد انتظار:** Playbook بدون تغییر حساس روی سیستم اجرا می‌شود و پیام یا Assertion واضح نشان می‌دهد.

### اشتباه رایج
اسکریپت Inventory را از اینترنت و ورودی نامطمئن بدون اعتبارسنجی اجرا نکن.

**تمرین ۱ دقیقه‌ای:** `ansible-inventory -i inventory.py --graph` را اجرا کن.

<sub>نمونه آزمایشی است؛ هیچ رمز، IP واقعی یا دسترسی مدیریتی نیاز ندارد.</sub>
