from django.db import models
from django.db.models import Count


class DishManager(models.Manager):
    def get_most_eaten(self):
        return self.annotate(
            count=Count('ration__ration_dishes')
        ).order_by(
            '-count'
        ).first()


class Dish(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=255,
    )

    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True
    )

    recipe = models.TextField(
        verbose_name='Рецепт',
        blank=True,
        null=True
    )

    objects = DishManager()

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return self.name
