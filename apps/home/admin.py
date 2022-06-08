# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import Org

# Register your models here.

@admin.register(Org)
class AuthorAdmin(admin.ModelAdmin):
    pass