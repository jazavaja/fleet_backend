# Generated by Django 5.2.3 on 2025-07-15 08:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleets', '0006_navybrand_sizes_navysize_types'),
    ]

    operations = [
        migrations.CreateModel(
            name='NavyMehvar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='محور ناوگان')),
                ('logo', models.ImageField(upload_to='files/navy-mehvar', verbose_name='لوگو محور ناوگان')),
            ],
        ),
        migrations.RemoveConstraint(
            model_name='navymain',
            name='unique_navy_combination',
        ),
        migrations.AddField(
            model_name='navymehvar',
            name='sizes',
            field=models.ManyToManyField(related_name='mehvars', to='fleets.navysize'),
        ),
        migrations.AddField(
            model_name='navymain',
            name='mehvar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='navies_by_mehvar', to='fleets.navymehvar', verbose_name='محور'),
        ),
        migrations.AddConstraint(
            model_name='navymain',
            constraint=models.UniqueConstraint(fields=('type', 'size', 'brand', 'tip', 'mehvar'), name='unique_navy_combination'),
        ),
    ]
