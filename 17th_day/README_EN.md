# Ansible Day 17 | Testing, assert, and executable contracts

[فارسی](README.md) · [Course index](../README.md) · [Official documentation](https://docs.ansible.com/projects/ansible-core/stable-2.22/playbook_guide/index.html)

> **The problem in one line:** A good test checks more than YAML syntax: it asserts an expected outcome.

### The key idea
`assert` expresses a contract; `changed_when: false` prevents read-only checks from reporting change.

### A small, executable example
```yaml
---
# Shared example: executable expectations.
- name: Validate a small configuration contract
  hosts: lab
  gather_facts: false
  vars:
    endpoint_port: 8080
  tasks:
    - name: Validate the TCP port range
      ansible.builtin.assert:
        that:
          - endpoint_port | int >= 1
          - endpoint_port | int <= 65535
        fail_msg: Port must be between 1 and 65535.

    - name: Show the validated value
      ansible.builtin.debug:
        msg: "Validated port: {{ endpoint_port }}"
```

### Run and verify
```bash
ansible-playbook -i 17th_day/inventory.yml 17th_day/playbook.yml --syntax-check
ansible-playbook -i 17th_day/inventory.yml 17th_day/playbook.yml
```

**Expected outcome:** The playbook runs without privileged changes and displays a clear message or assertion.

### Common trap
`--syntax-check` does not prove runtime correctness, safety, or idempotency.

**One-minute experiment:** Pass `-e endpoint_port=70000` to observe a deliberate assertion failure.

<sub>Lab-only: no credentials, real infrastructure IPs, or admin privileges required.</sub>
