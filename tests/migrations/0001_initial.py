# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-05-25 19:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('justeventme', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestEventType',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('justeventme.baseevent',),
        ),
    ]