# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cantidad_usuario', '0003_auto_20150928_1133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cantidadusuario',
            name='user_create',
        ),
    ]
