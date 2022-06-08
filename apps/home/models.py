# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Org(models.Model):
    org = models.CharField(max_length=255)
    orgId = models.CharField(max_length=255)
