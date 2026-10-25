# Day 5 | Ansible Vault

[فارسی](README.md)

**Goal:** Encrypt variables without committing real passwords.

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

`secrets.yml` and `.vault_pass` are gitignored. No reusable sample credentials are stored in the repository.

> [!IMPORTANT]
> MIT is not permission to disclose secrets or third-party copyrighted work; publish only material you have rights to share.
