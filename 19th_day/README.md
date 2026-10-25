# روز 19 | Security as Code و مجوز فایل‌ها در Ansible

[English](README_EN.md) · [فهرست دوره](../README.md) · [منبع رسمی](https://docs.ansible.com/projects/ansible-core/stable-2.22/playbook_guide/index.html)

> **مسئله در یک جمله:** امنیت باید قابل اندازه‌گیری باشد؛ مثلاً فایل حساس باید سطح دسترسی `0600` داشته باشد.

### نکته عمیق
`copy` وضعیت مطلوب را تنظیم می‌کند و `stat` همراه `assert` همان وضعیت را بررسی می‌کند.

### مثال کوتاه و واقعی
```yaml
---
# Shared example: enforce and verify file permissions.
- name: Verify a lab-only private file
  hosts: lab
  gather_facts: false
  tasks:
    - name: Write a synthetic demo file with strict mode
      ansible.builtin.copy:
        dest: "{{ playbook_dir }}/demo-secret.txt"
        content: "synthetic-training-data-only\n"
        mode: '0600'
      no_log: true

    - name: Inspect file permissions
      ansible.builtin.stat:
        path: "{{ playbook_dir }}/demo-secret.txt"
      register: demo_file

    - name: Enforce the permission contract
      ansible.builtin.assert:
        that:
          - demo_file.stat.exists
          - demo_file.stat.mode == '0600'
```

### اجرا و نتیجه
```bash
ansible-playbook -i 19th_day/inventory.yml 19th_day/playbook.yml --syntax-check
ansible-playbook -i 19th_day/inventory.yml 19th_day/playbook.yml
```

**خروجی مورد انتظار:** در اجرای دوم بدون تغییر ورودی، `changed=0` است.

### اشتباه رایج
متن این مثال ساختگی است؛ حتی فایل‌های رمزنگاری‌شده هم جایگزین سیاست مدیریت Secrets نیستند.

**تمرین ۱ دقیقه‌ای:** برای فایل آزمایشی `mode: '0644'` بگذار و شکست Assertion را ببین.

<sub>نمونه آزمایشی است؛ هیچ رمز، IP واقعی یا دسترسی مدیریتی نیاز ندارد.</sub>
