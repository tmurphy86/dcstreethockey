# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-23 14:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0025_auto_20170323_1022'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stat',
            options={'ordering': ('matchup__week', 'matchup__time', 'team__team_name', 'player__last_name')},
        ),
    ]
