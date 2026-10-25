# Day 4 | Reusable Roles

[فارسی](README.md)

**Goal:** Move a small repeatable task into `roles/nginx/tasks/main.yml`.

```text
ansible-roles-demo/
├── ansible.cfg
├── inventory/lab/hosts.yml
├── playbooks/site.yml
└── roles/nginx/tasks/main.yml
```

```bash
cd 4th_day/ansible-roles-demo
ansible-playbook playbooks/site.yml --syntax-check
ansible-playbook playbooks/site.yml --check --diff
ansible-playbook playbooks/site.yml --ask-become-pass
```

> [!WARNING]
> The default inventory targets `localhost`. With `become`, this changes local Nginx packages and services; use a disposable VM.
