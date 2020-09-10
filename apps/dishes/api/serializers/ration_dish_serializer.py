from rest_framework import serializers

from apps.dishes.api.serializers import DishSerializer
from apps.dishes.models import RationDish


class RationDishSerializer(serializers.ModelSerializer):
    dish = DishSerializer()
    total_calories = serializers.SerializerMethodField()

    class Meta:
        model = RationDish
        fields = ['dish', 'total_calories']

    @staticmethod
    def get_total_calories(obj):
        return obj.get_total_calories()
