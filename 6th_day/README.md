# روز 6 | Inventory و اولویت متغیرها در Ansible

[English](README_EN.md) · [فهرست دوره](../README.md) · [منبع رسمی](https://docs.ansible.com/projects/ansible-core/stable-2.22/playbook_guide/index.html)

> **مسئله در یک جمله:** Inventory فقط فهرست IP نیست؛ گروه‌بندی میزبان‌ها و تعیین رفتار مشترک را هم انجام می‌دهد.

### نکته عمیق
`group_vars/lab.yml` برای همه اعضای گروه `lab` اعمال می‌شود. `-e` برای override آزمایشی اولویت بالایی دارد.

### مثال کوتاه و واقعی
```yaml
---
# Shared example: inventory, group_vars, variable precedence.
- name: Read lab inventory variables
  hosts: lab
  gather_facts: false
  tasks:
    - name: Explain effective settings
      ansible.builtin.debug:
        msg: "{{ inventory_hostname }} listens on {{ demo_port }} ({{ demo_region }})"

    - name: Validate chosen port
      ansible.builtin.assert:
        that:
          - demo_port | int > 0
          - demo_port | int < 65536
```

### اجرا و نتیجه
```bash
ansible-playbook -i 6th_day/inventory.yml 6th_day/playbook.yml --syntax-check
ansible-playbook -i 6th_day/inventory.yml 6th_day/playbook.yml
```

**خروجی مورد انتظار:** Playbook بدون تغییر حساس روی سیستم اجرا می‌شود و پیام یا Assertion واضح نشان می‌دهد.

### اشتباه رایج
مقادیر حساس را در Inventory عمومی ننویس؛ برای رمزها از Vault استفاده کن.

**تمرین ۱ دقیقه‌ای:** با `-e demo_port=9090` اجرا کن و تفاوت خروجی را ببین.

<sub>نمونه آزمایشی است؛ هیچ رمز، IP واقعی یا دسترسی مدیریتی نیاز ندارد.</sub>
