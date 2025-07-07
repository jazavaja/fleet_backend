from django.db import models


class UsageType(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='نام کاربری',
        unique=True
    )
    description = models.TextField(
        verbose_name='توضیحات',
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        verbose_name='تاریخ ایجاد',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='تاریخ بروزرسانی',
        auto_now=True
    )

    class Meta:
        verbose_name = 'نوع کاربری ناوگان'
        verbose_name_plural = 'انواع کاربری ناوگان'
        ordering = ['name']

    def __str__(self):
        return self.name
