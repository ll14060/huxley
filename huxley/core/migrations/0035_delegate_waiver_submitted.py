# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-07-31 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('core', '0034_secretariatmember'), ]

    operations = [
        migrations.AddField(
            model_name='delegate',
            name='waiver_submitted',
            field=models.BooleanField(default=False), ),
    ]
