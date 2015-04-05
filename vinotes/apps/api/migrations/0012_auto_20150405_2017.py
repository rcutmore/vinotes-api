# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20150405_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='color_traits',
            field=models.ManyToManyField(null=True, related_name='color_notes', to='api.Trait', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='note',
            name='finish_traits',
            field=models.ManyToManyField(null=True, related_name='finish_notes', to='api.Trait', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='note',
            name='nose_traits',
            field=models.ManyToManyField(null=True, related_name='nose_notes', to='api.Trait', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='note',
            name='taste_traits',
            field=models.ManyToManyField(null=True, related_name='taste_notes', to='api.Trait', blank=True),
            preserve_default=True,
        ),
    ]
