# Ansible Day 18 | Performance, serial, and throttle

[فارسی](README.md) · [Course index](../README.md) · [Official documentation](https://docs.ansible.com/projects/ansible-core/stable-2.22/playbook_guide/index.html)

> **The problem in one line:** Fast is not always safe. Limit how many hosts are changed concurrently.

### The key idea
`serial: 1` processes one host per batch; `throttle` caps per-task concurrency.

### A small, executable example
```yaml
---
# Shared example: intentionally bounded concurrency.
- name: Configure hosts in small batches
  hosts: lab
  gather_facts: false
  serial: 1
  strategy: linear
  tasks:
    - name: Show current rollout host
      ansible.builtin.debug:
        msg: "Working on {{ inventory_hostname }}"
      throttle: 1
```

### Run and verify
```bash
ansible-playbook -i 18th_day/inventory.yml 18th_day/playbook.yml --syntax-check
ansible-playbook -i 18th_day/inventory.yml 18th_day/playbook.yml
```

**Expected outcome:** The playbook runs without privileged changes and displays a clear message or assertion.

### Common trap
With `serial`, `run_once` means once per batch, not necessarily once globally.

**One-minute experiment:** Try `serial: 2` and compare batches.

<sub>Lab-only: no credentials, real infrastructure IPs, or admin privileges required.</sub>
