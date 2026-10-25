<div align="center">

# 🚀 راه‌اندازی وب‌سرور Nginx با Ansible

**یک Playbook کاربردی و آموزشی برای نصب Nginx، ساخت صفحه خوش‌آمدگویی اختصاصی و بررسی فضای دیسک با Ansible.**

![Ansible](https://img.shields.io/badge/Ansible-Automation-EE0000?style=for-the-badge&logo=ansible&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-Web_Server-009639?style=for-the-badge&logo=nginx&logoColor=white)
![YAML](https://img.shields.io/badge/YAML-Playbook-CB171E?style=for-the-badge&logo=yaml&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-Debian%20%7C%20Ubuntu-FCC624?style=for-the-badge&logo=linux&logoColor=black)

</div>

---

## 📖 معرفی پروژه

این نمونه، مفاهیم اصلی Ansible را در یک سناریوی عملی نشان می‌دهد: نصب وب‌سرور، ساخت صفحه HTML با نام میزبان، فعال‌سازی سرویس، نصب ابزارهای کاربردی و نمایش میزان استفاده از دیسک.

> [!NOTE]
> این مثال برای میزبان‌های **Debian/Ubuntu** طراحی شده است. هرچند ماژول `ansible.builtin.package` از مدیر بسته‌های مختلف پشتیبانی می‌کند، کاربر `www-data` و مسیر `/var/www/html` لزوماً در همه توزیع‌های لینوکس یکسان نیستند.

## ✨ قابلیت‌ها

| قابلیت | مفهوم Ansible |
| --- | --- |
| به‌روزرسانی کش APT | اجرای شرطی با `when` |
| نصب Nginx | متغیرها و `ansible.builtin.package` |
| ساخت صفحه اصلی اختصاصی | اطلاعات میزبان در Jinja2 و `ansible.builtin.copy` |
| اجرای خودکار Nginx هنگام روشن‌شدن سیستم | `ansible.builtin.service` |
| نصب `curl`، `git` و `htop` | `loop` |
| بررسی فضای دیسک ریشه | `register`، `changed_when` و `debug` |
| راه‌اندازی مجدد Nginx پس از تغییر صفحه | Handler و `notify` |

## 📁 ساختار پروژه

```text
ansible-nginx-demo/
├── README.md
├── LICENSE
├── inventory.ini
└── playbook.yml
```

## 🧰 پیش‌نیازها

- نصب Ansible روی سیستم کنترل‌کننده.
- دسترسی SSH به سرورهای مقصد Debian/Ubuntu.
- حساب کاربری دارای مجوز `sudo` در سرورهای مقصد.
- وجود Python روی میزبان‌های مدیریت‌شونده.

## ⚙️ نمونه فایل Inventory

فایل `inventory.ini` را بسازید و نشانی IP و نام کاربری نمونه را با مقادیر واقعی خود جایگزین کنید:

```ini
[webservers]
web1 ansible_host=192.0.2.10 ansible_user=ubuntu
```

> [!TIP]
> نشانی `192.0.2.10` صرفاً برای مستندسازی است؛ از IP واقعی یا نام دامنه سرور خود استفاده کنید.

## 📝 کد اصلی Playbook (`playbook.yml`)

کد زیر عیناً حفظ شده است؛ توضیحات انگلیسی داخل کد نیز برای نگهداری نسخه اصلی تغییر نکرده‌اند.

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

## ▶️ اجرای Playbook

کد YAML بالا را در فایل `playbook.yml` ذخیره کنید و سپس دستورهای زیر را اجرا کنید:

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
> اگر کاربر SSH شما بدون رمز به `sudo` دسترسی دارد، گزینه `--ask-become-pass` را حذف کنید. برای دسترسی از راه دور به وب‌سایت، مطمئن شوید پورت **80/TCP** در فایروال یا Security Group مجاز است.

## 🌐 بررسی نتیجه استقرار

IP نمونه را با نشانی سرور خود جایگزین کنید:

```bash
curl http://192.0.2.10/
```

خروجی مورد انتظار (نام میزبان ممکن است متفاوت باشد):

```html
<h1>Welcome from web1</h1>
<p>Served by Ansible</p>
```

## 🧠 مفاهیم کلیدی Ansible

- **Idempotency (تکرارپذیری بدون تغییر اضافی):** اجرای دوباره بیشتر وظایف، سیستمِ از قبل تنظیم‌شده را بی‌دلیل تغییر نمی‌دهد.
- **Facts (اطلاعات میزبان):** متغیرهای `ansible_hostname` و `ansible_os_family` در حالت پیش‌فرض به‌صورت خودکار جمع‌آوری می‌شوند.
- **Variables (متغیرها):** مقادیر `web_package`، `web_service` و `html_path` تنظیمات را متمرکز می‌کنند.
- **Conditionals (شرط‌ها):** عبارت `when` به‌روزرسانی کش APT را به خانواده Debian محدود می‌کند.
- **Handlers:** وظیفه راه‌اندازی مجدد فقط هنگام دریافت اعلان از یک وظیفه تغییرکرده اجرا می‌شود؛ Handlerها معمولاً نزدیک پایان Play اجرا می‌شوند.
- **Registered results (نتایج ذخیره‌شده):** عبارت `disk_usage.stdout_lines` خروجی دستور `df -h /` را نمایش می‌دهد.

## 🔧 رفع مشکلات رایج

| مشکل | راهکار پیشنهادی |
| --- | --- |
| خطای اتصال SSH | نشانی IP، نام کاربری، کلید SSH و دسترسی پورت 22 را بررسی کنید. |
| خطای دسترسی sudo | از حساب دارای مجوز sudo استفاده کنید و در صورت نیاز رمز ارتقای دسترسی را وارد کنید. |
| صفحه Nginx باز نمی‌شود | وضعیت سرویس Nginx و قوانین فایروال پورت 80 را بررسی کنید. |
| کاربر `www-data` پیدا نشد | از Debian/Ubuntu استفاده کنید یا مالک فایل را متناسب با توزیع تغییر دهید. |
| نصب بسته ناموفق است | اتصال به مخازن بسته‌ها و نام بسته‌ها را بررسی کنید. |

## 📄 مجوز استفاده

این پروژه تحت مجوز **MIT** منتشر می‌شود. استفاده، کپی، ویرایش، انتشار و استفاده تجاری مجاز است، مشروط به حفظ متن مجوز و اعلان کپی‌رایت. جزئیات را در فایل [`LICENSE`](LICENSE) ببینید.

## 📚 منابع بیشتر

- [Ansible documentation](https://docs.ansible.com/ansible/latest/)
- [Ansible playbooks](https://docs.ansible.com/ansible/latest/playbook_guide/index.html)
- [Ansible built-in modules](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/index.html)

---

<div align="center">

**یادگیری Ansible، قدم‌به‌قدم و با مثال عملی.** ⚡

</div>
