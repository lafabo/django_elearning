# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20160612_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='files'),
        ),
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.FileField(upload_to='images'),
        ),
    ]
