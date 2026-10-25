# روز 14 | Retry، Until و Async در Ansible

[English](README_EN.md) · [فهرست دوره](../README.md) · [منبع رسمی](https://docs.ansible.com/projects/ansible-core/stable-2.22/playbook_guide/index.html)

> **مسئله در یک جمله:** اتوماتیک‌سازی باید انتظار کشیدن برای آماده‌شدن سرویس را کنترل کند، نه با تأخیرهای تصادفی.

### نکته عمیق
`until` بررسی را تکرار می‌کند، `retries` سقف تلاش‌ها و `async` اجرای طولانی را مدیریت می‌کند.

### مثال کوتاه و واقعی
```yaml
---
# Shared example: bounded retries and a short async task.
- name: Wait and retry safely
  hosts: lab
  gather_facts: false
  tasks:
    - name: Retry a harmless readiness check
      ansible.builtin.command: /bin/true
      register: readiness
      changed_when: false
      until: readiness.rc == 0
      retries: 3
      delay: 1

    - name: Run a short asynchronous command
      ansible.builtin.command: /bin/sleep 1
      async: 10
      poll: 1
      changed_when: false
```

### اجرا و نتیجه
```bash
ansible-playbook -i 14th_day/inventory.yml 14th_day/playbook.yml --syntax-check
ansible-playbook -i 14th_day/inventory.yml 14th_day/playbook.yml
```

**خروجی مورد انتظار:** Playbook بدون تغییر حساس روی سیستم اجرا می‌شود و پیام یا Assertion واضح نشان می‌دهد.

### اشتباه رایج
Taskهای `async` در حالت `--check` همیشه قابل اجرا نیستند؛ این مثال را واقعی ولی فقط محلی اجرا کن.

**تمرین ۱ دقیقه‌ای:** `retries` را از 3 به 1 تغییر بده؛ چون دستور موفق است نتیجه ثابت می‌ماند.

<sub>نمونه آزمایشی است؛ هیچ رمز، IP واقعی یا دسترسی مدیریتی نیاز ندارد.</sub>
