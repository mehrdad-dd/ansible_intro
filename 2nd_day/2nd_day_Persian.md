<div align="center">

# 📁 Ansible · Day 2

**Advanced File Management · Jinja2 Templates · Configuration & Backups**

![Ansible](https://img.shields.io/badge/Ansible-Automation-EE0000?style=for-the-badge&logo=ansible&logoColor=white) ![YAML](https://img.shields.io/badge/YAML-Playbook-CB171E?style=for-the-badge&logo=yaml&logoColor=white) ![Nginx](https://img.shields.io/badge/Nginx-HTTP_Proxy-009639?style=for-the-badge&logo=nginx&logoColor=white) ![MIT](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

</div>

---

## 📖 معرفی پروژه

این پروژه، بازنویسی و بازنگری **آموزش روز دوم Ansible** بر اساس کد ارسالی است. هدف، تمرین مدیریت فایل‌ها و پوشه‌ها، قالب‌های Jinja2، تنظیمات Nginx، نسخه پشتیبان، بررسی وضعیت فایل‌ها و Handlerها در یک محیط آزمایشی **Debian/Ubuntu** است.

> [!IMPORTANT]
> ابتدا روی ماشین مجازی آزمایشی اجرا کنید. این Playbook فایل‌های `/etc/hosts` و `/etc/security/limits.conf` و تنظیمات Nginx را تغییر می‌دهد. دامنه‌ها و پورت‌ها نمونه‌اند. این پروژه فقط **HTTP** را پیکربندی می‌کند و برای HTTPS عملیاتی آماده نیست.

## 🔧 اصلاحات انجام‌شده

| موضوع در کد اولیه | اصلاح در نسخه جدید |
| --- | --- |
| فایل‌های Jinja2 ارائه نشده بودند | سه قالب واقعی به پروژه اضافه شد |
| استفاده از `ansible.builtin.archive` | استفاده صحیح از `community.general.archive` به همراه فایل وابستگی |
| ساخت Virtual Host بدون فعال‌سازی | ایجاد لینک در `sites-enabled` |
| ترتیب اعتبارسنجی و Reload مشکل‌ساز بود | اجرای `nginx -t` پیش از Reload در Handler |
| امکان پنهان شدن خطای Nginx | حذف شرط خطای نامناسب و توقف در صورت خطا |
| پاکسازی Backup با Shell و تشخیص تغییر نادرست | استفاده از `find` و `file` |
| گواهی خودامضا بدون تنظیم HTTPS در Nginx | تبدیل به بررسی آموزشی وجود گواهی |
| تنظیمات نمونه غیرقابل اتکا | شفاف‌سازی محدودیت‌های دامنه‌ها و سرویس‌های نمونه |

## 📁 ساختار پروژه

```text
 day2_ansible/
 ├── README_EN.md
 ├── README_FA.md
 ├── playbook.yml
 ├── inventory.ini
 ├── requirements.yml
 ├── templates/
 │   ├── app_config.yml.j2
 │   ├── environment.sh.j2
 │   └── nginx_vhost.conf.j2
 └── files/scripts/healthcheck.sh
```

## 🧰 پیش‌نیازها و اجرای پروژه

روی سیستم کنترل‌کننده Ansible نصب باشد؛ سرور هدف Debian/Ubuntu، دسترسی SSH و مجوز sudo داشته باشد. ابتدا آدرس سرور آزمایشی را در `inventory.ini` وارد کنید.

```bash
ansible-galaxy collection install -r requirements.yml
ansible -i inventory.ini staging -m ping
ansible-playbook -i inventory.ini playbook.yml --syntax-check
ansible-playbook -i inventory.ini playbook.yml --check --diff
ansible-playbook -i inventory.ini playbook.yml --ask-become-pass
```

> [!NOTE]
> گزینه `--ask-become-pass` فقط وقتی لازم است که sudo رمز عبور بخواهد. اجرای `--check` ممکن است روی سیستم کاملاً خام، به دلیل نبود فایل‌ها و پوشه‌های موردنیاز، خطا دهد.

> [!WARNING]
> پیکربندی Nginx درخواست‌ها را به پورت‌های `3000`، `3001` و `3002` می‌فرستد، اما این آموزش خودِ برنامه‌های پشت این پورت‌ها را نصب نمی‌کند؛ بنابراین پاسخ `502 Bad Gateway` تا زمان اجرای برنامه‌ها طبیعی است.

## 🧠 سرفصل‌های آموزشی

| بخش | ماژول‌ها و مفاهیم |
| --- | --- |
| ۱ · ساخت پوشه‌ها | `file`، `loop`، مجوزها و `default` |
| ۲ · قالب‌ها | `template`، شرط و حلقه Jinja2 و `notify` |
| ۳ · ویرایش و انتقال فایل | `lineinfile`، `blockinfile`، `copy`، `fetch` |
| ۴ · بررسی وضعیت | `stat`، `register`، `debug` |
| ۵ · نسخه پشتیبان | `community.general.archive`، `find`، `file` |
| ۶ · اعتبارسنجی | `nginx -t`، `changed_when`، Handler و `service` |

## 💻 کد کامل و بازنگری‌شده (`playbook.yml`)

```yaml
---
- name: "Day 2 | Advanced file and template management"
  hosts: all
  become: true
  gather_facts: true

  vars:
    app_name: MyWebApp
    app_version: '2.1.0'
    app_environment: staging
    app_user: www-data
    app_group: www-data
    base_path: "/opt/{{ app_name }}"
    config_path: "{{ base_path }}/config"
    log_path: "/var/log/{{ app_name }}"
    data_path: "/var/lib/{{ app_name }}"
    backup_enabled: true
    backup_retention_days: 7
    database:
      host: db.internal.local
      port: 5432
      name: "{{ app_name }}_db"
      pool_size: 25
    redis:
      host: redis.internal.local
      port: 6379
    features:
      caching: true
      compression: true
      monitoring: true
    env_configs:
      development: { debug_mode: true, log_level: DEBUG }
      staging: { debug_mode: false, log_level: INFO }
      production: { debug_mode: false, log_level: WARN }
    nginx_configs:
      - { domain: example.com, upstream_port: 3000 }
      - { domain: api.example.com, upstream_port: 3001 }
      - { domain: admin.example.com, upstream_port: 3002 }

  pre_tasks:
    - name: Check supported operating system
      ansible.builtin.assert:
        that: ansible_facts['os_family'] == 'Debian'
        fail_msg: 'This lab targets Debian/Ubuntu only.'

    - name: Install required packages
      ansible.builtin.apt:
        name: [nginx, python3, curl]
        state: present
        update_cache: true
        cache_valid_time: 3600

  tasks:
    # GROUP 1: Directory management
    - name: Create application directories
      ansible.builtin.file:
        path: "{{ item.path }}"
        state: directory
        owner: "{{ item.owner | default('root') }}"
        group: "{{ item.group | default('root') }}"
        mode: "{{ item.mode | default('0755') }}"
      loop:
        - { path: "{{ base_path }}", owner: www-data, group: www-data }
        - { path: "{{ config_path }}", owner: www-data, group: www-data, mode: '0750' }
        - { path: "{{ log_path }}", owner: www-data, group: www-data, mode: '0750' }
        - { path: "{{ data_path }}", owner: www-data, group: www-data, mode: '0750' }
        - { path: "{{ base_path }}/backups", mode: '0750' }
        - { path: "{{ base_path }}/scripts", mode: '0755' }
      loop_control:
        label: "{{ item.path }}"
      tags: [files]

    # GROUP 2: Jinja2 templates
    - name: Render application YAML configuration
      ansible.builtin.template:
        src: templates/app_config.yml.j2
        dest: "{{ config_path }}/app_config.yml"
        owner: "{{ app_user }}"
        group: "{{ app_group }}"
        mode: '0640'
        backup: "{{ backup_enabled }}"
      tags: [config, templates]

    - name: Render environment shell configuration
      ansible.builtin.template:
        src: templates/environment.sh.j2
        dest: "{{ config_path }}/environment.sh"
        owner: "{{ app_user }}"
        group: "{{ app_group }}"
        mode: '0640'
      tags: [config, templates]

    - name: Render HTTP Nginx virtual hosts
      ansible.builtin.template:
        src: templates/nginx_vhost.conf.j2
        dest: "/etc/nginx/sites-available/{{ item.domain }}.conf"
        owner: root
        group: root
        mode: '0644'
        backup: true
      loop: "{{ nginx_configs }}"
      loop_control:
        label: "{{ item.domain }}"
      notify: validate and reload nginx
      tags: [nginx, templates]

    - name: Enable Nginx virtual hosts
      ansible.builtin.file:
        src: "/etc/nginx/sites-available/{{ item.domain }}.conf"
        dest: "/etc/nginx/sites-enabled/{{ item.domain }}.conf"
        state: link
      loop: "{{ nginx_configs }}"
      loop_control:
        label: "{{ item.domain }}"
      notify: validate and reload nginx
      tags: [nginx]

    # GROUP 3: Controlled edits and file transfers
    - name: Configure open-file limits for application user
      ansible.builtin.lineinfile:
        path: /etc/security/limits.conf
        regexp: '^www-data\s+soft\s+nofile\s+'
        line: 'www-data soft nofile 65535'
        backup: true
      tags: [files, security]

    - name: Insert a managed block in hosts file
      ansible.builtin.blockinfile:
        path: /etc/hosts
        marker: '# {mark} ANSIBLE MANAGED {{ app_name }}'
        block: |
          10.0.1.100 monitoring.local
        backup: true
      tags: [files, networking]

    - name: Copy sample maintenance script
      ansible.builtin.copy:
        src: files/scripts/healthcheck.sh
        dest: "{{ base_path }}/scripts/healthcheck.sh"
        owner: root
        group: "{{ app_group }}"
        mode: '0755'
      tags: [files, scripts]

    - name: Check remote system log presence
      ansible.builtin.stat:
        path: /var/log/syslog
      register: syslog_stat
      tags: [logs]

    - name: Fetch system log when present
      ansible.builtin.fetch:
        src: /var/log/syslog
        dest: fetched_logs/
        flat: false
      when: syslog_stat.stat.exists
      tags: [logs]

    # GROUP 4: File state checks
    - name: Check whether an application TLS certificate exists
      ansible.builtin.stat:
        path: "{{ base_path }}/ssl/server.crt"
      register: tls_certificate
      tags: [ssl, check]

    - name: Report TLS certificate state
      ansible.builtin.debug:
        msg: "Certificate exists: {{ tls_certificate.stat.exists }} (TLS is not configured by this HTTP-only demo)."
      tags: [ssl, check]

    # GROUP 5: Backups and metadata
    - name: Create configuration backup archive
      community.general.archive:
        path: "{{ config_path }}"
        dest: "{{ base_path }}/backups/config_{{ ansible_date_time.date }}.tar.gz"
        format: gz
        owner: root
        group: root
        mode: '0640'
      when: backup_enabled
      tags: [backup]

    - name: Find old configuration backups
      ansible.builtin.find:
        paths: "{{ base_path }}/backups"
        patterns: 'config_*.tar.gz'
        age: "{{ backup_retention_days }}d"
        file_type: file
      register: old_backups
      when: backup_enabled
      tags: [backup]

    - name: Delete old configuration backups
      ansible.builtin.file:
        path: "{{ item.path }}"
        state: absent
      loop: "{{ old_backups.files | default([]) }}"
      loop_control:
        label: "{{ item.path }}"
      when: backup_enabled
      tags: [backup]

    - name: Write application deployment information
      ansible.builtin.copy:
        content: |
          {{ app_name }} v{{ app_version }}
          Environment: {{ app_environment }}
          Host: {{ ansible_hostname }}
          OS: {{ ansible_distribution }} {{ ansible_distribution_version }}
        dest: "{{ base_path }}/README.txt"
        owner: root
        group: "{{ app_group }}"
        mode: '0644'
      tags: [docs]

    # GROUP 6: Validation
    - name: Check Nginx configuration syntax
      ansible.builtin.command: nginx -t
      register: nginx_test
      changed_when: false
      tags: [nginx, validate]

    - name: Show Nginx validation result
      ansible.builtin.debug:
        msg: "{{ nginx_test.stderr_lines }}"
      tags: [nginx, validate]

    - name: Ensure Nginx is running
      ansible.builtin.service:
        name: nginx
        state: started
        enabled: true
      tags: [nginx]

  handlers:
    - name: validate and reload nginx
      ansible.builtin.command: nginx -t
      changed_when: false
      notify: reload nginx

    - name: reload nginx
      ansible.builtin.service:
        name: nginx
        state: reloaded
```

## 📎 فایل‌های تکمیلی

سه فایل `templates/*.j2` و اسکریپت `files/scripts/healthcheck.sh` برای اجرای Playbook ضروری هستند و همراه این مستندات در بسته پروژه قرار دارند. فایل `inventory.ini` عمداً نمونه و بدون سرور واقعی است.

## ⚖️ مجوز

MIT — به فایل `LICENSE` مراجعه کنید. هنگام بازنشر، اعلان کپی‌رایت و متن مجوز باید حفظ شوند.

