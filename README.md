# Ansible Capabilities Demonstration Playbook

<img src="https://img.shields.io/badge/ansible-2.9+-blue.svg" alt="Ansible Version">
<img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License">
<img src="https://img.shields.io/badge/platform-linux-lightgrey.svg" alt="Platform">

A simple, well-documented Ansible playbook designed to illustrate fundamental Ansible concepts through a practical example: deploying and configuring an Nginx web server.

---

## 📋 Table of Contents
- [Overview](#overview)
- [Features Demonstrated](#features-demonstrated)
- [Playbook Workflow](#playbook-workflow)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Example Output](#example-output)
- [Playbook Structure Explained](#playbook-structure-explained)
- [Key Ansible Concepts Covered](#key-ansible-concepts-covered)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## 🚀 Overview

| **Attribute**       | **Details**                         |
|----------------------|-------------------------------------|
| **Purpose**         | Showcase core Ansible features      |
| **Target Audience** | Ansible beginners / intermediate    |
| **Demo Application**| Nginx web server                    |
| **Supported OS**    | Debian/Ubuntu, RHEL/CentOS (partial)|

This project provides a practical, step-by-step introduction to Ansible automation. By running a single playbook, you will see how Ansible handles package management, service control, file deployment, dynamic templating, conditionals, loops, variable registration, and event-driven handlers.

---

## ✨ Features Demonstrated

- ✅ **Idempotency** – Tasks only make changes when necessary
- ✅ **Multi-OS Package Management** – Generic `package` module works across different Linux families
- ✅ **Privilege Escalation** – Using `become: yes` for system-level operations
- ✅ **Variables** – Centralized configuration values
- ✅ **Jinja2 Templating** – Dynamic content generation with host-specific data
- ✅ **Conditionals** – OS-specific task execution via `when`
- ✅ **Loops** – Installing multiple packages with a single task
- ✅ **Registering Output** – Capturing and displaying command results
- ✅ **Handlers & Notifications** – Triggering service restart only when configuration changes
- ✅ **File Management** – Setting ownership, group, and permissions
- ✅ **Service Management** – Starting and enabling services at boot
- ✅ **Debug Output** – Real-time visibility into playbook execution

---

## 🔄 Playbook Workflow

```mermaid
graph TD
    A[Start] --> B[Update apt cache<br>Debian only]
    B --> C[Install Nginx]
    C --> D[Deploy custom index.html]
    D --> E[Start & enable Nginx]
    E --> F[Install additional tools<br>curl, git, htop]
    F --> G[Check disk usage]
    G --> H[Display disk info]
    D -.->|Notify: if changed| I[Restart Nginx Handler]
    I --> H
    H --> J[End]
