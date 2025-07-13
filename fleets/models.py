# Create your models here.

from django.db import models


class NavyType(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='نوع ناوگان')
    logo = models.ImageField(upload_to='files/navy-type', verbose_name='لوگو تایپ ناوگان')

    def __str__(self):
        return self.name


class NavySize(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='سایز ناوگان')
    logo = models.ImageField(upload_to='files/navy-size', verbose_name='لوگو سایز ناوگان')
    types = models.ManyToManyField(NavyType, related_name='sizes')  # Many-to-many

    def __str__(self):
        return self.name


class NavyBrand(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='برند ناوگان')
    logo = models.ImageField(upload_to='files/navy-brands', verbose_name='لوگو برند ناوگان')
    sizes = models.ManyToManyField(NavySize, related_name='brands')  # Many-to-many

    def __str__(self):
        return self.name


class NavyMain(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام اصلی ناوگان')
    type = models.ForeignKey(NavyType, on_delete=models.SET_NULL, null=True, blank=True, related_name='navies_by_type',
                             verbose_name='نوع')
    size = models.ForeignKey(NavySize, on_delete=models.SET_NULL, null=True, blank=True, related_name='navies_by_size',
                             verbose_name='سایز')
    brand = models.ForeignKey(NavyBrand, on_delete=models.SET_NULL, null=True, blank=True,
                              related_name='navies_by_brand', verbose_name='برند')
    tip = models.CharField(max_length=100, verbose_name='تیپ ناوگان')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['type', 'size', 'brand', 'tip'],
                name='unique_navy_combination'
            )
        ]

    def __str__(self):
        return self.name
