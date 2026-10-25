# Ansible Day 4 | Reusable Ansible roles

[فارسی](README.md) · [Course index](../README.md)

> **The problem:** A role packages related tasks so that a playbook can stay small.

### Mental model
The playbook declares `roles: [nginx]`; Ansible loads tasks from `roles/nginx/tasks/main.yml`.

### Shared runnable example
```yaml
---
# Minimal role demonstration; run against lab inventory only.
- name: Apply a small webserver role
  hosts: lab
  become: true
  roles:
    - nginx
```

**Role implementation:** [`roles/nginx/tasks/main.yml`](ansible-roles-demo/roles/nginx/tasks/main.yml)

### How to run
```bash
cd 4th_day/ansible-roles-demo
ansible-playbook -i inventory/lab/hosts.yml playbooks/site.yml --syntax-check
# Run only in a disposable Debian/Ubuntu VM:
ansible-playbook -i inventory/lab/hosts.yml playbooks/site.yml --ask-become-pass
```

> [!WARNING]
> The role installs Nginx; use only on a test VM. Its active config keeps SSH host-key checking enabled.

**One-minute experiment:** Add a read-only `debug` task to the role and re-run syntax checking.

**Note:** Samples contain no real credentials or infrastructure details.
