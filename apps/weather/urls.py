from django.urls import path
from .views import WeatherAPIView, WeatherHistoryAPIView

urlpatterns = [
    path('weather/', WeatherAPIView.as_view(), name='weather'),
    path('weather/history/', WeatherHistoryAPIView.as_view(), name='weather-history'),
]
