# -*- coding: utf-8 -*-
from decimal import Decimal
from django.test import TestCase

from vcx.plans.models import Package


class PackageTest(TestCase):
    def test_calculate_internet_type(self):
        self.assertEqual(Decimal('6.90'), Package.calculate(500, Package.DATA))
        self.assertEqual(Decimal('9.90'), Package.calculate(750, Package.DATA))
        self.assertEqual(Decimal('12.90'), Package.calculate(1000, Package.DATA))
        self.assertEqual(Decimal('15.90'), Package.calculate(2000, Package.DATA))

    def test_calculate_internet_type_extra(self):
        self.assertEqual(Decimal('47.70'), Package.calculate(5500, Package.DATA))

    def test_calculate_sms_type(self):
        self.assertEqual(Decimal('6.90'), Package.calculate(50, Package.SMS))
        self.assertEqual(Decimal('9.90'), Package.calculate(100, Package.SMS))
        self.assertEqual(Decimal('12.90'), Package.calculate(800, Package.SMS))
        self.assertEqual(Decimal('15.90'), Package.calculate(2000, Package.SMS))

    def test_calculate_sms_type_extra(self):
        self.assertEqual(Decimal('15.90'), Package.calculate(5500, Package.SMS))
