# روز پنجم | Ansible Vault و حفاظت از Secrets

[English](README_EN.md) · [فهرست دوره](../README.md)

> **مسئله:** رمز یا Token نباید به‌صورت خوانا وارد Git و لاگ CI شود.

### مدل ذهنی
**Vault داده را در حالت ذخیره رمز می‌کند؛** `no_log` فقط خروجی Task را می‌پوشاند. این دو جایگزین یکدیگر نیستند.

### کد کوتاه و مشترک
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

### دستورات Vault و تست
```bash
ansible-vault create secrets.yml
ansible-vault view secrets.yml
ansible-vault edit secrets.yml
# The file secrets.yml is ignored by Git and must never be committed.
ansible-playbook -i 5th_day/inventory.ini 5th_day/playbook.yml --syntax-check
ansible-playbook -i 5th_day/inventory.ini 5th_day/playbook.yml
```

> [!IMPORTANT]
> برای رمز واقعی از یک Vault Password امن و خارج از مخزن استفاده کن. `secrets.yml` و `.vault_pass` در `.gitignore` هستند؛ حتی رمز آزمایشی را به‌صورت کلید واقعی منتشر نکن.

**تمرین یک دقیقه‌ای:** یک Vault با متن ساختگی بساز و `view` را تست کن؛ هیچ فایل رمزگذاری‌شده واقعی را commit نکن.
