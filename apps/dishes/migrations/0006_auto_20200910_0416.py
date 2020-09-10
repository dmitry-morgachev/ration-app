# Generated by Django 2.2.16 on 2020-09-10 04:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0005_auto_20200910_0414'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='ration',
            new_name='ration_dish',
        ),
        migrations.RenameField(
            model_name='userration',
            old_name='ration_dishes',
            new_name='ration_dish',
        ),
        migrations.AlterField(
            model_name='userration',
            name='eaten_in',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 10, 4, 16, 1, 251857, tzinfo=utc), verbose_name='Когда съедено'),
        ),
    ]