# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_note_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='color_traits',
            field=models.ManyToManyField(null=True, blank=True, to='api.Trait', related_name='color_traits'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='note',
            name='finish_traits',
            field=models.ManyToManyField(null=True, blank=True, to='api.Trait', related_name='finish_traits'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='note',
            name='nose_traits',
            field=models.ManyToManyField(null=True, blank=True, to='api.Trait', related_name='nose_traits'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='note',
            name='taste_traits',
            field=models.ManyToManyField(null=True, blank=True, to='api.Trait', related_name='taste_traits'),
            preserve_default=True,
        ),
    ]
