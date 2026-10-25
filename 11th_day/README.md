# روز 11 | Idempotency و حالت Check/Diff در Ansible

[English](README_EN.md) · [فهرست دوره](../README.md) · [منبع رسمی](https://docs.ansible.com/projects/ansible-core/stable-2.22/playbook_guide/index.html)

> **مسئله در یک جمله:** تعریف اتوماسیون خوب این نیست که هر بار اجرا شود؛ این است که با اجرای دوباره بی‌دلیل تغییری ایجاد نکند.

### نکته عمیق
`copy` تغییر را تشخیص می‌دهد؛ Handler فقط هنگام تغییر اجرا می‌شود و `--check --diff` پیش‌نمایش می‌دهد.

### مثال کوتاه و واقعی
```yaml
---
# Shared example: convergent file management.
- name: Prove idempotent behavior
  hosts: lab
  gather_facts: false
  tasks:
    - name: Keep a predictable text file
      ansible.builtin.copy:
        dest: "{{ playbook_dir }}/demo-output.txt"
        content: "managed_by=ansible\n"
        mode: '0644'
      notify: Report file update

  handlers:
    - name: Report file update
      ansible.builtin.debug:
        msg: Content actually changed.
```

### اجرا و نتیجه
```bash
ansible-playbook -i 11th_day/inventory.yml 11th_day/playbook.yml --syntax-check
ansible-playbook -i 11th_day/inventory.yml 11th_day/playbook.yml
```

**خروجی مورد انتظار:** در اجرای دوم بدون تغییر ورودی، `changed=0` است.

### اشتباه رایج
`--check` جای تست واقعی را نمی‌گیرد و همه ماژول‌ها پیش‌نمایش کامل ندارند.

**تمرین ۱ دقیقه‌ای:** دو بار اجرا کن؛ دفعه دوم باید `changed=0` باشد.

<sub>نمونه آزمایشی است؛ هیچ رمز، IP واقعی یا دسترسی مدیریتی نیاز ندارد.</sub>
