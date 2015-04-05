# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20150405_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wine',
            name='winery',
            field=models.ForeignKey(related_name='wines', to='api.Winery'),
            preserve_default=True,
        ),
    ]
