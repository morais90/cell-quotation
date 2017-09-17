# -*- coding: utf-8 -*-
from decimal import Decimal
from django.test import TestCase

from vcx.plans.models import Plan


class PlanTestCase(TestCase):
    def test_make_dataset_default(self):
        plan = Plan.objects.get(name='Plano A')
        dataset = plan.make_dataset(0, 0)

        self.assertListEqual(dataset, [0, 100, 0, Decimal('24.90'), Decimal('0'), Decimal('0'), Decimal('24.90')])

    def test_make_dataset_data_package(self):
        plan = Plan.objects.get(name='Plano A')
        dataset = plan.make_dataset(3000, 0)

        self.assertListEqual(dataset, [0, 100, 0, Decimal('24.90'), Decimal('28.80'), Decimal('0'), Decimal('53.70')])

    def test_make_dataset_sms_package(self):
        plan = Plan.objects.get(name='Plano A')
        dataset = plan.make_dataset(0, 500)

        self.assertListEqual(dataset, [0, 100, 0, Decimal('24.90'), Decimal('0'), Decimal('12.90'), Decimal('37.80')])

    def test_make_dataset_sms_unlimited(self):
        plan = Plan.objects.get(name='Plano A')
        dataset = plan.make_dataset(0, 1000)

        self.assertListEqual(dataset, [0, 100, 0, Decimal('24.90'), Decimal('0'), Decimal('15.90'), Decimal('40.80')])
