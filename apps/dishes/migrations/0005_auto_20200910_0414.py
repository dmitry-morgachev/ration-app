# Generated by Django 2.2.16 on 2020-09-10 04:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dishes', '0004_auto_20200910_0348'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DishRation',
            new_name='RationDish',
        ),
        migrations.CreateModel(
            name='UserRation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eaten_in', models.DateTimeField(default=datetime.datetime(2020, 9, 10, 4, 14, 15, 950389, tzinfo=utc), verbose_name='Когда съедено')),
                ('ration_dishes', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ration_dishes', to='dishes.RationDish', verbose_name='Блюдо')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ration', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': ('Рацион пользователя',),
                'verbose_name_plural': 'Рационы пользователей',
            },
        ),
    ]