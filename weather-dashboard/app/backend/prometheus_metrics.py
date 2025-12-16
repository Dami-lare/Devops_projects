from prometheus_client import Counter, Histogram

# Total number of requests to the weather endpoint
WEATHER_REQUESTS = Counter(
    "weather_requests_total",
    "Total number of weather API requests"
)

# Time spent processing weather requests
WEATHER_REQUEST_LATENCY = Histogram(
    "weather_request_latency_seconds",
    "Latency for weather API requests"
)
