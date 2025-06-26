import logging
import requests
from django.core.cache import cache


class WeatherService:
    def __init__(self, api_key: str, base_url: str, cache_backend=None):
        self.api_key = api_key
        self.base_url = base_url
        self.cache = cache_backend or cache
        self.logger = logging.getLogger("weather_api")

    def _build_cache_key(self, city: str) -> str:
        return f"weather:{city.lower().replace(' ', '_')}"

    def _build_params(self, city: str) -> dict:
        return {
            "q": city,
            "appid": self.api_key,
            "units": "metric",
            "lang": "pt_br",
        }

    def get_weather(self, city: str) -> dict:
        if not city:
            self.logger.error("Parameter 'city' is required.")
            raise ValueError("City name is required.")

        cache_key = self._build_cache_key(city)
        cached = self.cache.get(cache_key)

        if cached:
            self.logger.info("Cache register", extra={"city": city, "cache_key": cache_key})
            return cached

        url = f"{self.base_url}/data/2.5/weather"
        params = self._build_params(city)

        self.logger.info(
            "Request data from OpenWeather.", extra={"url": url, "params": params}
        )

        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            self.logger.error(
                "Error fetching data from OpenWeather.",
                extra={"error": str(e), "city": city, "params": params},
            )
            raise Exception(f"Failed to fetch weather data: {str(e)}")

        data = response.json()
        self.cache.set(cache_key, data, timeout=600)
        self.logger.info(
            "Response cached successfully.",
            extra={"city": city, "cache_key": cache_key},
        )

        return data
