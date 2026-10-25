# روز 17 | Testing، Assert و قراردادهای خودکار در Ansible

[English](README_EN.md) · [فهرست دوره](../README.md) · [منبع رسمی](https://docs.ansible.com/projects/ansible-core/stable-2.22/playbook_guide/index.html)

> **مسئله در یک جمله:** تست خوب فقط سالم‌بودن YAML نیست؛ نتیجه موردانتظار را هم بررسی می‌کند.

### نکته عمیق
`assert` یک قرارداد واضح می‌سازد؛ `changed_when: false` روی کارهای خواندنی جلوی گزارش تغییر ساختگی را می‌گیرد.

### مثال کوتاه و واقعی
```yaml
---
# Shared example: executable expectations.
- name: Validate a small configuration contract
  hosts: lab
  gather_facts: false
  vars:
    endpoint_port: 8080
  tasks:
    - name: Validate the TCP port range
      ansible.builtin.assert:
        that:
          - endpoint_port | int >= 1
          - endpoint_port | int <= 65535
        fail_msg: Port must be between 1 and 65535.

    - name: Show the validated value
      ansible.builtin.debug:
        msg: "Validated port: {{ endpoint_port }}"
```

### اجرا و نتیجه
```bash
ansible-playbook -i 17th_day/inventory.yml 17th_day/playbook.yml --syntax-check
ansible-playbook -i 17th_day/inventory.yml 17th_day/playbook.yml
```

**خروجی مورد انتظار:** Playbook بدون تغییر حساس روی سیستم اجرا می‌شود و پیام یا Assertion واضح نشان می‌دهد.

### اشتباه رایج
`--syntax-check` برای تضمین اجرا، امنیت یا Idempotency کافی نیست.

**تمرین ۱ دقیقه‌ای:** پورت 70000 را با `-e endpoint_port=70000` بده و شکست کنترل‌شده را ببین.

<sub>نمونه آزمایشی است؛ هیچ رمز، IP واقعی یا دسترسی مدیریتی نیاز ندارد.</sub>
