# روز 4 | Roleهای قابل استفاده مجدد در Ansible

[English](README_EN.md) · [فهرست دوره](../README.md)

> **مسئله:** Role کارهای مرتبط را در یک ساختار جدا جمع می‌کند تا Playbook کوتاه بماند.

### مدل ذهنی
Playbook نام `nginx` را در `roles` می‌آورد و Ansible وظایف `roles/nginx/tasks/main.yml` را بار می‌کند.

### کد مشترک و قابل اجرا
```yaml
---
# Minimal role demonstration; run against lab inventory only.
- name: Apply a small webserver role
  hosts: lab
  become: true
  roles:
    - nginx
```

**محتوای Role:** [`roles/nginx/tasks/main.yml`](ansible-roles-demo/roles/nginx/tasks/main.yml)

### نحوه اجرا
```bash
cd 4th_day/ansible-roles-demo
ansible-playbook -i inventory/lab/hosts.yml playbooks/site.yml --syntax-check
# Run only in a disposable Debian/Ubuntu VM:
ansible-playbook -i inventory/lab/hosts.yml playbooks/site.yml --ask-become-pass
```

> [!WARNING]
> این Role وب‌سرور نصب می‌کند؛ فقط روی VM آزمایشی اجرا کن. بررسی SSH host key در تنظیمات فعال است.

**تمرین یک دقیقه‌ای:** یک Task ساده `debug` به Role اضافه کن و دوباره Syntax را بررسی کن.

**نکته:** فایل‌های نمونه از رمز و اطلاعات زیرساخت واقعی استفاده نمی‌کنند.
