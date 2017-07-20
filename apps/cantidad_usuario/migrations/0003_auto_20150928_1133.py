# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cantidad_usuario', '0002_cantidadusuario_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cantidadusuario',
            name='codigo',
            field=models.CharField(max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
    ]
