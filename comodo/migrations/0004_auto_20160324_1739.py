# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-24 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comodo', '0003_auto_20160323_0304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'not_rezerved'), (1, 'rezerved'), (2, 'given'), (3, 'izin_ver')]),
        ),
    ]
