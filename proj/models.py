# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.


class CustomUser(models.Model):
    user = models.OneToOneField(User)

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = CustomUser.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)



class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    datestamp = models.DateTimeField(auto_now_add=True)
    document = models.FileField(upload_to='uploads/%Y/%m/%d/')