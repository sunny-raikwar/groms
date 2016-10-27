# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-26 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StaffUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loginid', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('fullname', models.CharField(max_length=100)),
                ('contact_no', models.CharField(max_length=15)),
                ('alternate_contact_no', models.CharField(max_length=15)),
                ('address', models.TextField()),
            ],
        ),
    ]