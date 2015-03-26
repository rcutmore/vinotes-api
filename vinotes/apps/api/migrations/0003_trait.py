# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20150325_1104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trait',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('description', models.CharField(unique=True, max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
