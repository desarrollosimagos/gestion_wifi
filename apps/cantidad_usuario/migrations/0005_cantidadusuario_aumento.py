# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cantidad_usuario', '0004_remove_cantidadusuario_user_create'),
    ]

    operations = [
        migrations.AddField(
            model_name='cantidadusuario',
            name='aumento',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
