# Ansible Day 13 | Delegation and run_once

[فارسی](README.md) · [Course index](../README.md) · [Official documentation](https://docs.ansible.com/projects/ansible-core/stable-2.22/playbook_guide/index.html)

> **The problem in one line:** Sometimes a task relates to several hosts but should execute on the controller only.

### The key idea
`delegate_to: localhost` changes execution location; `run_once` runs once per play batch when serial is used.

### A small, executable example
```yaml
---
# Shared example: delegate one task to the controller.
- name: Delegate centrally, report per host
  hosts: lab
  gather_facts: false
  tasks:
    - name: Perform one central check
      ansible.builtin.debug:
        msg: Checked centrally on the control node.
      delegate_to: localhost
      run_once: true

    - name: Report each inventory host
      ansible.builtin.debug:
        msg: "Current inventory host: {{ inventory_hostname }}"
```

### Run and verify
```bash
ansible-playbook -i 13th_day/inventory.yml 13th_day/playbook.yml --syntax-check
ansible-playbook -i 13th_day/inventory.yml 13th_day/playbook.yml
```

**Expected outcome:** The playbook runs without privileged changes and displays a clear message or assertion.

### Common trap
`inventory_hostname` does not necessarily identify the machine that executed a delegated task.

**One-minute experiment:** Two local aliases simulate hosts; compare how often the tasks run.

<sub>Lab-only: no credentials, real infrastructure IPs, or admin privileges required.</sub>
