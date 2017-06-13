# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.contrib.postgres.fields.hstore
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestAggregate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False,
                                        verbose_name='ID')),
                ('test_text', models.CharField(max_length=20, blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),

    ]
