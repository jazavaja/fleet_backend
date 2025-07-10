# regions/apps.py
import json
import os

from django.apps import AppConfig
from django.conf import settings


class RegionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'regions'

    def ready(self):
        if getattr(settings, 'INIT_PROVINCE_CITY', False):
            if os.environ.get('RUN_MAIN') == 'true':
                self.load_provinces_and_cities()

    def load_provinces_and_cities(self):
        from django.apps import apps

        Province = apps.get_model('regions', 'Province')
        City = apps.get_model('regions', 'City')

        data_path = os.path.join(self.path, 'data')
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

        # بارگذاری شهرها
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
