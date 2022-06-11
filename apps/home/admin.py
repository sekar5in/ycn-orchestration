# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import Org
from .models import Devices


# Register your models here.
@admin.register(Org)
# Admin View for Organization
class OrgAdmin(admin.ModelAdmin):
    list_display = ('orgId', 'org')


# Register your models here.
@admin.register(Devices)
# Admin View for Organization
class DevicesAdmin(admin.ModelAdmin):
    list_display = ('deviceOrg', 'deviceName', 'deviceIPAddr', 'deviceIPAddr', 'deviceSerial',
                    'deviceLocation', 'deviceSite', 'deviceDesc', 'deviceType', 'devicePort',
                    'deviceLogin', 'devicePassword')

