# روز 3 | مدیریت امن کاربران در Ansible

[English](README_EN.md) · [فهرست دوره](../README.md)

> **مسئله:** مدیریت کاربر باید قابل بازگشت باشد و دسترسی مدیریتی به سرور را قطع نکند.

### مدل ذهنی
`user` حساب را به وضعیت مطلوب می‌رساند و `register` خروجی دستور خواندنی `id` را نگه می‌دارد.

### کد مشترک و قابل اجرا
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

### نحوه اجرا
```bash
ansible-playbook -i 2nd_day/inventory.ini 3rd_day/user-security.yml --syntax-check
# Run only inside a disposable VM with sudo:
ansible-playbook -i 2nd_day/inventory.ini 3rd_day/user-security.yml --ask-become-pass
```

> [!WARNING]
> رمزها را داخل کد نگذار و بدون دسترسی کنسول، SSH یا sudo سرور واقعی را تغییر نده.

**تمرین یک دقیقه‌ای:** با `-e cleanup_demo_user=true` فقط حساب آزمایشی را حذف کن.

**نکته:** فایل‌های نمونه از رمز و اطلاعات زیرساخت واقعی استفاده نمی‌کنند.
