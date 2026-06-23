# 🏗️ Ansible Learning Path - Stage 4: Professional Roles & Project Structure

[![Ansible](https://img.shields.io/badge/Ansible-2.9+-blue?logo=ansible&logoColor=white)](https://www.ansible.com/)
[![Best Practices](https://img.shields.io/badge/Best%20Practices-✓-brightgreen)]()
[![Difficulty](https://img.shields.io/badge/Difficulty-Advanced-red)]()
[![Stage](https://img.shields.io/badge/Stage-4%20of%207-purple)]()

> **Master Ansible Roles for enterprise-grade infrastructure automation**  
> Build reusable, maintainable, and scalable automation code

---

## 🎯 What You'll Learn

| # | Skill | Key Concepts |
|---|-------|-------------|
| 1 | **Role Structure** | Standard directory layout, file organization |
| 2 | **Role Dependencies** | Meta dependencies, role composition |
| 3 | **Variable Precedence** | defaults < vars < inventory < host_vars < extra_vars |
| 4 | **Task Modularization** | `include_tasks`, `import_tasks`, dynamic includes |
| 5 | **Role Reusability** | Parameterized roles, Galaxy integration |
| 6 | **Multi-Environment** | Production, staging, development configurations |
| 7 | **Best Practices** | Tags, handlers, validation, testing |

---

## 📐 Project Architecture

```mermaid
graph TB
    subgraph "Playbook Layer"
        SITE[site.yml<br/>Main Orchestrator]
    end
    
    subgraph "Role Layer"
        COMMON[Common Role<br/>Base Configuration]
        NGINX[Nginx Role<br/>Web Server]
        PHP[PHP Role<br/>Application Server]
        MYSQL[MySQL Role<br/>Database]
        NODEJS[Node.js Role<br/>App Runtime]
    end
    
    subgraph "Inventory Layer"
        ALL[Group: all]
        WEB[Group: webservers]
        DB[Group: dbservers]
        MON[Group: monitoring]
    end
    
    SITE --> ALL
    SITE --> WEB
    SITE --> DB
    SITE --> MON
    
    ALL --> COMMON
    WEB --> NGINX
    WEB --> PHP
    WEB --> NODEJS
    DB --> MYSQL
    
    NGINX -.->|depends on| COMMON
    PHP -.->|depends on| COMMON
    MYSQL -.->|depends on| COMMON
    NODEJS -.->|depends on| COMMON
    
    style SITE fill:#e1f5fe,stroke:#01579b,stroke-width:3px
    style COMMON fill:#f3e5f5,stroke:#4a148c
    style NGINX fill:#fff3e0,stroke:#e65100
    style PHP fill:#e8f5e9,stroke:#1b5e20
    style MYSQL fill:#fce4ec,stroke:#880e4f
    style NODEJS fill:#fff9c4,stroke:#f57f17
