# Ansible Day 5 | Vault and secret handling

[فارسی](README.md) · [Course index](../README.md)

> **The problem:** Passwords and tokens must not end up in Git or CI output.

### Mental model
**Vault encrypts stored content;** `no_log` suppresses task output. They solve different problems.

### Shared executable example
```yaml
---
# Shared example: no_log hides output, but does not encrypt values.
- name: Demonstrate non-sensitive logging behavior
  hosts: lab
  gather_facts: false
  vars:
    synthetic_value: training-example-only
  tasks:
    - name: Suppress task output for a synthetic value
      ansible.builtin.debug:
        msg: "{{ synthetic_value }}"
      no_log: true

    - name: Explain the limitation
      ansible.builtin.debug:
        msg: Use Ansible Vault for secrets stored on disk.
```

### Vault commands and checks
```bash
ansible-vault create secrets.yml
ansible-vault view secrets.yml
ansible-vault edit secrets.yml
# The file secrets.yml is ignored by Git and must never be committed.
ansible-playbook -i 5th_day/inventory.ini 5th_day/playbook.yml --syntax-check
ansible-playbook -i 5th_day/inventory.ini 5th_day/playbook.yml
```

> [!IMPORTANT]
> Keep the Vault password secure and outside the repository. `secrets.yml` and `.vault_pass` are gitignored; never publish working credentials.

**One-minute experiment:** Create a Vault with synthetic text and inspect it with `view`; do not commit actual secrets.
