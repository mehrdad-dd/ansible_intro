# روز 2 | مدیریت فایل و قالب Jinja2 در Ansible

[English](2nd_day_English.md) · [فهرست دوره](../README.md)

> **مسئله:** Template داده و شکل فایل تنظیمات را از هم جدا می‌کند.

### مدل ذهنی
`template` قالب Jinja2 را خروجی می‌دهد؛ `lineinfile` یک خط، `blockinfile` یک بلوک و `stat` وضعیت فایل را مدیریت یا بررسی می‌کنند.

### کد مشترک و قابل اجرا
```yaml
---
# Day 2: file operations and Jinja2 templates (Debian/Ubuntu lab).
- name: Manage an application configuration
  hosts: lab
  become: true
  vars:
    app_dir: /opt/ansible-demo
    app_port: 8080
    app_environment: staging
  tasks:
    - name: Create application directory
      ansible.builtin.file:
        path: "{{ app_dir }}"
        state: directory
        owner: root
        group: root
        mode: '0755'

    - name: Render configuration from a template
      ansible.builtin.template:
        src: templates/app.conf.j2
        dest: "{{ app_dir }}/app.conf"
        owner: root
        group: root
        mode: '0644'
        backup: true

    - name: Ensure a configuration line exists
      ansible.builtin.lineinfile:
        path: "{{ app_dir }}/app.conf"
        regexp: '^managed_by='
        line: managed_by=ansible

    - name: Add a managed configuration block
      ansible.builtin.blockinfile:
        path: "{{ app_dir }}/notes.txt"
        create: true
        mode: '0644'
        block: |
          environment={{ app_environment }}
          port={{ app_port }}

    - name: Inspect the rendered configuration
      ansible.builtin.stat:
        path: "{{ app_dir }}/app.conf"
      register: config_stat

    - name: Show file status
      ansible.builtin.debug:
        msg: "Configuration exists: {{ config_stat.stat.exists }}"

    - name: Download configuration to the control machine
      ansible.builtin.fetch:
        src: "{{ app_dir }}/app.conf"
        dest: fetched/
        flat: false
```

**قالب:** [`app.conf.j2`](templates/app.conf.j2)

### نحوه اجرا
```bash
ansible-playbook -i 2nd_day/inventory.ini 2nd_day/playbook.yml --syntax-check
# Run only inside a disposable Debian/Ubuntu VM:
ansible-playbook -i 2nd_day/inventory.ini 2nd_day/playbook.yml --ask-become-pass
```

> [!WARNING]
> این درس در `/opt` می‌نویسد و sudo لازم دارد؛ Check Mode روی میزبان خام ممکن است محدود باشد.

**تمرین یک دقیقه‌ای:** `app_port` را تغییر بده و محتوای تولیدشده `app.conf` را مقایسه کن.

**نکته:** فایل‌های نمونه از رمز و اطلاعات زیرساخت واقعی استفاده نمی‌کنند.
