# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class subscription(models.Model):

    '''
        [
        '%Y-%m-%d %H:%M:%S',     # '2006-10-25 14:30:59'
        '%Y-%m-%d %H:%M:%S.%f',  # '2006-10-25 14:30:59.000200'
        '%Y-%m-%d %H:%M',        # '2006-10-25 14:30'
        '%m/%d/%Y %H:%M:%S',     # '10/25/2006 14:30:59'
        '%m/%d/%Y %H:%M:%S.%f',  # '10/25/2006 14:30:59.000200'
        '%m/%d/%Y %H:%M',        # '10/25/2006 14:30'
        '%m/%d/%y %H:%M:%S',     # '10/25/06 14:30:59'
        '%m/%d/%y %H:%M:%S.%f',  # '10/25/06 14:30:59.000200'
        '%m/%d/%y %H:%M',        # '10/25/06 14:30'
        ]
    '''

    Plan = [
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
        ('dev', 'Devices'),
    ]
    # orgMaxDevice default = 0 means , unlimited devices by default for an organization
    subsMaxDevice = models.IntegerField(default=0, blank=False)
    subsPlan = models.CharField(max_length=8, choices=Plan, default='monthly')
    subsStart = models.DateTimeField()
    subsEnd = models.DateTimeField()


class Org(models.Model):
    # objects: models.Manager()
    orgId = models.CharField(max_length=255, primary_key=True)
    org = models.CharField(max_length=255, null=False, blank=False)
    orgMaxDevice = models.ForeignKey(subscription, on_delete=models.CASCADE)

    class Meta:
        ordering = ("orgId",)

    def __unicode__(self):
        return self.org


class Devices(models.Model):
    #deviceId = models.IntegerField(primary_key=True)
    deviceOrg = models.ForeignKey(Org, on_delete=models.CASCADE, null=False, blank=False)
    deviceName = models.CharField(max_length=255, null=False, blank=False)
    deviceIPAddr = models.GenericIPAddressField()
    deviceSerial = models.CharField(max_length=255)
    deviceLocation = models.CharField(max_length=255)
    deviceSite = models.CharField(max_length=255)
    deviceDesc = models.CharField(max_length=255)
    deviceType = models.CharField(max_length=10)
    devicePort = models.IntegerField()
    deviceLogin = models.CharField(max_length=15)
    devicePassword = models.CharField(max_length=15)

    class Meta:
        ordering = ("deviceName",)

    def __unicode__(self):
        return self.deviceName