from flask import Flask, jsonify, request
import requests
from prometheus_client import generate_latest
from prometheus_metrics import WEATHER_REQUESTS, WEATHER_REQUEST_LATENCY

app = Flask(__name__)

API_KEY = "YOUR_WEATHER_API_KEY"
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route("/weather")
@WEATHER_REQUEST_LATENCY.time()
def get_weather():
    WEATHER_REQUESTS.inc()
    city = request.args.get("city", "London")

    response = requests.get(
        WEATHER_URL,
        params={"q": city, "appid": API_KEY, "units": "metric"}
    )
    return jsonify(response.json())

@app.route("/metrics")
def metrics():
    return generate_latest()
