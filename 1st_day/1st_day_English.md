# Ansible Day 1 | First playbook: modules, variables, handlers

[فارسی](1st_day_Persian.md) · [Course index](../README.md)

> **The problem:** A playbook states what each target host should look like, not just a list of commands.

### Mental model
A task calls a module, variables configure behavior, and a notified handler reacts to change.

### Shared runnable example
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

### How to run
```bash
ansible-playbook -i 1st_day/inventory.ini 1st_day/playbook.yml --syntax-check
# Run only inside a disposable Debian/Ubuntu VM:
ansible-playbook -i 1st_day/inventory.ini 1st_day/playbook.yml --ask-become-pass
```

> [!WARNING]
> This lab installs Nginx with sudo. Never point a beginner lab at a production host.

**One-minute experiment:** Change `page_title` and compare the handler behavior.

**Note:** Samples contain no real credentials or infrastructure details.
