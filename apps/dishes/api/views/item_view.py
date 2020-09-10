from rest_framework import viewsets

from apps.dishes.api.serializers import ItemSerializer
from apps.dishes.models import Item


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
