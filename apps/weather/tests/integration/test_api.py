from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from apps.weather.models import WeatherQuery


class WeatherHistoryAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse(
            "weather-history"
        )

        for i in range(12):
            WeatherQuery.objects.create(city=f"City{i}", response={"temp": 25 + i})

    def test_returns_last_10_queries(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 10)
