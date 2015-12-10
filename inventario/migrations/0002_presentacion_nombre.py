# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentacion',
            name='nombre',
            field=models.CharField(default='', max_length=45),
            preserve_default=False,
        ),
    ]
