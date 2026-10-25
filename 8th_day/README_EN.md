# Ansible Day 8 | Loops, filters, and data shaping

[فارسی](README.md) · [Course index](../README.md) · [Official documentation](https://docs.ansible.com/projects/ansible-core/stable-2.22/playbook_guide/index.html)

> **The problem in one line:** Normalize data before looping: sorting and removing duplicates make automation predictable.

### The key idea
`unique` removes duplicates, `sort` makes order deterministic, and `loop` iterates the resulting values.

### A small, executable example
```yaml
---
# Shared example: loop over normalized values.
- name: Iterate over clean data
  hosts: lab
  gather_facts: false
  vars:
    input_ports: [443, 8080, 443, 80]
  tasks:
    - name: Normalize the list
      ansible.builtin.set_fact:
        unique_ports: "{{ input_ports | unique | sort | list }}"

    - name: Show each unique port
      ansible.builtin.debug:
        msg: "Allowed demo port: {{ item }}"
      loop: "{{ unique_ports }}"

    - name: Verify deduplication
      ansible.builtin.assert:
        that: unique_ports | length == 3
```

### Run and verify
```bash
ansible-playbook -i 8th_day/inventory.yml 8th_day/playbook.yml --syntax-check
ansible-playbook -i 8th_day/inventory.yml 8th_day/playbook.yml
```

**Expected outcome:** The playbook runs without privileged changes and displays a clear message or assertion.

### Common trap
Sorting strings and numbers differs; be explicit about data types.

**One-minute experiment:** Add port 443 twice and see how many times it appears.

<sub>Lab-only: no credentials, real infrastructure IPs, or admin privileges required.</sub>
