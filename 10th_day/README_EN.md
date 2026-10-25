# Ansible Day 10 | Static imports vs dynamic includes

[فارسی](README.md) · [Course index](../README.md) · [Official documentation](https://docs.ansible.com/projects/ansible-core/stable-2.22/playbook_guide/index.html)

> **The problem in one line:** Split task files for clarity; imports are static, while includes are evaluated during execution.

### The key idea
`import_tasks` expands statically; `include_tasks` is evaluated at runtime.

### A small, executable example
```yaml
---
# Shared example: static and dynamic task inclusion.
- name: Reuse task files
  hosts: lab
  gather_facts: false
  vars:
    show_optional: true
  tasks:
    - name: Load tasks statically
      ansible.builtin.import_tasks: tasks/prepare.yml

    - name: Load optional tasks at runtime
      ansible.builtin.include_tasks: tasks/optional.yml
      when: show_optional | bool
```

**Task files:** [`prepare.yml`](tasks/prepare.yml) · [`optional.yml`](tasks/optional.yml)

### Run and verify
```bash
ansible-playbook -i 10th_day/inventory.yml 10th_day/playbook.yml --syntax-check
ansible-playbook -i 10th_day/inventory.yml 10th_day/playbook.yml
```

**Expected outcome:** The playbook runs without privileged changes and displays a clear message or assertion.

### Common trap
`--list-tasks` and tag selection behave differently for includes and imports.

**One-minute experiment:** Set `show_optional=false` with `-e` to skip the optional task.

<sub>Lab-only: no credentials, real infrastructure IPs, or admin privileges required.</sub>
