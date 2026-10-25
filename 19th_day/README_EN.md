# Ansible Day 19 | Security as code and file permissions

[فارسی](README.md) · [Course index](../README.md) · [Official documentation](https://docs.ansible.com/projects/ansible-core/stable-2.22/playbook_guide/index.html)

> **The problem in one line:** Security should be verifiable, for example by asserting a private file has mode `0600`.

### The key idea
`copy` enforces the desired state; `stat` plus `assert` verifies it.

### A small, executable example
```yaml
---
# Shared example: enforce and verify file permissions.
- name: Verify a lab-only private file
  hosts: lab
  gather_facts: false
  tasks:
    - name: Write a synthetic demo file with strict mode
      ansible.builtin.copy:
        dest: "{{ playbook_dir }}/demo-secret.txt"
        content: "synthetic-training-data-only\n"
        mode: '0600'
      no_log: true

    - name: Inspect file permissions
      ansible.builtin.stat:
        path: "{{ playbook_dir }}/demo-secret.txt"
      register: demo_file

    - name: Enforce the permission contract
      ansible.builtin.assert:
        that:
          - demo_file.stat.exists
          - demo_file.stat.mode == '0600'
```

### Run and verify
```bash
ansible-playbook -i 19th_day/inventory.yml 19th_day/playbook.yml --syntax-check
ansible-playbook -i 19th_day/inventory.yml 19th_day/playbook.yml
```

**Expected outcome:** The second identical run reports `changed=0`.

### Common trap
This uses synthetic data; encrypted files still require a real secret management policy.

**One-minute experiment:** Set the demo file mode to `0644` and observe the assertion fail.

<sub>Lab-only: no credentials, real infrastructure IPs, or admin privileges required.</sub>
