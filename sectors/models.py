# Create your models here.
from django.db import models


class ActivityCategory(models.Model):
    CATEGORY_TYPE_CHOICES = (
        ('SERVICE', 'خدمت'),
        ('PRODUCT', 'کالا'),
        ('BOTH', 'کالا و خدمت'),
    )

    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='نام رسته'
    )

    category_type = models.CharField(
        max_length=10,
        choices=CATEGORY_TYPE_CHOICES,
        default='SERVICE',
        verbose_name='نوع رسته'
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name='فعال'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='تاریخ ایجاد'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='تاریخ بروزرسانی'
    )

    class Meta:
        verbose_name = 'رسته فعالیت'
        verbose_name_plural = 'رسته‌های فعالیت'
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.get_category_type_display()})"
