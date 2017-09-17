# -*- coding utf-8 -*-
from decimal import Decimal
from django.db import models


class Plan(models.Model):
    name = models.CharField(max_length=100)
    minutes = models.IntegerField(default=0)
    data = models.IntegerField(default=0)
    sms = models.IntegerField(default=0)
    value = models.DecimalField(max_digits=8, decimal_places=2)

    def make_dataset(self, data, sms):
        '''Return Dataset for Chart

        Parameters:
            data: Internet data amount
            sms: SMS amount

        Returns:
            [plan_minute, plan_data, plan_sms, plan_value, data_package_value, sms_package_value, total]
        '''

        dataset = [
            self.minutes,
            self.data,
            self.sms,
            self.value
        ]
        data_package_value = Decimal()
        sms_package_value = Decimal()

        # Need more data packages
        if self.data < data:
            remaining_data = data - self.data
            data_package_value = Package.calculate(remaining_data, Package.DATA)

        # Need more sms packages
        if self.sms < sms:
            remaining_sms = sms - self.sms
            sms_package_value = Package.calculate(remaining_sms, Package.SMS)

        total = sum([self.value, data_package_value, sms_package_value])

        dataset.extend([
            data_package_value,
            sms_package_value,
            total
        ])

        return dataset


class Package(models.Model):
    SMS = 'sms'
    DATA = 'data'

    TYPES = (
        (SMS, 'SMS'),
        (DATA, 'data')
    )

    type = models.CharField(max_length=25, choices=TYPES)
    unlimited = models.BooleanField(default=False)
    amount = models.IntegerField()
    value = models.DecimalField(max_digits=8, decimal_places=2)

    @staticmethod
    def calculate(amount, _type, accumulated=Decimal()):
        '''Recursive method to calculate packages cost

        Parameters:
            amount: Amount that needs to be satisfied
            type: Type of Package (SMS or DATA)
            accumulated: Recursive SUM cache (not change manually)
        '''
        if amount <= 0:
            return accumulated

        # Greater than 800 means unlimited SMS plan
        if _type == Package.SMS and amount > 800:
            return Package.objects.values('value').get(unlimited=True).get('value')

        package = Package.objects.filter(type=_type, amount__gte=amount).values('value').first()

        # Found the package with correct amount
        if package:
            return package.get('value') + accumulated

        # We are unlucky, need to combine the packages :(
        else:
            package = Package.objects.values('value', 'amount').latest('amount')
            amount = amount - package.get('amount')
            accumulated = package.get('value') + accumulated

            return Package.calculate(amount, _type, accumulated=accumulated)
