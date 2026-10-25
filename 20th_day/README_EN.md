# Ansible Day 20 | Capstone: a small configuration pipeline

[فارسی](README.md) · [Course index](../README.md) · [Official documentation](https://docs.ansible.com/projects/ansible-core/stable-2.22/playbook_guide/index.html)

> **The problem in one line:** Real automation ties inventory, variables, templates, validation, and handlers into one predictable flow.

### The key idea
Jinja2 renders configuration, `stat` checks it, and a handler signals only real changes.

### A small, executable example
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

**Related template:** [`templates/service.conf.j2`](templates/service.conf.j2)

### Run and verify
```bash
ansible-playbook -i 20th_day/inventory.yml 20th_day/playbook.yml --syntax-check
ansible-playbook -i 20th_day/inventory.yml 20th_day/playbook.yml
```

**Expected outcome:** The second identical run reports `changed=0`.

### Common trap
The lab handler reports only; production reloads should follow real service validation.

**One-minute experiment:** Change `service_port` and compare first, second, and modified runs.

<sub>Lab-only: no credentials, real infrastructure IPs, or admin privileges required.</sub>
