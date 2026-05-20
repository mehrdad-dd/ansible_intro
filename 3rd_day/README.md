# 🔐 Ansible Learning Path - Stage 3: User Management & Security Hardening

[![Ansible](https://img.shields.io/badge/Ansible-2.9+-blue?logo=ansible)](https://www.ansible.com/)
[![Security](https://img.shields.io/badge/Focus-Security-red)](https://github.com/your-username/ansible-learning-path)
[![Difficulty](https://img.shields.io/badge/Difficulty-Intermediate-yellow)]()
[![Stage](https://img.shields.io/badge/Stage-3%20of%207-purple)]()

> **Master Linux security automation with Ansible**  
> Learn user lifecycle management, SSH hardening, firewall configuration, and compliance auditing

---

## 🎯 What You'll Learn

| # | Skill | Module(s) Used | Real-World Application |
|---|-------|---------------|----------------------|
| 1 | **User Lifecycle Management** | `user`, `group` | Onboarding/offboarding automation |
| 2 | **SSH Key Distribution** | `authorized_key`, `openssh_keypair` | Secure access management |
| 3 | **Sudo Privilege Management** | `template` + validation | Granular command access |
| 4 | **SSH Server Hardening** | `lineinfile` + validation | Security best practices |
| 5 | **Password Policy Enforcement** | `lineinfile` (PAM, login.defs) | Compliance requirements |
| 6 | **Firewall Configuration** | `ufw` | Network security |
| 7 | **Security Auditing** | `shell` + `debug` | Compliance verification |

---

## 📊 Playbook Architecture

```mermaid
graph TB
    subgraph "Phase 1: Foundation"
        A[Groups] --> B[Users]
    end
    
    subgraph "Phase 2: Access Control"
        C[SSH Keys] --> D[Sudo Rules]
        D --> E[SSH Hardening]
    end
    
    subgraph "Phase 3: Security Policies"
        F[Password Policies] --> G[Firewall Rules]
    end
    
    subgraph "Phase 4: Audit"
        H[SUID Scan] --> I[UID Zero Check]
        I --> J[Password Audit]
        J --> K[Security Report]
    end
    
    B --> C
    E --> F
    G --> H
    K --> L[✅ Complete]
    
    style A fill:#e1f5fe
    style B fill:#e1f5fe
    style C fill:#fff3e0
    style D fill:#fff3e0
    style E fill:#fff3e0
    style F fill:#f3e5f5
    style G fill:#f3e5f5
    style H fill:#e8f5e9
    style I fill:#e8f5e9
    style J fill:#e8f5e9
    style K fill:#e8f5e9
