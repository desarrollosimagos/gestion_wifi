# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CantidadUsuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField(null=True, blank=True)),
                ('aumento', models.IntegerField(null=True, blank=True)),
                ('subida_usu', models.IntegerField(null=True, blank=True)),
                ('bajada_usu', models.IntegerField(null=True, blank=True)),
                ('date_create', models.DateTimeField(auto_now_add=True, null=True)),
                ('hora', models.CharField(max_length=10, null=True, blank=True)),
                ('aumento', models.CharField(max_length=30, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
