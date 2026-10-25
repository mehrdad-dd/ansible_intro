# Ansible Day 11 | Idempotency and check/diff mode

[فارسی](README.md) · [Course index](../README.md) · [Official documentation](https://docs.ansible.com/projects/ansible-core/stable-2.22/playbook_guide/index.html)

> **The problem in one line:** Good automation converges on the desired state; a second run should make no unnecessary changes.

### The key idea
`copy` detects differences; handlers run on change, and `--check --diff` previews work.

### A small, executable example
```yaml
---
# Shared example: convergent file management.
- name: Prove idempotent behavior
  hosts: lab
  gather_facts: false
  tasks:
    - name: Keep a predictable text file
      ansible.builtin.copy:
        dest: "{{ playbook_dir }}/demo-output.txt"
        content: "managed_by=ansible\n"
        mode: '0644'
      notify: Report file update

  handlers:
    - name: Report file update
      ansible.builtin.debug:
        msg: Content actually changed.
```

### Run and verify
```bash
ansible-playbook -i 11th_day/inventory.yml 11th_day/playbook.yml --syntax-check
ansible-playbook -i 11th_day/inventory.yml 11th_day/playbook.yml
```

**Expected outcome:** The second identical run reports `changed=0`.

### Common trap
`--check` is not a substitute for real tests; not all modules fully simulate changes.

**One-minute experiment:** Run twice; the second run should report `changed=0`.

<sub>Lab-only: no credentials, real infrastructure IPs, or admin privileges required.</sub>
