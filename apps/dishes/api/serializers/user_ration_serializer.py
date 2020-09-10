from rest_framework import serializers

from apps.dishes.models import UserRation


class UserRationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRation
        fields = '__all__'


class UserCaloriesSerializer(serializers.Serializer):
    calories = serializers.FloatField()

