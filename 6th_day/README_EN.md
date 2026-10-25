# Ansible Day 6 | Inventory and variable precedence

[فارسی](README.md) · [Course index](../README.md) · [Official documentation](https://docs.ansible.com/projects/ansible-core/stable-2.22/playbook_guide/index.html)

> **The problem in one line:** An inventory is more than a list of IPs: it groups hosts and provides contextual variables.

### The key idea
`group_vars/lab.yml` applies to hosts in `lab`. `-e` has high precedence for intentional overrides.

### A small, executable example
```yaml
---
# Shared example: inventory, group_vars, variable precedence.
- name: Read lab inventory variables
  hosts: lab
  gather_facts: false
  tasks:
    - name: Explain effective settings
      ansible.builtin.debug:
        msg: "{{ inventory_hostname }} listens on {{ demo_port }} ({{ demo_region }})"

    - name: Validate chosen port
      ansible.builtin.assert:
        that:
          - demo_port | int > 0
          - demo_port | int < 65536
```

### Run and verify
```bash
ansible-playbook -i 6th_day/inventory.yml 6th_day/playbook.yml --syntax-check
ansible-playbook -i 6th_day/inventory.yml 6th_day/playbook.yml
```

**Expected outcome:** The playbook runs without privileged changes and displays a clear message or assertion.

### Common trap
Keep secrets out of public inventories; store sensitive values with Vault.

**One-minute experiment:** Run with `-e demo_port=9090` and observe the override.

<sub>Lab-only: no credentials, real infrastructure IPs, or admin privileges required.</sub>
