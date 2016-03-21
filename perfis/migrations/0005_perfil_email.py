# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0004_auto_20160320_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='email',
            field=models.EmailField(max_length=255, default=1),
            preserve_default=False,
        ),
    ]
