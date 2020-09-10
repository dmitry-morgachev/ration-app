from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class UserRation(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='ration',
        verbose_name='Пользователь'
    )

    ration_dish = models.ForeignKey(
        'RationDish',
        on_delete=models.DO_NOTHING,
        related_name='ration_dishes',
        verbose_name='Блюдо'
    )

    eaten_in = models.DateTimeField(
        verbose_name='Когда съедено',
        default=timezone.now()
    )

    class Meta:
        verbose_name = 'Рацион пользователя',
        verbose_name_plural = 'Рационы пользователей'

    def __str__(self):
        return f'[{self.eaten_in}] {self.user.username} - {self.ration_dish.dish.name}'
