# روز سوم | مدیریت کاربران و امنیت

[English](README_EN.md)

**هدف:** کار با `user`، `register` و `when` بدون دستکاری SSH، فایروال یا دسترسی sudo.

**نکته:** تغییر SSH و UFW روی سرور دوردست می‌تواند دسترسی شما را قطع کند؛ این مباحث را جداگانه و فقط با دسترسی کنسول تمرین کنید.

```bash
ansible-playbook -i 2nd_day/inventory.ini user-security.yml --syntax-check
ansible-playbook -i 2nd_day/inventory.ini user-security.yml --check --diff
ansible-playbook -i 2nd_day/inventory.ini user-security.yml --ask-become-pass
# Optional cleanup:
ansible-playbook -i 2nd_day/inventory.ini user-security.yml -e cleanup_demo_user=true --ask-become-pass
```

**سه نکته:** رمزها و کلید خصوصی را commit نکنید؛ برای داده حساس `ansible-vault` استفاده کنید؛ قبل از تنظیمات امنیتی، امکان بازیابی سرور را بررسی کنید.
