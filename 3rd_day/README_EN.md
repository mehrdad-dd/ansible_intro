# Day 3 | Users and Security

[فارسی](README.md)

**Goal:** Learn `user`, `register`, and `when` without modifying SSH, firewall, or sudo access.

**Safety:** Changing SSH or UFW on remote hosts can lock you out; practice hardening separately with console access.

```bash
ansible-playbook -i ../2nd_day/inventory.ini user-security.yml --syntax-check
ansible-playbook -i ../2nd_day/inventory.ini user-security.yml --check --diff
ansible-playbook -i ../2nd_day/inventory.ini user-security.yml --ask-become-pass
# Optional cleanup:
ansible-playbook -i ../2nd_day/inventory.ini user-security.yml -e cleanup_demo_user=true --ask-become-pass
```

**Remember:** Never commit passwords or private keys; use `ansible-vault` for secrets; verify a recovery path before security changes.
