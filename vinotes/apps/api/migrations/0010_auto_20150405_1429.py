# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20150329_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='taster',
            field=models.ForeignKey(related_name='notes', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
