from django.contrib.auth.models import User
from django.db.models import Sum
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.dishes.api.serializers import UserSerializer, UserCaloriesSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=['get'], detail=True)
    def get_calories_today(self, request, pk=None):
        user = self.get_object()

        calories = UserCaloriesSerializer(
            user.ration.aggregate(
                calories=Sum('ration_dish__items__calories')
            )
        ).data

        return Response(calories)
