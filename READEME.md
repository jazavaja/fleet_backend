<div dir="rtl" style="font-family: 'Vazir', Tahoma, sans-serif;">

##  ساختار پیشنهادی Django Apps:

| Django App                    | توضیحات کامل                                                     |
| ----------------------------- | ---------------------------------------------------------------- |
| **accounts**                  | مدیریت کاربران، احراز هویت، نقش‌ها (roles)، دسترسی‌ها، تغییر رمز |
| **fleets**                    | ثبت و مدیریت ناوگان (نوع، سایز، برند، تیپ)                       |
| **regions**                   | ثبت مناطق فعالیت (استان، شهر، منطقه)                             |
| **usages**                    | ثبت نوع کاربری ناوگان (مثل یخچالی)                               |
| **services**                  | مدیریت درخواست‌های سرویس‌دهندگان، تایید یا رد آن‌ها              |
| **categories** یا **sectors** | ثبت رسته فعالیت (نام رسته، خدمت یا کالا)                         |
| **exports**                   | مدیریت خروجی اکسل برای هر ماژول                                  |
| **core** یا **common**        | برای ابزارهای مشترک (مدل‌ها، mixins، utils، middleware و...)     |

---

##  جزئیات هر App:

###  1. `accounts`

* مدل User (کاستوم یا extend شده از AbstractUser)
* مدل Role / Group
* Permission System با `django-guardian` یا `rules` یا `DRF permissions`
* پنل ثبت/ویرایش کاربران و مدیریت نقش‌ها
* تغییر رمز، فعال/غیرفعال کردن کاربر

---

###  2. `fleets`

* مدل Fleet:

  ```python
  class Fleet(models.Model):
      type = models.CharField(...)      # مثل کشنده، باری
      size = models.CharField(...)
      brand = models.CharField(...)
      model = models.CharField(...)     # تیپ ناوگان
  ```
* امکان فیلتر، جستجو، و خروجی اکسل

---

###  3. `regions`

* مدل Province, City, Zone
* UI پویا (مثلاً انتخاب استان → شهرها فیلتر شن)

---

###  4. `usages`

* مدل UsageType:

  ```python
  class UsageType(models.Model):
      name = models.CharField(...)  # مثلاً یخچالی، عادی
  ```

---

###  5. `services`

* مدل ServiceProvider:

  ```python
  class ServiceProvider(models.Model):
      user = models.ForeignKey(...)
      status = models.CharField(choices=[('pending', 'در انتظار'), ('approved', 'تایید شده'), ('rejected', 'رد شده')])
      ...
  ```
* تایید یا رد توسط ادمین

---

###  6. `sectors`

* مدل Sector:

  ```python
  class Sector(models.Model):
      name = models.CharField(...)      # نام رسته
      type = models.CharField(...)      # خدمت / کالا
  ```

---

###  7. `exports`

* خروجی اکسل با `django-import-export` یا `openpyxl`
* برای هر جدول دکمه‌ی Export to Excel
* می‌تونی داخل هر view بذاری یا اختصاصی کنی

---

##  نصب پکیج‌های پیشنهادی:

```bash
pip install djangorestframework
pip install django-cors-headers
pip install django-filter
pip install django-import-export
pip install django-guardian
```

---

##  دسترسی نقش‌ها:

برای RBAC از یکی از این ۳ گزینه استفاده کن:

* `django.contrib.auth` (پایه‌ای ولی ساده)
* `django-guardian` برای object-level permission
* `django-rules` یا `DRF permissions` برای REST API با سطوح دقیق‌تر

---

## ارتباط با React:

در نهایت برای ارتباط React با Django:

* از `Django REST Framework (DRF)` برای ساخت API استفاده کن
* همه endpointها به‌صورت REST طراحی بشن
* React front با Fetch یا Axios داده‌ها رو بگیره

---

برای پروژه‌ی مدیریت ناوگان با نقش‌ها و ثبت داده‌های مختلف، API views در Django REST Framework بخش حیاتی هستند.
لیست کلی و پیشنهادی API views به صورت لیست وار و همراه با توضیح کوتاه:

---

## ۱. **User & Authentication**

* **RegisterUserAPIView**: ثبت کاربر جدید
* **LoginAPIView**: ورود کاربر (می‌تونی JWT یا TokenAuth استفاده کنی)
* **LogoutAPIView**: خروج
* **ChangePasswordAPIView**: تغییر رمز عبور
* **UserProfileAPIView**: مشاهده و ویرایش پروفایل کاربر جاری
* **UserListAPIView**: (برای مدیر) لیست کاربران
* **UserDetailAPIView**: جزئیات کاربر خاص (ویرایش، حذف، مشاهده)

---

## ۲. **Role & Permission Management**

* (اگر از Group و Permission خود Django استفاده می‌کنی)
* **GroupListAPIView**: لیست گروه‌ها
* **GroupDetailAPIView**: مشاهده، ویرایش گروه و دسترسی‌ها
* **AssignUserToGroupAPIView**: اختصاص کاربر به گروه (نقش)

---

## ۳. **Fleet Management (ناوگان)**

* **FleetListAPIView**: لیست ناوگان‌ها
* **FleetCreateAPIView**: ثبت ناوگان جدید (نوع، سایز، برند و تیپ)
* **FleetDetailAPIView**: جزئیات، ویرایش و حذف ناوگان

---

## ۴. **Region Management (منطقه فعالیت)**

* **RegionListAPIView**: لیست مناطق (استان، شهر، منطقه متنی)
* **RegionCreateAPIView**: ثبت منطقه جدید
* **RegionDetailAPIView**: ویرایش، حذف منطقه

---

## ۵. **Usage Type Management (نوع کاربری)**

* **UsageTypeListAPIView**: لیست نوع کاربری (مثلاً یخچالی)
* **UsageTypeCreateAPIView**: ثبت نوع کاربری جدید
* **UsageTypeDetailAPIView**: ویرایش، حذف نوع کاربری

---

## ۶. **Activity Category (رسته فعالیت)**

* **ActivityCategoryListAPIView**: لیست رسته‌ها (نام رسته، خدمت یا کالا)
* **ActivityCategoryCreateAPIView**: ثبت رسته جدید
* **ActivityCategoryDetailAPIView**: ویرایش، حذف رسته

---

## ۷. **Service Provider Requests (مدیریت درخواست سرویس‌دهندگان)**

* **ServiceProviderRequestListAPIView**: لیست درخواست‌ها
* **ServiceProviderRequestApproveAPIView**: تایید درخواست
* **ServiceProviderRequestRejectAPIView**: رد درخواست

---

## ۸. **Export Excel**

* API جداگانه یا endpoint که خروجی Excel جداول مختلف رو ایجاد کنه
* مثلاً:

  * `/api/export/fleets/`
  * `/api/export/users/`

---


## نکات مهم:

* برای همه viewها از permission مناسب استفاده کن (مثلاً فقط admin بتونه حذف کنه)
* اگر تعداد زیاد است، از viewset و router استفاده کن که کد تمیزتر باشه
* برای تایید و رد درخواست‌ها می‌تونی action سفارشی تو viewset تعریف کنی

---
</div>