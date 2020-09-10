from rest_framework import viewsets

from apps.dishes.api.serializers import UserRationSerializer
from apps.dishes.models import UserRation


class UserRationViewSet(viewsets.ModelViewSet):
    queryset = UserRation.objects.all()
    serializer_class = UserRationSerializer
