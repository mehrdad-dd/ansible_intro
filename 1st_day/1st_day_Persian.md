# روز اول | اولین Playbook

[English](1st_day_English.md)

**هدف:** با یک Playbook کوچک Nginx نصب کنیم، صفحه HTML بسازیم و اطلاعات دیسک را ببینیم.

## مفهوم در یک نگاه

| مفهوم | مثال |
|---|---|
| `hosts` | `lab` |
| `become` | `true` |
| `vars` | `web_package: nginx` |
| وظیفه و ماژول | `ansible.builtin.apt` |
| ثبت خروجی | `register` |
| فقط هنگام تغییر | `notify` + handler |
| اجرای بدون تغییر | `changed_when: false` |

## فایل اجرایی مشترک

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

## ساختار

```text
1st_day/
├── 1st_day_English.md
├── 1st_day_Persian.md
├── inventory.ini
└── playbook.yml
```

## تست و اجرا

```bash
ansible-playbook -i 1st_day/inventory.ini 1st_day/playbook.yml --syntax-check
ansible-playbook -i 1st_day/inventory.ini 1st_day/playbook.yml --check --diff
ansible-playbook -i 1st_day/inventory.ini 1st_day/playbook.yml --ask-become-pass
```

> [!WARNING]
> Inventory نمونه به `localhost` اشاره می‌کند و اجرای واقعی بسته و سرویس روی همان سیستم را تغییر می‌دهد. فقط از ماشین آزمایشی Debian/Ubuntu استفاده کنید.

**تمرین:** مقدار `page_title` را تغییر دهید، دوباره اجرا کنید و ببینید Handler فقط در زمان تغییر محتوا اجرا می‌شود.
