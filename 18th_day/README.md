# روز 18 | Performance، Serial و Throttle در Ansible

[English](README_EN.md) · [فهرست دوره](../README.md) · [منبع رسمی](https://docs.ansible.com/projects/ansible-core/stable-2.22/playbook_guide/index.html)

> **مسئله در یک جمله:** افزایش سرعت همیشه هدف نیست؛ گاهی تعداد میزبان‌های هم‌زمان باید محدود شود.

### نکته عمیق
`serial: 1` اجرای هر Batch را به یک میزبان محدود می‌کند؛ `throttle` تعداد اجرای هم‌زمان Task را مهار می‌کند.

### مثال کوتاه و واقعی
```yaml
---
# Shared example: intentionally bounded concurrency.
- name: Configure hosts in small batches
  hosts: lab
  gather_facts: false
  serial: 1
  strategy: linear
  tasks:
    - name: Show current rollout host
      ansible.builtin.debug:
        msg: "Working on {{ inventory_hostname }}"
      throttle: 1
```

### اجرا و نتیجه
```bash
ansible-playbook -i 18th_day/inventory.yml 18th_day/playbook.yml --syntax-check
ansible-playbook -i 18th_day/inventory.yml 18th_day/playbook.yml
```

**خروجی مورد انتظار:** Playbook بدون تغییر حساس روی سیستم اجرا می‌شود و پیام یا Assertion واضح نشان می‌دهد.

### اشتباه رایج
استفاده از `run_once` کنار `serial` به معنی یک‌بار در کل Play نیست.

**تمرین ۱ دقیقه‌ای:** `serial: 2` را امتحان کن و ترتیب Batchها را مقایسه کن.

<sub>نمونه آزمایشی است؛ هیچ رمز، IP واقعی یا دسترسی مدیریتی نیاز ندارد.</sub>
