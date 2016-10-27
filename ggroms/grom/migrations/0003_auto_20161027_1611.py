# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-27 10:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grom', '0002_auto_20161026_2238'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgentAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='AgentDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('father_name', models.CharField(max_length=50)),
                ('mother_name', models.CharField(max_length=50)),
                ('pancard', models.CharField(max_length=50, null=True)),
                ('address', models.TextField()),
                ('date_of_birth', models.DateField()),
                ('contact_no', models.CharField(max_length=15)),
                ('alternate_contact_no', models.CharField(max_length=15, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('date_of_joining', models.DateField()),
                ('percentage_alloted', models.FloatField()),
                ('introducer_percentage', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='AgentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='NominiDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
                ('relation', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('contact_no', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('belong_to', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='agentdetail',
            name='Nomini_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grom.NominiDetail'),
        ),
        migrations.AddField(
            model_name='agentdetail',
            name='account_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grom.AgentAccount'),
        ),
        migrations.AddField(
            model_name='agentdetail',
            name='introducor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grom.AgentDetail'),
        ),
        migrations.AddField(
            model_name='agentdetail',
            name='type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grom.AgentType'),
        ),
    ]
