<div align="center">

# 🚀 Ansible Nginx Web Server Playbook

**A practical, beginner-friendly Ansible playbook to deploy Nginx, publish a custom welcome page, and inspect disk usage.**

![Ansible](https://img.shields.io/badge/Ansible-Automation-EE0000?style=for-the-badge&logo=ansible&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-Web_Server-009639?style=for-the-badge&logo=nginx&logoColor=white)
![YAML](https://img.shields.io/badge/YAML-Playbook-CB171E?style=for-the-badge&logo=yaml&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-Debian%20%7C%20Ubuntu-FCC624?style=for-the-badge&logo=linux&logoColor=black)

</div>

---

## 📖 Overview

This example demonstrates core Ansible concepts with a real-world Nginx deployment. It installs the web server, creates a host-specific HTML page, enables the service, installs useful tools, and reports disk usage.

> [!NOTE]
> This example is designed for **Debian/Ubuntu** hosts. Although `ansible.builtin.package` works with multiple package managers, the `www-data` account and `/var/www/html` path used here are not portable to every Linux distribution.

## ✨ Features

| Feature | Ansible concept |
| --- | --- |
| Refresh APT cache | Conditional execution with `when` |
| Install Nginx | Variables and `ansible.builtin.package` |
| Create a custom homepage | Jinja2 facts and `ansible.builtin.copy` |
| Keep Nginx running on boot | `ansible.builtin.service` |
| Install `curl`, `git`, and `htop` | `loop` |
| Inspect root disk usage | `register`, `changed_when`, and `debug` |
| Restart Nginx after homepage changes | Handlers and `notify` |

## 📁 Project structure

```text
ansible-nginx-demo/
├── README.md
├── inventory.ini
└── playbook.yml
```

## 🧰 Prerequisites

- Ansible installed on the control machine.
- SSH access to the target Debian/Ubuntu host(s).
- An account with `sudo` privileges on target hosts.
- Python available on the managed hosts.

## ⚙️ Inventory example

Create `inventory.ini` and replace the example address and username with your own:

```ini
[webservers]
web1 ansible_host=192.0.2.10 ansible_user=ubuntu
```

> [!TIP]
> `192.0.2.10` is a documentation-only example IP address. Use your actual server IP or DNS name.

## 📝 Playbook (`playbook.yml`)

The comments explain each part of the playbook so you can learn as you run it.

```yaml
---
# Each YAML document in Ansible starts with three dashes (optional but recommended).
# A playbook is a list of plays; this dash marks the beginning of a play.
- # The 'name' field describes what this play does.
  name: A simple playbook to demonstrate Ansible capabilities
  # 'hosts' defines which inventory hosts this play will run on; 'all' means every host in the inventory.
  hosts: all
  # 'become' elevates privileges (e.g., sudo) to perform system-level tasks.
  become: yes
  # 'vars' section defines variables used throughout the play.
  vars:
    # Variable 'web_package' holds the name of the package to install for the web server.
    web_package: nginx
    # Variable 'web_service' holds the name of the service we'll manage.
    web_service: nginx
    # Variable 'html_path' defines where the welcome page will be placed.
    html_path: /var/www/html/index.html
  # 'tasks' is a list of actions that Ansible will execute in order.
  tasks:
    # Task 1: Update the apt package cache on Debian-family systems.
    - name: Update apt cache (for Debian/Ubuntu)
      # 'ansible.builtin.apt' is the module that manages APT packages.
      ansible.builtin.apt:
        # 'update_cache' tells the module to run 'apt-get update' before proceeding.
        update_cache: yes
        # 'cache_valid_time' skips the update if the cache was refreshed within the given seconds.
        # Setting this parameter explicitly also implies 'update_cache=yes' (Ansible 2.4+).
        cache_valid_time: 3600
      # 'when' adds a conditional — this task runs only if the OS family is Debian.
      when: ansible_os_family == "Debian"

    # Task 2: Install the web server package using a generic package manager module.
    - name: Install the web server package
      # 'ansible.builtin.package' works across different package managers (apt, yum, dnf, etc.).
      # Note: this generic module does not support advanced options such as repository
      # management or cache updates; use OS-specific modules for those cases.
      ansible.builtin.package:
        # 'name' uses the variable defined above to determine which package to install.
        name: "{{ web_package }}"
        # 'state' set to 'present' ensures the package is installed (but not upgraded if already installed).
        state: present

    # Task 3: Copy a custom welcome page to the document root using the 'copy' module.
    - name: Create a custom index.html with hostname information
      # 'ansible.builtin.copy' copies a file or inline content to a remote location.
      ansible.builtin.copy:
        # 'content' defines the literal string to be written; it uses a Jinja2 template expression.
        content: |
          <h1>Welcome from {{ ansible_hostname }}</h1>
          <p>Served by Ansible</p>
        # 'dest' is the absolute path on the remote host where the content will be written.
        dest: "{{ html_path }}"
        # 'owner' sets the file owner.
        owner: www-data
        # 'group' sets the file group.
        group: www-data
        # 'mode' sets the file permissions (0644 = u+rw,g+r,o+r).
        mode: '0644'
      # 'notify' triggers a handler named 'restart web service' if this task changes something.
      notify: restart web service

    # Task 4: Ensure the web service is started and enabled at boot.
    - name: Start and enable the web service
      # 'ansible.builtin.service' manages services (start, stop, enable, etc.).
      ansible.builtin.service:
        # 'name' tells the module which service to manage.
        name: "{{ web_service }}"
        # 'state' set to 'started' ensures the service is running.
        # 'started' is idempotent: the start command is only issued if the service is not already running.
        state: started
        # 'enabled' set to yes configures the service to start at boot.
        enabled: yes

    # Task 5: Use a loop to install additional useful command-line tools.
    - name: Install several helpful packages using a loop
      # Using the same generic package module.
      ansible.builtin.package:
        # 'name' becomes the individual item from the loop.
        name: "{{ item }}"
        # Ensure each package is present.
        state: present
      # 'loop' iterates over a list, running the task once for each item.
      loop:
        - curl
        - git
        - htop

    # Task 6: Register the result of a command and display it with debug.
    - name: Check disk usage on the root filesystem
      # 'ansible.builtin.command' runs arbitrary commands on the remote host.
      ansible.builtin.command: df -h /
      # 'register' saves the full result of the task into a variable.
      register: disk_usage
      # 'changed_when' overrides the default change detection; set to false so the task never shows as 'changed'.
      # This is appropriate for read-only commands that gather information.
      changed_when: false

    - name: Display disk usage information
      # 'ansible.builtin.debug' prints messages during playbook execution.
      ansible.builtin.debug:
        # 'msg' specifies the message; here we access the 'stdout' attribute of the registered variable.
        msg: "Disk usage on /: {{ disk_usage.stdout_lines }}"

  # 'handlers' are special tasks that only run when notified by other tasks.
  handlers:
    # Handler name matches the string used in the 'notify' directive.
    - name: restart web service
      # Handler tasks use the same module syntax as regular tasks.
      ansible.builtin.service:
        name: "{{ web_service }}"
        # 'state' set to 'restarted' stops and then starts the service.
        # 'restarted' always performs the restart when the handler is triggered.
        state: restarted
```

## ▶️ Run the playbook

Save the YAML code above in `playbook.yml`. Then run:

```bash
# Test SSH connectivity
ansible all -i inventory.ini -m ping

# Validate playbook syntax
ansible-playbook -i inventory.ini playbook.yml --syntax-check

# Preview proposed changes (some modules have limited check-mode support)
ansible-playbook -i inventory.ini playbook.yml --check --diff

# Apply the playbook
ansible-playbook -i inventory.ini playbook.yml --ask-become-pass
```

> [!IMPORTANT]
> If your SSH user has passwordless sudo, omit `--ask-become-pass`. Ensure port **80/TCP** is allowed by the server firewall/security group if you want to access the site remotely.

## 🌐 Verify deployment

Replace the example IP with your server's address:

```bash
curl http://192.0.2.10/
```

Expected response (hostname varies):

```html
<h1>Welcome from web1</h1>
<p>Served by Ansible</p>
```

## 🧠 Key Ansible concepts

- **Idempotency:** Re-running most tasks leaves an already-correct system unchanged.
- **Facts:** `ansible_hostname` and `ansible_os_family` are discovered automatically when fact gathering is enabled (the default).
- **Variables:** `web_package`, `web_service`, and `html_path` centralize configuration.
- **Conditionals:** `when` restricts the APT cache task to Debian-family systems.
- **Handlers:** The restart handler runs only when notified by a changed task; handlers normally run near the end of a play.
- **Registered results:** `disk_usage.stdout_lines` exposes the output of `df -h /`.

## 🔧 Troubleshooting

| Problem | Suggested check |
| --- | --- |
| SSH connection fails | Confirm the inventory IP, username, SSH key, and port 22 access. |
| Sudo permission denied | Use a sudo-enabled account and supply the become password if needed. |
| Nginx page is unreachable | Check Nginx service status and port 80 firewall rules. |
| `www-data` user not found | Use a Debian/Ubuntu host or adapt ownership to your distribution. |
| Package installation fails | Check package repository connectivity and package names. |

## 📚 Further reading

- [Ansible documentation](https://docs.ansible.com/ansible/latest/)
- [Ansible playbooks](https://docs.ansible.com/ansible/latest/playbook_guide/index.html)
- [Ansible built-in modules](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/index.html)

---

<div align="center">

**Made for learning Ansible, one task at a time.** ⚡

</div>
