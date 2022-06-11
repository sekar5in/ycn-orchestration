# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('devices', views.list_devices, name='devices'),
    path('subscription', views.create_org, name='subscription'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
