# Day 1 | Your First Playbook

[فارسی](1st_day_Persian.md)

**Goal:** Install Nginx, publish an HTML page, and inspect disk usage in one small playbook.

## Concepts at a glance

| Concept | Example |
|---|---|
| `hosts` | `lab` |
| `become` | `true` |
| `vars` | `web_package: nginx` |
| Task and module | `ansible.builtin.apt` |
| Captured output | `register` |
| Only on change | `notify` + handler |
| Read-only command | `changed_when: false` |

## Shared runnable playbook

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

## Structure

```text
1st_day/
├── 1st_day_English.md
├── 1st_day_Persian.md
├── inventory.ini
└── playbook.yml
```

## Test and run

```bash
ansible-playbook -i 1st_day/inventory.ini 1st_day/playbook.yml --syntax-check
ansible-playbook -i 1st_day/inventory.ini 1st_day/playbook.yml --check --diff
ansible-playbook -i 1st_day/inventory.ini 1st_day/playbook.yml --ask-become-pass
```

> [!WARNING]
> The sample inventory points to `localhost`; real execution changes packages and services on that system. Use a disposable Debian/Ubuntu VM.

**Try:** Change `page_title`, run again, and observe that the handler runs only if the file content changes.
