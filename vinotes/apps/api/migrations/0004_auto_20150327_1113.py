# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_trait'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='color_traits',
            field=models.ManyToManyField(related_name='color_traits', blank=True, to='api.Trait'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='note',
            name='finish_traits',
            field=models.ManyToManyField(related_name='finish_traits', blank=True, to='api.Trait'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='note',
            name='nose_traits',
            field=models.ManyToManyField(related_name='nose_traits', blank=True, to='api.Trait'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='note',
            name='taste_traits',
            field=models.ManyToManyField(related_name='taste_traits', blank=True, to='api.Trait'),
            preserve_default=True,
        ),
    ]
