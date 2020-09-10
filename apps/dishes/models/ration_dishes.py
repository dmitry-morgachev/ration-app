from django.db import models
from django.db.models import Sum


class RationDish(models.Model):
    dish = models.ForeignKey(
        'Dish',
        on_delete=models.DO_NOTHING,
        related_name='ration',
        verbose_name='Блюдо'
    )

    class Meta:
        verbose_name = 'Блюдо в рационе'
        verbose_name_plural = 'Блюда в рационе'

    def __str__(self):
        return self.dish.name

    def get_total_calories(self):
        return self.items.aggregate(total_calories=Sum('calories'))
