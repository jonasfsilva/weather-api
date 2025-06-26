from django.test import TestCase
from unittest.mock import patch, Mock
from apps.weather.services import WeatherService


class TestWeatherService(TestCase):
    def setUp(self):
        self.api_key = "dummy_api_key"
        self.base_url = "https://api.openweathermap.org"
        self.city = "Sao Luis"
        self.service = WeatherService(api_key=self.api_key, base_url=self.base_url)

    def test_get_weather_without_city_raises_error(self):
        with self.assertRaises(ValueError):
            self.service.get_weather("")

    @patch("apps.weather.services.requests.get")
    @patch("apps.weather.services.cache")
    def test_get_weather_success(self, mock_cache, mock_get):
        mock_cache.get.return_value = None

        expected_json = {
            "coord": {"lon": -44.3028, "lat": -2.5297},
            "weather": [
                {
                    "id": 802,
                    "main": "Clouds",
                    "description": "nuvens dispersas",
                    "icon": "03n",
                }
            ],
            "main": {
                "temp": 27.11,
                "feels_like": 30.29,
                "temp_min": 27.11,
                "temp_max": 27.11,
                "pressure": 1012,
                "humidity": 83,
                "sea_level": 1012,
                "grnd_level": 1011,
            },
            "name": "São Luís",
            "cod": 200,
        }

        mock_response = Mock()
        mock_response.ok = True
        mock_response.json.return_value = expected_json
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = self.service.get_weather(self.city)

        self.assertEqual(result["name"], "São Luís")
        self.assertEqual(result["main"]["temp"], 27.11)
        self.assertEqual(result["weather"][0]["description"], "nuvens dispersas")
