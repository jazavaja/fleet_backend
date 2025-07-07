# Create your models here.
from django.core.validators import MinLengthValidator
from django.db import models


class Province(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    tel_prefix = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'استان'
        verbose_name_plural = 'استان‌ها'
        ordering = ['name']

    def __str__(self):
        return self.name


class City(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    province = models.ForeignKey(
        Province,
        on_delete=models.CASCADE,
        related_name='cities'
    )
    county_id = models.BigIntegerField()

    class Meta:
        verbose_name = 'شهر'
        verbose_name_plural = 'شهرها'
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.province.name})"


class ActivityArea(models.Model):
    province = models.ForeignKey(
        Province,
        on_delete=models.CASCADE,
        verbose_name='استان',
        related_name='activity_areas'
    )
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        verbose_name='شهر',
        related_name='activity_areas'
    )
    area = models.CharField(
        max_length=255,
        verbose_name='منطقه',
        validators=[MinLengthValidator(2)]
    )

    class Meta:
        verbose_name = 'منطقه فعالیت'
        verbose_name_plural = 'مناطق فعالیت'
        constraints = [
            models.UniqueConstraint(
                fields=['province', 'city', 'area'],
                name='unique_activity_area'
            )
        ]

    def __str__(self):
        return f"{self.area} - {self.city.name} - {self.province.name}"
