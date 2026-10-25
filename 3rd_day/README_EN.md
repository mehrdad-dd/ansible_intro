# Ansible Day 3 | Safe user management

[فارسی](README.md) · [Course index](../README.md)

> **The problem:** User management should be reversible and must not disable access to your own server.

### Mental model
`user` converges to a desired account state. `register` captures the read-only `id` command output.

### Shared runnable example
```yaml
---
# Safe lab: create an unprivileged account without configuring SSH or sudo.
- name: Practice account management safely
  hosts: lab
  become: true
  vars:
    demo_user: ansible_demo
  tasks:
    - name: Create a demo user without password login
      ansible.builtin.user:
        name: "{{ demo_user }}"
        comment: Ansible training account
        shell: /usr/sbin/nologin
        create_home: false
        password_lock: true
        state: present

    - name: Inspect account entry
      ansible.builtin.command: "id {{ demo_user }}"
      changed_when: false
      register: account_result

    - name: Show account information
      ansible.builtin.debug:
        msg: "{{ account_result.stdout }}"

    - name: Remove the demo account only when requested
      ansible.builtin.user:
        name: "{{ demo_user }}"
        state: absent
        remove: false
      when: cleanup_demo_user | default(false) | bool
```

### How to run
```bash
ansible-playbook -i 2nd_day/inventory.ini 3rd_day/user-security.yml --syntax-check
# Run only inside a disposable VM with sudo:
ansible-playbook -i 2nd_day/inventory.ini 3rd_day/user-security.yml --ask-become-pass
```

> [!WARNING]
> Never hard-code passwords or experiment with SSH and sudo access on an inaccessible host.

**One-minute experiment:** Run with `-e cleanup_demo_user=true` to remove only the demo account.

**Note:** Samples contain no real credentials or infrastructure details.
