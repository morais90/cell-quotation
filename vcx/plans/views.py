# -*- coding: utf-8 -*-
from collections import defaultdict
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.views import View

from .models import Plan, Package


class PlanView(TemplateView):
    template_name = 'plans/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'plans': Plan.objects.all().order_by('name'),
            'packages': Package.objects.all().order_by('type')
        })

        return context


class CalculateView(View):
    '''Calculate the cost of the plans and returns the sum
    of the packages and plans

    Expected querystring:
        minutes: Required plan minutes
        data: Required plan Internet data
        sms: Required plan SMS data
    '''
    def post(self, request, *args, **kwargs):
        minutes = float(request.POST.get('minutes', 0))
        data = float(request.POST.get('data', 0))
        sms = float(request.POST.get('sms', 0))

        plans = Plan.objects.filter(minutes__gte=minutes)
        dataset = defaultdict(list)

        for plan in plans.iterator():
            plan_dataset = plan.make_dataset(data, sms)
            dataset[plan.name].extend(plan_dataset)

        return JsonResponse(dataset)
