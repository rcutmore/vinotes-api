# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_note_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='winery',
            options={'verbose_name_plural': 'wineries'},
        ),
        migrations.RenameField(
            model_name='trait',
            old_name='description',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='wine',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='winery',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='note',
            name='created',
        ),
        migrations.RemoveField(
            model_name='winery',
            name='description',
        ),
        migrations.AddField(
            model_name='note',
            name='tasted',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='wine',
            unique_together=set([('winery', 'name', 'vintage')]),
        ),
        migrations.RemoveField(
            model_name='wine',
            name='description',
        ),
    ]
