# Ansible Day 14 | Retry, until, and async jobs

[فارسی](README.md) · [Course index](../README.md) · [Official documentation](https://docs.ansible.com/projects/ansible-core/stable-2.22/playbook_guide/index.html)

> **The problem in one line:** Automation should wait for readiness deliberately instead of relying on arbitrary delays.

### The key idea
`until` repeats a check, `retries` bounds attempts, and `async` allows long-running jobs.

### A small, executable example
```yaml
---
# Shared example: bounded retries and a short async task.
- name: Wait and retry safely
  hosts: lab
  gather_facts: false
  tasks:
    - name: Retry a harmless readiness check
      ansible.builtin.command: /bin/true
      register: readiness
      changed_when: false
      until: readiness.rc == 0
      retries: 3
      delay: 1

    - name: Run a short asynchronous command
      ansible.builtin.command: /bin/sleep 1
      async: 10
      poll: 1
      changed_when: false
```

### Run and verify
```bash
ansible-playbook -i 14th_day/inventory.yml 14th_day/playbook.yml --syntax-check
ansible-playbook -i 14th_day/inventory.yml 14th_day/playbook.yml
```

**Expected outcome:** The playbook runs without privileged changes and displays a clear message or assertion.

### Common trap
Asynchronous tasks can behave differently in check mode; run this harmless example locally.

**One-minute experiment:** Change retries from 3 to 1; the successful command needs only one attempt.

<sub>Lab-only: no credentials, real infrastructure IPs, or admin privileges required.</sub>
