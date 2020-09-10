from django.db import models


class Item(models.Model):
    ration_dish = models.ForeignKey(
        'RationDish',
        on_delete=models.DO_NOTHING,
        related_name='items',
        verbose_name='Блюдо в рационе',
        blank=True,
        null=True
    )

    name = models.CharField(
        verbose_name='Название продукта',
        max_length=255
    )

    calories = models.PositiveIntegerField(
        verbose_name='Количество калорий',
        help_text='в 100 граммах',
    )

    grams = models.PositiveIntegerField(
        verbose_name='Количество грамм',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Продукт',
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name
