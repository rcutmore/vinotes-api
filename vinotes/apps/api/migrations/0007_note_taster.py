# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0006_auto_20150328_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='taster',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=''),
            preserve_default=False,
        ),
    ]
