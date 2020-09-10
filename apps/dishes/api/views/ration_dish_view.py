from django.db.models import Func, F
from rest_framework import viewsets

from apps.dishes.api.serializers import RationDishSerializer
from apps.dishes.models import RationDish


class RationDishViewSet(viewsets.ModelViewSet):
    queryset = RationDish.objects.all()
    serializer_class = RationDishSerializer

    def get_queryset(self):
        calories = self.request.query_params.get('calories', None)

        if calories is not None:
            nearest_dish_by_calories = self.queryset.annotate(
                abs_diff=Func(F('items__calories') - calories, function='ABS')
            ).order_by('abs_diff')[:1]

            return nearest_dish_by_calories

        return self.queryset


