# روز 7 | Facts و شرط‌های دقیق در Ansible

[English](README_EN.md) · [فهرست دوره](../README.md) · [منبع رسمی](https://docs.ansible.com/projects/ansible-core/stable-2.22/playbook_guide/index.html)

> **مسئله در یک جمله:** Ansible اطلاعات واقعی میزبان را در Facts جمع می‌کند؛ شرط‌ها باید بر همین داده‌ها تکیه کنند، نه حدس.

### نکته عمیق
`gather_facts: true` اطلاعات سیستم را بارگذاری می‌کند؛ `when` باید یک عبارت بولی بدون `{{ }}` باشد.

### مثال کوتاه و واقعی
```yaml
---
# Shared example: host facts and conditions.
- name: Use facts for conditional behavior
  hosts: lab
  gather_facts: true
  tasks:
    - name: Show the detected operating system
      ansible.builtin.debug:
        msg: "{{ ansible_facts['distribution'] }} is in {{ ansible_facts['os_family'] }}"

    - name: Explain a Debian-specific task
      ansible.builtin.debug:
        msg: This branch would manage APT packages.
      when: ansible_facts['os_family'] == 'Debian'

    - name: Explain the fallback branch
      ansible.builtin.debug:
        msg: This host is not in the Debian family.
      when: ansible_facts['os_family'] != 'Debian'
```

### اجرا و نتیجه
```bash
ansible-playbook -i 7th_day/inventory.yml 7th_day/playbook.yml --syntax-check
ansible-playbook -i 7th_day/inventory.yml 7th_day/playbook.yml
```

**خروجی مورد انتظار:** Playbook بدون تغییر حساس روی سیستم اجرا می‌شود و پیام یا Assertion واضح نشان می‌دهد.

### اشتباه رایج
نام توزیع را با خانواده سیستم‌عامل (`os_family`) اشتباه نگیر.

**تمرین ۱ دقیقه‌ای:** سیستم خود را شناسایی کن و نتیجه شرط Debian را بررسی کن.

<sub>نمونه آزمایشی است؛ هیچ رمز، IP واقعی یا دسترسی مدیریتی نیاز ندارد.</sub>
