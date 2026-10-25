# روز 1 | اولین Playbook؛ ماژول، متغیر و Handler در Ansible

[English](1st_day_English.md) · [فهرست دوره](../README.md)

> **مسئله:** Playbook وضعیت مطلوب میزبان را تعریف می‌کند؛ فقط فهرست دستورهای پشت‌سرهم نیست.

### مدل ذهنی
Task یک ماژول را اجرا می‌کند، متغیرها رفتار را تعیین می‌کنند و Handler در صورت تغییر فراخوانی می‌شود.

### کد مشترک و قابل اجرا
```yaml
---
# Day 1: tasks, variables, loops, conditionals, handlers.
- name: Deploy a simple Nginx page
  hosts: lab
  become: true
  vars:
    web_package: nginx
    page_title: Ansible Demo
  tasks:
    - name: Refresh APT cache
      ansible.builtin.apt:
        update_cache: true
        cache_valid_time: 3600

    - name: Install web server and CLI tools
      ansible.builtin.apt:
        name:
          - "{{ web_package }}"
          - curl
          - git
        state: present

    - name: Publish a welcome page
      ansible.builtin.copy:
        dest: /var/www/html/index.html
        content: "<h1>{{ page_title }}</h1>\n"
        owner: root
        group: root
        mode: '0644'
      notify: reload nginx

    - name: Start and enable Nginx
      ansible.builtin.service:
        name: nginx
        state: started
        enabled: true

    - name: Get disk usage
      ansible.builtin.command: df -h /
      register: disk_usage
      changed_when: false

    - name: Show disk usage
      ansible.builtin.debug:
        msg: "{{ disk_usage.stdout }}"

  handlers:
    - name: reload nginx
      ansible.builtin.service:
        name: nginx
        state: reloaded
```

### نحوه اجرا
```bash
ansible-playbook -i 1st_day/inventory.ini 1st_day/playbook.yml --syntax-check
# Run only inside a disposable Debian/Ubuntu VM:
ansible-playbook -i 1st_day/inventory.ini 1st_day/playbook.yml --ask-become-pass
```

> [!WARNING]
> این آزمایش با sudo وب‌سرور نصب می‌کند؛ هرگز آن را مستقیم روی سرور عملیاتی اجرا نکن.

**تمرین یک دقیقه‌ای:** `page_title` را تغییر بده و رفتار Handler را مقایسه کن.

**نکته:** فایل‌های نمونه از رمز و اطلاعات زیرساخت واقعی استفاده نمی‌کنند.
