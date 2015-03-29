# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_note_taster'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 29, 11, 30, 6, 134185, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
