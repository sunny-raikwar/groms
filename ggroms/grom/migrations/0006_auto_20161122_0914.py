# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-22 03:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grom', '0005_auto_20161109_1958'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agentdetail',
            old_name='Nomini_id',
            new_name='nomini_id',
        ),
        migrations.AddField(
            model_name='agentdetail',
            name='image',
            field=models.ImageField(null=True, upload_to=b''),
        ),
    ]
