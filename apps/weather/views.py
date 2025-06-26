from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from rest_framework.serializers import ValidationError
from drf_yasg import openapi
from apps.weather.services import WeatherService
from django.conf import settings
from .models import WeatherQuery
from .serializers import WeatherQuerySerializer
from .ratelimit import TenPerMinuteThrottle
from .tasks import save_weather_query


class WeatherAPIView(APIView):
    permission_classes = [AllowAny]
    throttle_classes = [TenPerMinuteThrottle]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "city",
                openapi.IN_QUERY,
                description="Nome da cidade. Ex: 'Sao Luis' ou 'Sao Luis,BR'",
                type=openapi.TYPE_STRING,
                required=True,
            )
        ],
        responses={200: "Retorna dados do clima da cidade."},
    )
    def get(self, request):
        city = request.query_params.get("city")
        if not city:
            return Response({"error": "City is required"}, status=400)

        try:
            weather_service = WeatherService(
                api_key=settings.OPENWEATHER_API_KEY,
                base_url=settings.WEATHER_URL
            )

            weather_data = weather_service.get_weather(city)

        except Exception:
            raise ValidationError(
                {"error": f"Nao foi possivel obter os dados do clima da Cidade: {city}"}
            )

        save_weather_query.delay(city, weather_data)

        return Response(weather_data, status=200)


class WeatherHistoryAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        history = WeatherQuery.objects.all().order_by('-created_at')[:10]
        serializer = WeatherQuerySerializer(history, many=True)
        return Response(serializer.data)
