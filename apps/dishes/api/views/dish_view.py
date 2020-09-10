from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.dishes.api.serializers import DishSerializer
from apps.dishes.models import Dish


class DishViewSet(viewsets.ModelViewSet):
    model = Dish
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

    @action(methods=['get'], detail=False)
    def most_eaten_dish(self, request, pk=None):
        return Response(
            self.serializer_class(
                self.model.objects.get_most_eaten()
            ).data
        )
