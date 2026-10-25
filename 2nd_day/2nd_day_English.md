# Ansible Day 2 | Files and Jinja2 templates

[فارسی](2nd_day_Persian.md) · [Course index](../README.md)

> **The problem:** A template separates data (variables) from configuration structure.

### Mental model
`template` renders Jinja2; `lineinfile` controls a single line, `blockinfile` manages a block, and `stat` inspects files.

### Shared runnable example
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

**Template:** [`app.conf.j2`](templates/app.conf.j2)

### How to run
```bash
ansible-playbook -i 2nd_day/inventory.ini 2nd_day/playbook.yml --syntax-check
# Run only inside a disposable Debian/Ubuntu VM:
ansible-playbook -i 2nd_day/inventory.ini 2nd_day/playbook.yml --ask-become-pass
```

> [!WARNING]
> This lesson writes to `/opt` and uses sudo; check mode may need pre-existing directories.

**One-minute experiment:** Change `app_port` and compare the rendered `app.conf` content.

**Note:** Samples contain no real credentials or infrastructure details.
