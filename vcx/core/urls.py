# -*- coding: utf-8 -*-
from django.conf.urls import url
from vcx.plans.views import PlanView, CalculateView

urlpatterns = [
    url(r'^$', PlanView.as_view()),
    url(r'^calculate/$', CalculateView.as_view())
]
