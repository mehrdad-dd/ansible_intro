# روز 9 | مدیریت خطا با Block و Rescue در Ansible

[English](README_EN.md) · [فهرست دوره](../README.md) · [منبع رسمی](https://docs.ansible.com/projects/ansible-core/stable-2.22/playbook_guide/index.html)

> **مسئله در یک جمله:** همه خطاها نباید کل فرایند را متوقف کنند؛ اما باید روشن باشد چه چیزی واقعاً بازیابی شده است.

### نکته عمیق
`block` عملیات اصلی، `rescue` واکنش به شکست Task و `always` مرحله نهایی است.

### مثال کوتاه و واقعی
```yaml
---
# Shared example: controlled failure and recovery.
- name: Recover from a task failure
  hosts: lab
  gather_facts: false
  vars:
    demo_ready: false
  tasks:
    - name: Demonstrate a controlled recovery
      block:
        - name: Check readiness
          ansible.builtin.assert:
            that: demo_ready | bool
            fail_msg: Demo is intentionally not ready.

        - name: Report success
          ansible.builtin.debug:
            msg: The normal path completed.
      rescue:
        - name: Explain fallback action
          ansible.builtin.debug:
            msg: A controlled failure was handled.
      always:
        - name: Report cleanup phase
          ansible.builtin.debug:
            msg: The final step always runs.
```

### اجرا و نتیجه
```bash
ansible-playbook -i 9th_day/inventory.yml 9th_day/playbook.yml --syntax-check
ansible-playbook -i 9th_day/inventory.yml 9th_day/playbook.yml
```

**خروجی مورد انتظار:** پیام Rescue و سپس Always دیده می‌شود.

### اشتباه رایج
`rescue` سرور قطع‌شده یا خطای نحوی را الزاماً نجات نمی‌دهد.

**تمرین ۱ دقیقه‌ای:** با `-e demo_ready=true` اجرا کن تا مسیر بدون Rescue را ببینی.

<sub>نمونه آزمایشی است؛ هیچ رمز، IP واقعی یا دسترسی مدیریتی نیاز ندارد.</sub>
