# روز چهارم | Roleهای قابل استفاده مجدد

[English](README_EN.md)

**هدف:** یک کار کوچک را از Playbook به `roles/nginx/tasks/main.yml` منتقل کنیم.

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
> Inventory پیش‌فرض فقط `localhost` را هدف می‌گیرد. اجرا با `become` روی سیستم محلی بسته و سرویس Nginx را تغییر می‌دهد؛ بهتر است از VM آزمایشی استفاده کنید.
