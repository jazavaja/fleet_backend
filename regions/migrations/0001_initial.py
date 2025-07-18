# Generated by Django 5.2.3 on 2025-07-10 07:49

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('tel_prefix', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'استان',
                'verbose_name_plural': 'استان\u200cها',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('county_id', models.BigIntegerField()),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='regions.province')),
            ],
            options={
                'verbose_name': 'شهر',
                'verbose_name_plural': 'شهرها',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ActivityArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='منطقه')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_areas', to='regions.city', verbose_name='شهر')),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_areas', to='regions.province', verbose_name='استان')),
            ],
            options={
                'verbose_name': 'منطقه فعالیت',
                'verbose_name_plural': 'مناطق فعالیت',
                'constraints': [models.UniqueConstraint(fields=('province', 'city', 'area'), name='unique_activity_area')],
            },
        ),
    ]
