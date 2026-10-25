# Ansible Day 16 | Dynamic inventory with Python

[فارسی](README.md) · [Course index](../README.md) · [Official documentation](https://docs.ansible.com/projects/ansible-core/stable-2.22/playbook_guide/index.html)

> **The problem in one line:** When hosts change frequently, an executable inventory script can generate the host list on demand.

### The key idea
A dynamic inventory script returns JSON for `--list` and should have no side effects.

### A small, executable example
```yaml
---
# Shared example: consume a dynamic inventory.
- name: Use generated inventory groups
  hosts: lab
  gather_facts: false
  tasks:
    - name: Identify dynamically generated hosts
      ansible.builtin.debug:
        msg: "Dynamic inventory host: {{ inventory_hostname }}"
```

**Inventory script:** [`inventory.py`](inventory.py)

### Run and verify
```bash
ansible-playbook -i 16th_day/inventory.py 16th_day/playbook.yml --syntax-check
ansible-playbook -i 16th_day/inventory.py 16th_day/playbook.yml
```

**Expected outcome:** The playbook runs without privileged changes and displays a clear message or assertion.

### Common trap
Do not execute an untrusted inventory script or consume unvalidated external data.

**One-minute experiment:** Run `ansible-inventory -i inventory.py --graph`.

<sub>Lab-only: no credentials, real infrastructure IPs, or admin privileges required.</sub>
