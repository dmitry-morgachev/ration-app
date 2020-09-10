from django.db import models


class Image(models.Model):
    dish = models.ForeignKey(
        'Dish',
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Блюдо'
    )

    image = models.ImageField(
        upload_to='dish_images'
    )

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return f'{self.dish.name} - {self.image.name}'
