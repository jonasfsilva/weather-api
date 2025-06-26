from rest_framework.throttling import AnonRateThrottle


class TenPerMinuteThrottle(AnonRateThrottle):
    rate = '10/min'
