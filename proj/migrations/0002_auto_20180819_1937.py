# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-19 19:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='customuser',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='profile',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]