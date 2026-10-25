---
# هر سند YAML در Ansible با سه خط تیره شروع می‌شود (اختیاری اما توصیه‌شده).
# یک playbook فهرستی از playهاست؛ این خط تیره آغاز یک play را مشخص می‌کند.
- # فیلد 'name' توضیح می‌دهد که این play چه کاری انجام می‌دهد.
  name: A simple playbook to demonstrate Ansible capabilities
  # فیلد 'hosts' مشخص می‌کند که این play روی کدام میزبان‌های inventory اجرا می‌شود؛ 'all' یعنی همه میزبان‌ها.
  hosts: all
  # فیلد 'become' دسترسی‌های سطح بالا (مثلاً sudo) را برای انجام وظایف سیستمی فعال می‌کند.
  become: yes
  # بخش 'vars' متغیرهایی را تعریف می‌کند که در سراسر play استفاده می‌شوند.
  vars:
    # متغیر 'web_package' نام بسته‌ای را نگه می‌دارد که باید برای وب‌سرور نصب شود.
    web_package: nginx
    # متغیر 'web_service' نام سرویسی را نگه می‌دارد که مدیریت خواهیم کرد.
    web_service: nginx
    # متغیر 'html_path' مسیری را تعریف می‌کند که صفحه خوش‌آمدگویی در آن قرار می‌گیرد.
    html_path: /var/www/html/index.html
  # بخش 'tasks' فهرستی از اقداماتی است که Ansible به ترتیب اجرا می‌کند.
  tasks:
    # وظیفه ۱: به‌روزرسانی کش بسته apt در سیستم‌های خانواده Debian.
    - name: Update apt cache (for Debian/Ubuntu)
      # ماژول 'ansible.builtin.apt' بسته‌های APT را مدیریت می‌کند.
      ansible.builtin.apt:
        # 'update_cache' به ماژول می‌گوید که قبل از ادامه 'apt-get update' را اجرا کند.
        update_cache: yes
        # 'cache_valid_time' اگر کش در بازه زمانی مشخص‌شده (ثانیه) به‌روزرسانی شده باشد، از به‌روزرسانی مجدد صرف‌نظر می‌کند.
        # اگر این پارامتر صریحاً تنظیم شود، 'update_cache=yes' را نیز فعال می‌کند .
        cache_valid_time: 3600
      # 'when' یک شرط اضافه می‌کند — این وظیفه فقط در صورتی اجرا می‌شود که خانواده سیستم‌عامل Debian باشد.
      when: ansible_os_family == "Debian"

    # وظیفه ۲: نصب بسته وب‌سرور با استفاده از ماژول عمومی مدیریت بسته.
    - name: Install the web server package
      # 'ansible.builtin.package' در میان مدیران بسته مختلف (apt، yum، dnf و غیره) کار می‌کند .
      # توجه: این ماژول گزینه‌های پیشرفته‌ای مانند مدیریت مخزن یا به‌روزرسانی کش را پشتیبانی نمی‌کند .
      ansible.builtin.package:
        # 'name' از متغیر تعریف‌شده در بالا برای تعیین بسته‌ای که باید نصب شود استفاده می‌کند.
        name: "{{ web_package }}"
        # 'state' روی 'present' تنظیم شده تا اطمینان حاصل شود که بسته نصب شده است (اما اگر قبلاً نصب شده باشد، ارتقا نمی‌یابد).
        state: present

    # وظیفه ۳: کپی یک صفحه خوش‌آمدگویی سفارشی در پوشه ریشه اسناد با استفاده از ماژول 'copy'.
    - name: Create a custom index.html with hostname information
      # 'ansible.builtin.copy' یک فایل یا محتوای درون‌خطی را به یک مکان راه دور کپی می‌کند.
      ansible.builtin.copy:
        # 'content' رشته تحت‌اللفظی را تعریف می‌کند که نوشته می‌شود؛ از یک عبارت قالب Jinja2 استفاده می‌کند.
        content: |
          <h1>Welcome from {{ ansible_hostname }}</h1>
          <p>Served by Ansible</p>
        # 'dest' مسیر مطلق روی میزبان راه دور است که محتوا در آن نوشته می‌شود.
        dest: "{{ html_path }}"
        # 'owner' مالک فایل را تعیین می‌کند.
        owner: www-data
        # 'group' گروه فایل را تعیین می‌کند.
        group: www-data
        # 'mode' مجوزهای فایل را تعیین می‌کند (0644 = u+rw,g+r,o+r).
        mode: '0644'
      # 'notify' در صورت تغییر چیزی در این وظیفه، handlerی با نام 'restart web service' را فعال می‌کند.
      notify: restart web service

    # وظیفه ۴: اطمینان از اینکه سرویس وب راه‌اندازی شده و در زمان بوت فعال است.
    - name: Start and enable the web service
      # 'ansible.builtin.service' سرویس‌ها را مدیریت می‌کند (شروع، توقف، فعال‌سازی و غیره).
      ansible.builtin.service:
        # 'name' به ماژول می‌گوید که کدام سرویس را مدیریت کند.
        name: "{{ web_service }}"
        # 'state' روی 'started' تنظیم شده تا اطمینان حاصل شود که سرویس در حال اجراست.
        # 'started' یک اقدام idempotent است و فقط در صورت نیاز دستور اجرا می‌کند .
        state: started
        # 'enabled' روی yes تنظیم شده تا سرویس در زمان بوت شروع شود.
        enabled: yes

    # وظیفه ۵: استفاده از یک حلقه برای نصب ابزارهای خط فرمان اضافی مفید.
    - name: Install several helpful packages using a loop
      # استفاده از همان ماژول عمومی بسته.
      ansible.builtin.package:
        # 'name' به آیتم فردی از حلقه تبدیل می‌شود.
        name: "{{ item }}"
        # اطمینان از وجود هر بسته.
        state: present
      # 'loop' روی یک فهرست تکرار می‌کند و وظیفه را یک بار برای هر آیتم اجرا می‌کند.
      loop:
        - curl
        - git
        - htop

    # وظیفه ۶: ثبت نتیجه یک دستور و نمایش آن با debug.
    - name: Check disk usage on the root filesystem
      # 'ansible.builtin.command' دستورات دلخواه را روی میزبان راه دور اجرا می‌کند.
      ansible.builtin.command: df -h /
      # 'register' نتیجه کامل وظیفه را در یک متغیر ذخیره می‌کند.
      register: disk_usage
      # 'changed_when' تشخیص تغییر پیش‌فرض را بازنویسی می‌کند؛ روی false تنظیم شده تا وظیفه هرگز به عنوان 'changed' نمایش داده نشود.
      # این برای دستوراتی که فقط اطلاعات را می‌خوانند مناسب است .
      changed_when: false

    - name: Display disk usage information
      # 'ansible.builtin.debug' پیام‌ها را در طول اجرای playbook چاپ می‌کند.
      ansible.builtin.debug:
        # 'msg' پیام را مشخص می‌کند؛ در اینجا به ویژگی 'stdout' متغیر ثبت‌شده دسترسی پیدا می‌کنیم.
        msg: "Disk usage on /: {{ disk_usage.stdout_lines }}"

  # 'handlers' وظایف ویژه‌ای هستند که فقط زمانی اجرا می‌شوند که توسط وظایف دیگر اطلاع‌داده شوند.
  handlers:
    # نام handler با رشته‌ای که در دستور 'notify' استفاده شده مطابقت دارد.
    - name: restart web service
      # وظایف handler از همان نحو ماژول وظایف معمولی استفاده می‌کنند.
      ansible.builtin.service:
        name: "{{ web_service }}"
        # 'state' روی 'restarted' تنظیم شده تا سرویس متوقف و سپس شروع شود.
        # 'restarted' همیشه سرویس را دوباره راه‌اندازی می‌کند .
        state: restarted
