# Generated by Django 2.2.16 on 2020-09-10 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0003_auto_20200910_0340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishration',
            name='dish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ration', to='dishes.Dish', verbose_name='Блюдо'),
        ),
        migrations.AlterField(
            model_name='image',
            name='dish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='dishes.Dish', verbose_name='Блюдо'),
        ),
        migrations.AlterField(
            model_name='item',
            name='ration',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='items', to='dishes.DishRation', verbose_name='Блюдо в рационе'),
        ),
    ]
