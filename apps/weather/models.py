from django.db import models

from apps.core.models import BaseModel


class WeatherQuery(BaseModel):
    city = models.CharField(max_length=100)
    response = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-timestamp"]
