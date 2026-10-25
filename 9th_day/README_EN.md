# Ansible Day 9 | Error handling with block and rescue

[فارسی](README.md) · [Course index](../README.md) · [Official documentation](https://docs.ansible.com/projects/ansible-core/stable-2.22/playbook_guide/index.html)

> **The problem in one line:** Not every failure must stop a workflow, but recovery must be explicit and observable.

### The key idea
`block` holds primary tasks, `rescue` handles task failures, and `always` runs afterward.

### A small, executable example
```yaml
---
# Shared example: controlled failure and recovery.
- name: Recover from a task failure
  hosts: lab
  gather_facts: false
  vars:
    demo_ready: false
  tasks:
    - name: Demonstrate a controlled recovery
      block:
        - name: Check readiness
          ansible.builtin.assert:
            that: demo_ready | bool
            fail_msg: Demo is intentionally not ready.

        - name: Report success
          ansible.builtin.debug:
            msg: The normal path completed.
      rescue:
        - name: Explain fallback action
          ansible.builtin.debug:
            msg: A controlled failure was handled.
      always:
        - name: Report cleanup phase
          ansible.builtin.debug:
            msg: The final step always runs.
```

### Run and verify
```bash
ansible-playbook -i 9th_day/inventory.yml 9th_day/playbook.yml --syntax-check
ansible-playbook -i 9th_day/inventory.yml 9th_day/playbook.yml
```

**Expected outcome:** The rescue message is followed by the always message.

### Common trap
`rescue` does not necessarily recover unreachable hosts or syntax errors.

**One-minute experiment:** Use `-e demo_ready=true` to see the successful path.

<sub>Lab-only: no credentials, real infrastructure IPs, or admin privileges required.</sub>
