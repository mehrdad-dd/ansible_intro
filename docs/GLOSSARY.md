# Ansible mini-glossary | واژه‌نامه کوتاه

| Concept | معنی دقیق و کوتاه | One-line explanation |
|---|---|---|
| Control node | سیستم اجراکننده Ansible | Machine running Ansible |
| Managed node | میزبان تحت مدیریت | Target managed by Ansible |
| Inventory | فهرست و گروه‌بندی میزبان‌ها | Host/group catalog |
| Play | اتصال میزبان‌ها به Taskها | A set of tasks applied to hosts |
| Playbook | فایل YAML شامل Playها | YAML automation plan |
| Task | یک عمل مشخص | One unit of work |
| Module | ابزار اجرایی Task | Executable Ansible capability |
| Variable | داده قابل جایگزینی | Value influencing behavior |
| Fact | داده شناسایی‌شده از میزبان | Collected host information |
| Jinja2 | موتور قالب و عبارت | Templating/filter engine |
| Handler | Task قابل اعلان هنگام تغییر | Notified task run on change |
| Idempotency | بدون تغییر اضافی در اجرای مجدد | Convergent repeat execution |
| Role | بسته قابل‌استفاده‌مجدد | Reusable automation unit |
| Collection | بسته ماژول‌ها و Roleها | Distributable content namespace |
| Vault | رمزگذاری داده در مخزن | Encryption for sensitive files |
| Delegate | تغییر محل اجرای یک Task | Execute a task elsewhere |
| Serial | تعداد میزبان در هر Batch | Rolling batch size |
| Check mode | پیش‌نمایش تغییرات | Dry-run preview |
| Assert | بررسی یک شرط الزامی | Executable expectation |
| CI | آزمایش خودکار تغییرات | Continuous integration |

[Course index / فهرست دروس](../README.md)
