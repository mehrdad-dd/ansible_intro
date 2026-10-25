# Ansible Day 12 | Secrets and no_log without leaks

[فارسی](README.md) · [Course index](../README.md) · [Official documentation](https://docs.ansible.com/projects/ansible-core/stable-2.22/playbook_guide/index.html)

> **The problem in one line:** Hiding task output is not secret management; the secret must never be committed to Git.

### The key idea
The environment lookup checks whether a value exists without displaying or storing the value.

### A small, executable example
```yaml
---
# Shared example: avoid exposing a secret's contents.
- name: Check secret availability safely
  hosts: lab
  gather_facts: false
  tasks:
    - name: Detect whether an environment token exists
      ansible.builtin.set_fact:
        demo_token_provided: "{{ (lookup('ansible.builtin.env', 'ANSIBLE_DEMO_TOKEN') | length) > 0 }}"
      no_log: true

    - name: Report only a Boolean status
      ansible.builtin.debug:
        msg: "Example token configured: {{ demo_token_provided | bool }}"
```

### Run and verify
```bash
ansible-playbook -i 12th_day/inventory.yml 12th_day/playbook.yml --syntax-check
ansible-playbook -i 12th_day/inventory.yml 12th_day/playbook.yml
```

**Expected outcome:** The playbook runs without privileged changes and displays a clear message or assertion.

### Common trap
`no_log` is not encryption; use Vault for files and repository secrets for CI.

**One-minute experiment:** Set a dummy environment variable and observe only the Boolean output.

<sub>Lab-only: no credentials, real infrastructure IPs, or admin privileges required.</sub>
