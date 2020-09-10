from django.db.models import Sum
from rest_framework import viewsets

from apps.dishes.api.serializers import RationDishSerializer
from apps.dishes.models import RationDish


class RationDishViewSet(viewsets.ModelViewSet):
    queryset = RationDish.objects.all()
    serializer_class = RationDishSerializer

    def get_queryset(self):
        calories = self.request.query_params.get('calories', None)

        if calories and calories.isdigit() and not calories == '':
            dishes_calories = RationDish.objects.annotate(
                total_calories=Sum('items__calories')
            ).values('pk', 'total_calories')

            closest_dish_by_calories = min(
                dishes_calories, key=lambda x: abs(x['total_calories'] - int(calories))
            )

            return RationDish.objects.filter(pk=closest_dish_by_calories['pk'])

        return self.queryset


