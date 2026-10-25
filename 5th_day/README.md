# روز پنجم | Ansible Vault

[English](README_EN.md)

**هدف:** یادگیری رمزگذاری متغیرها بدون گذاشتن رمز واقعی در مخزن.

```bash
# Create a new encrypted file; the editor asks you for a value.
ansible-vault create secrets.yml
# Read the encrypted file.
ansible-vault view secrets.yml
# Edit safely.
ansible-vault edit secrets.yml
# Run a playbook that uses Vault values (if configured).
ansible-playbook site.yml --ask-vault-pass
```

فایل‌های `secrets.yml` و `.vault_pass` در `.gitignore` هستند. هیچ رمز نمونه‌ای برای استفاده واقعی در مخزن نیست.

> [!IMPORTANT]
> MIT به معنی اجازه انتشار رمزها یا محتوای اشخاص ثالث نیست؛ فقط محتوایی را منتشر کنید که حق انتشار آن را دارید.
