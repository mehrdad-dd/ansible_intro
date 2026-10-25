# روز 13 | Delegation و Run Once در Ansible

[English](README_EN.md) · [فهرست دوره](../README.md) · [منبع رسمی](https://docs.ansible.com/projects/ansible-core/stable-2.22/playbook_guide/index.html)

> **مسئله در یک جمله:** گاهی دستور باید برای چند میزبان تصمیم بگیرد اما فقط روی کنترل‌نود اجرا شود.

### نکته عمیق
`delegate_to: localhost` محل اجرا را عوض می‌کند؛ `run_once` یک‌بار در Play یا هر Batch با `serial` اجرا می‌شود.

### مثال کوتاه و واقعی
```yaml
---
# Shared example: delegate one task to the controller.
- name: Delegate centrally, report per host
  hosts: lab
  gather_facts: false
  tasks:
    - name: Perform one central check
      ansible.builtin.debug:
        msg: Checked centrally on the control node.
      delegate_to: localhost
      run_once: true

    - name: Report each inventory host
      ansible.builtin.debug:
        msg: "Current inventory host: {{ inventory_hostname }}"
```

### اجرا و نتیجه
```bash
ansible-playbook -i 13th_day/inventory.yml 13th_day/playbook.yml --syntax-check
ansible-playbook -i 13th_day/inventory.yml 13th_day/playbook.yml
```

**خروجی مورد انتظار:** Playbook بدون تغییر حساس روی سیستم اجرا می‌شود و پیام یا Assertion واضح نشان می‌دهد.

### اشتباه رایج
نمایش داده از `inventory_hostname` لزوماً نشان‌دهنده میزبان اجرای Task نیست.

**تمرین ۱ دقیقه‌ای:** در Inventory دو میزبان مجازی داریم؛ تعداد اجرای هر Task را بررسی کن.

<sub>نمونه آزمایشی است؛ هیچ رمز، IP واقعی یا دسترسی مدیریتی نیاز ندارد.</sub>
