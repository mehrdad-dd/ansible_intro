# Ansible Day 7 | Facts and precise conditions

[فارسی](README.md) · [Course index](../README.md) · [Official documentation](https://docs.ansible.com/projects/ansible-core/stable-2.22/playbook_guide/index.html)

> **The problem in one line:** Facts describe the managed host. Conditions should depend on those facts instead of assumptions.

### The key idea
`gather_facts: true` gathers system metadata; `when` uses an unquoted Boolean expression, not `{{ }}`.

### A small, executable example
```yaml
---
# Shared example: host facts and conditions.
- name: Use facts for conditional behavior
  hosts: lab
  gather_facts: true
  tasks:
    - name: Show the detected operating system
      ansible.builtin.debug:
        msg: "{{ ansible_facts['distribution'] }} is in {{ ansible_facts['os_family'] }}"

    - name: Explain a Debian-specific task
      ansible.builtin.debug:
        msg: This branch would manage APT packages.
      when: ansible_facts['os_family'] == 'Debian'

    - name: Explain the fallback branch
      ansible.builtin.debug:
        msg: This host is not in the Debian family.
      when: ansible_facts['os_family'] != 'Debian'
```

### Run and verify
```bash
ansible-playbook -i 7th_day/inventory.yml 7th_day/playbook.yml --syntax-check
ansible-playbook -i 7th_day/inventory.yml 7th_day/playbook.yml
```

**Expected outcome:** The playbook runs without privileged changes and displays a clear message or assertion.

### Common trap
A distribution name is not the same as an OS family.

**One-minute experiment:** Inspect your host OS and the Debian condition.

<sub>Lab-only: no credentials, real infrastructure IPs, or admin privileges required.</sub>
