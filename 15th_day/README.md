# روز 15 | Collections، Galaxy و FQCN در Ansible

[English](README_EN.md) · [فهرست دوره](../README.md) · [منبع رسمی](https://docs.ansible.com/projects/ansible-core/stable-2.22/playbook_guide/index.html)

> **مسئله در یک جمله:** ماژول‌های Ansible داخل Namespace/Collection هستند؛ نام کامل ابهام و وابستگی پنهان را کم می‌کند.

### نکته عمیق
`ansible.builtin.debug` یک FQCN است؛ برای Collection بیرونی نسخه مشخص‌شده در `requirements.yml` نصب می‌شود.

### مثال کوتاه و واقعی
```yaml
---
# Shared example: use unambiguous built-in module names.
- name: Explain collections and module namespaces
  hosts: lab
  gather_facts: false
  tasks:
    - name: Use a fully qualified module name
      ansible.builtin.debug:
        msg: "Module namespace: ansible.builtin"

    - name: Verify collection metadata example
      ansible.builtin.assert:
        that: "'ansible.builtin.debug'.startswith('ansible.builtin')"
```

**وابستگی اختیاری:** [`requirements.yml`](requirements.yml)

### اجرا و نتیجه
```bash
ansible-playbook -i 15th_day/inventory.yml 15th_day/playbook.yml --syntax-check
ansible-playbook -i 15th_day/inventory.yml 15th_day/playbook.yml
```

**خروجی مورد انتظار:** Playbook بدون تغییر حساس روی سیستم اجرا می‌شود و پیام یا Assertion واضح نشان می‌دهد.

### اشتباه رایج
وجود `requirements.yml` نصب خودکار نیست؛ Collection را آگاهانه و از منبع معتبر نصب کن.

**تمرین ۱ دقیقه‌ای:** `ansible-galaxy collection list` را اجرا کن و تفاوت builtin با Collection بیرونی را ببین.

<sub>نمونه آزمایشی است؛ هیچ رمز، IP واقعی یا دسترسی مدیریتی نیاز ندارد.</sub>
