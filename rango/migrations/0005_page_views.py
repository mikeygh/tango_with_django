# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_remove_page_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='views',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
