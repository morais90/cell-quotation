# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-12 22:32
from __future__ import unicode_literals
from decimal import Decimal

from django.db import migrations, models


def forwards_func(apps, schema_editor):
    db_alias = schema_editor.connection.alias

    Plan = apps.get_model('plans', 'Plan')
    Plan.objects.using(db_alias).bulk_create([
        Plan(name='Plano A', minutes=0, data=100, sms=0, value=Decimal('24.90')),
        Plan(name='Plano B', minutes=0, data=100, sms=0, value=Decimal('19.90')),
        Plan(name='Plano C', minutes=0, data=100, sms=0, value=Decimal('14.90')),
        Plan(name='Plano D', minutes=100, data=100, sms=0, value=Decimal('45.90')),
        Plan(name='Plano E', minutes=100, data=300, sms=50, value=Decimal('54.90')),
        Plan(name='Plano F', minutes=100, data=1000, sms=50, value=Decimal('79.90')),
        Plan(name='Plano G', minutes=500, data=1000, sms=50, value=Decimal('59.90')),
        Plan(name='Plano H', minutes=500, data=2000, sms=50, value=Decimal('64.90')),
        Plan(name='Plano I', minutes=500, data=4000, sms=50, value=Decimal('79.90')),
        Plan(name='Plano J', minutes=500, data=10000, sms=50, value=Decimal('104.90')),
        Plan(name='Plano K', minutes=1000, data=3000, sms=800, value=Decimal('99.90')),
        Plan(name='Plano L', minutes=1000, data=6000, sms=800, value=Decimal('129.90')),
        Plan(name='Plano M', minutes=1000, data=10000, sms=800, value=Decimal('144.90'))
    ])

    Package = apps.get_model('plans', 'Package')
    Package.objects.using(db_alias).bulk_create([
        Package(type='sms', amount=50, value=Decimal('6.90')),
        Package(type='sms', amount=100, value=Decimal('9.90')),
        Package(type='sms', amount=800, value=Decimal('12.90')),
        Package(type='sms', amount=0, value=Decimal('15.90'), unlimited=True),
        Package(type='data', amount=500, value=Decimal('6.90')),
        Package(type='data', amount=750, value=Decimal('9.90')),
        Package(type='data', amount=1000, value=Decimal('12.90')),
        Package(type='data', amount=2000, value=Decimal('15.90'))
    ])


def reverse_func(apps, schema_editor):
    db_alias = schema_editor.connection.alias

    Plan = apps.get_model('plan', 'Plan')
    Plan.objects.using(db_alias).filter(
        models.Q(name='Plano A', minutes=0, data=100, sms=0, value=Decimal('24.90')) |
        models.Q(name='Plano B', minutes=0, data=100, sms=0, value=Decimal('19.90')) |
        models.Q(name='Plano C', minutes=0, data=100, sms=0, value=Decimal('14.90')) |
        models.Q(name='Plano D', minutes=100, data=100, sms=0, value=Decimal('45.90')) |
        models.Q(name='Plano E', minutes=100, data=300, sms=50, value=Decimal('54.90')) |
        models.Q(name='Plano F', minutes=100, data=1000, sms=50, value=Decimal('79.90')) |
        models.Q(name='Plano G', minutes=500, data=1000, sms=50, value=Decimal('59.90')) |
        models.Q(name='Plano H', minutes=500, data=2000, sms=50, value=Decimal('64.90')) |
        models.Q(name='Plano I', minutes=500, data=4000, sms=50, value=Decimal('79.90')) |
        models.Q(name='Plano J', minutes=500, data=10000, sms=50, value=Decimal('104.90')) |
        models.Q(name='Plano K', minutes=1000, data=3000, sms=800, value=Decimal('99.90')) |
        models.Q(name='Plano L', minutes=1000, data=6000, sms=800, value=Decimal('129.90')) |
        models.Q(name='Plano M', minutes=1000, data=10000, sms=800, value=Decimal('144.90'))
    ).delete()

    Package = apps.get_model('plan', 'Package')
    Package.objects.using(db_alias).filter(
        models.Q(type='sms', amount=50, value=Decimal('6.90')) |
        models.Q(type='sms', amount=100, value=Decimal('9.90')) |
        models.Q(type='sms', amount=800, value=Decimal('12.90')) |
        models.Q(type='sms', amount=0, value=Decimal('15.90'), unlimited=True) |
        models.Q(type='data', amount=500, value=Decimal('6.90')) |
        models.Q(type='data', amount=750, value=Decimal('9.90')) |
        models.Q(type='data', amount=1000, value=Decimal('12.90')) |
        models.Q(type='data', amount=2000, value=Decimal('15.90'))
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func)
    ]
