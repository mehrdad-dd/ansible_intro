# Ansible Day 15 | Collections, Galaxy, and FQCN

[فارسی](README.md) · [Course index](../README.md) · [Official documentation](https://docs.ansible.com/projects/ansible-core/stable-2.22/playbook_guide/index.html)

> **The problem in one line:** Modules belong to collections; fully qualified names reduce ambiguity and hidden dependencies.

### The key idea
`ansible.builtin.debug` is an FQCN. External collections should declare version ranges in `requirements.yml`.

### A small, executable example
```yaml
---
# Shared example: use unambiguous built-in module names.
- name: Explain collections and module namespaces
  hosts: lab
  gather_facts: false
  tasks:
    - name: Use a fully qualified module name
      ansible.builtin.debug:
        msg: "Module namespace: ansible.builtin"

    - name: Verify collection metadata example
      ansible.builtin.assert:
        that: "'ansible.builtin.debug'.startswith('ansible.builtin')"
```

**Optional dependency:** [`requirements.yml`](requirements.yml)

### Run and verify
```bash
ansible-playbook -i 15th_day/inventory.yml 15th_day/playbook.yml --syntax-check
ansible-playbook -i 15th_day/inventory.yml 15th_day/playbook.yml
```

**Expected outcome:** The playbook runs without privileged changes and displays a clear message or assertion.

### Common trap
A `requirements.yml` file does not install itself; install vetted collections explicitly.

**One-minute experiment:** Run `ansible-galaxy collection list` and distinguish builtin from external collections.

<sub>Lab-only: no credentials, real infrastructure IPs, or admin privileges required.</sub>
