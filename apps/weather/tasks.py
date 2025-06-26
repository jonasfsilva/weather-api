from celery import shared_task
from .models import WeatherQuery


@shared_task
def save_weather_query(city, response):
    WeatherQuery.objects.create(
        city=city,
        response=response
    )
