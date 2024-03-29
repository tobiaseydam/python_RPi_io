# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 17:52:06 2019

@author: Tobias
"""

from django.urls import path
from . import views
from .views import gpioPinListView, gpioPinDetailView, gpioPinUpdateView

urlpatterns = [
    path("", gpioPinListView.as_view(), name="gpio_manager-home"),
    path("list/", gpioPinListView.as_view(), name="gpio_manager-overview"),
    path("pin/<int:pk>/", gpioPinDetailView.as_view(), name="gpio_manager-detail"),
    path("pin/update/<int:pk>/", gpioPinUpdateView.as_view(), name="gpio_manager-update"),
]