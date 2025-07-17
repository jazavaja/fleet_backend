# regions/management/commands/load_regions.py

import os
import json

from django.core.management.base import BaseCommand
from django.apps import apps


class Command(BaseCommand):
    help = 'Load provinces and cities from JSON files into the database'

    def handle(self, *args, **kwargs):
        self.stdout.write('Loading provinces and cities...')

        Province = apps.get_model('regions', 'Province')
        City = apps.get_model('regions', 'City')

        app_path = os.path.dirname(os.path.dirname(__file__))
        data_path = os.path.join(app_path, 'data')

        # Load provinces
        with open(os.path.join(data_path, 'provinces.json'), 'r', encoding='utf-8') as f:
            provinces = json.load(f)
            for item in provinces:
                Province.objects.update_or_create(
                    id=item['id'],
                    defaults={
                        'name': item['name'],
                        'slug': item['slug'],
                        'tel_prefix': item['tel_prefix']
                    }
                )
            self.stdout.write(self.style.SUCCESS(f'{len(provinces)} provinces loaded.'))

        # Load cities
        with open(os.path.join(data_path, 'cities.json'), 'r', encoding='utf-8') as f:
            cities = json.load(f)
            for item in cities:
                try:
                    province = Province.objects.get(id=item['province_id'])
                    City.objects.update_or_create(
                        id=item['id'],
                        defaults={
                            'name': item['name'],
                            'slug': item['slug'],
                            'province': province,
                            'county_id': item['county_id']
                        }
                    )
                except Province.DoesNotExist:
                    continue
            self.stdout.write(self.style.SUCCESS(f'{len(cities)} cities loaded.'))