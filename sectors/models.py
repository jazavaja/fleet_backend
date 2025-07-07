from django.db import models

# Create your models here.

class ActivityCategory(models.Model):
    CATEGORY_TYPE_CHOICES = (
        ('SERVICE', 'خدمت'),
        ('PRODUCT', 'کالا'),
    )

    name = models.CharField(
        max_length=100,
        verbose_name='نام رسته',
        unique=True
    )
    category_type = models.CharField(
        max_length=10,
        choices=CATEGORY_TYPE_CHOICES,
        verbose_name='نوع رسته',
        help_text='تعیین می‌کند این رسته مربوط به خدمت است یا کالا'
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
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'category_type'],
                name='unique_category_name_type'
            )
        ]

    def __str__(self):
        return f"{self.name} ({self.get_category_type_display()})"