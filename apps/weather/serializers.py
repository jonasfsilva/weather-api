from rest_framework import serializers
from .models import WeatherQuery


class WeatherQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherQuery
        fields = "__all__"
