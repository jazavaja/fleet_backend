# Create your models here.

from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.db import models


class UserServiceProvider(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'در انتظار تایید'),
        ('APPROVED', 'تایید شده'),
        ('REJECTED', 'رد شده'),
        ('SUSPENDED', 'معلق'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='service_provider',
                                verbose_name='کاربر')
    national_id = models.CharField(max_length=10, verbose_name='کد ملی', unique=True)
    activity_category = models.CharField(max_length=50, choices=ACTIVITY_CATEGORIES, verbose_name='رسته فعالیت')
    activity_areas = models.ManyToManyField('ActivityArea', verbose_name='مناطق فعالیت')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING', verbose_name='وضعیت')
    manager_image = models.ImageField(upload_to='service_providers/manager_images/', verbose_name='تصویر مسئول',
                                      validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])])
    stamp_image = models.ImageField(upload_to='service_providers/stamp_images/', verbose_name='تصویر مهر',
                                    validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])])
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت نام')
    approval_date = models.DateTimeField(null=True, blank=True, verbose_name='تاریخ تایید')
    rejection_reason = models.TextField(null=True, blank=True, verbose_name='دلیل رد')

    class Meta:
        verbose_name = 'سرویس دهنده'
        verbose_name_plural = 'سرویس دهندگان'
        ordering = ['-registration_date']

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.get_activity_category_display()}"

    @property
    def mobile(self):
        return self.user.mobile

    @property
    def full_name(self):
        return self.user.get_full_name()
