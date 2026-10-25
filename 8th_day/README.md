# روز 8 | Loops، Filters و تبدیل داده در Ansible

[English](README_EN.md) · [فهرست دوره](../README.md) · [منبع رسمی](https://docs.ansible.com/projects/ansible-core/stable-2.22/playbook_guide/index.html)

> **مسئله در یک جمله:** قبل از اجرای یک عمل تکراری، لیست را به داده تمیز و بدون تکرار تبدیل کن.

### نکته عمیق
`unique` عناصر تکراری را حذف می‌کند، `sort` ترتیب ثابت می‌دهد و `loop` برای هر مقدار یک Task اجرا می‌کند.

### مثال کوتاه و واقعی
```yaml
---
# Shared example: loop over normalized values.
- name: Iterate over clean data
  hosts: lab
  gather_facts: false
  vars:
    input_ports: [443, 8080, 443, 80]
  tasks:
    - name: Normalize the list
      ansible.builtin.set_fact:
        unique_ports: "{{ input_ports | unique | sort | list }}"

    - name: Show each unique port
      ansible.builtin.debug:
        msg: "Allowed demo port: {{ item }}"
      loop: "{{ unique_ports }}"

    - name: Verify deduplication
      ansible.builtin.assert:
        that: unique_ports | length == 3
```

### اجرا و نتیجه
```bash
ansible-playbook -i 8th_day/inventory.yml 8th_day/playbook.yml --syntax-check
ansible-playbook -i 8th_day/inventory.yml 8th_day/playbook.yml
```

**خروجی مورد انتظار:** Playbook بدون تغییر حساس روی سیستم اجرا می‌شود و پیام یا Assertion واضح نشان می‌دهد.

### اشتباه رایج
فیلتر `sort` برای رشته و عدد رفتار متفاوتی دارد؛ نوع داده را روشن نگه دار.

**تمرین ۱ دقیقه‌ای:** پورت 443 را دوبار اضافه کن و ببین چندبار در خروجی ظاهر می‌شود.

<sub>نمونه آزمایشی است؛ هیچ رمز، IP واقعی یا دسترسی مدیریتی نیاز ندارد.</sub>
