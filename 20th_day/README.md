# روز 20 | پروژه نهایی: Config Pipeline کوچک در Ansible

[English](README_EN.md) · [فهرست دوره](../README.md) · [منبع رسمی](https://docs.ansible.com/projects/ansible-core/stable-2.22/playbook_guide/index.html)

> **مسئله در یک جمله:** در پروژه واقعی، Inventory، متغیر، Template، اعتبارسنجی و Handler در یک جریان به هم متصل می‌شوند.

### نکته عمیق
قالب Jinja2 خروجی می‌سازد؛ `stat` آن را می‌سنجد؛ Handler فقط تغییر واقعی را گزارش می‌کند.

### مثال کوتاه و واقعی
```yaml
---
# Shared capstone: configure, render, verify, notify.
- name: Build a small configuration pipeline
  hosts: lab
  gather_facts: false
  vars:
    service_port: 8080
    service_environment: staging
    output_dir: "{{ playbook_dir }}/rendered"
  tasks:
    - name: Create output directory
      ansible.builtin.file:
        path: "{{ output_dir }}"
        state: directory
        mode: '0755'

    - name: Render the application configuration
      ansible.builtin.template:
        src: templates/service.conf.j2
        dest: "{{ output_dir }}/service.conf"
        mode: '0644'
      notify: Report config update

    - name: Inspect the generated configuration
      ansible.builtin.stat:
        path: "{{ output_dir }}/service.conf"
      register: rendered

    - name: Assert that the configuration exists
      ansible.builtin.assert:
        that: rendered.stat.exists

  handlers:
    - name: Report config update
      ansible.builtin.debug:
        msg: Configuration changed; validate before reloading a real service.
```

**قالب مرتبط:** [`templates/service.conf.j2`](templates/service.conf.j2)

### اجرا و نتیجه
```bash
ansible-playbook -i 20th_day/inventory.yml 20th_day/playbook.yml --syntax-check
ansible-playbook -i 20th_day/inventory.yml 20th_day/playbook.yml
```

**خروجی مورد انتظار:** در اجرای دوم بدون تغییر ورودی، `changed=0` است.

### اشتباه رایج
Handler این درس فقط پیام می‌دهد؛ در سیستم واقعی قبل از Reload باید اعتبارسنجی سرویس داشته باشی.

**تمرین ۱ دقیقه‌ای:** `service_port` را تغییر بده و اجرای اول، دوم و بعد از تغییر را مقایسه کن.

<sub>نمونه آزمایشی است؛ هیچ رمز، IP واقعی یا دسترسی مدیریتی نیاز ندارد.</sub>
