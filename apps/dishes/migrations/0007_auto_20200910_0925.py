# Generated by Django 2.2.16 on 2020-09-10 09:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0006_auto_20200910_0416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userration',
            name='eaten_in',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 10, 9, 25, 30, 284938, tzinfo=utc), verbose_name='Когда съедено'),
        ),
    ]
