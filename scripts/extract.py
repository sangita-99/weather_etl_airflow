import requests
import json
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def extract_weather():
    """
    Extract weather data from OpenWeather API
    and save raw JSON file locally.
    Returns file path.
    """

    api_key = os.getenv("OPENWEATHER_API_KEY")

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": "28.6139",   # Delhi
        "lon": "77.2090",
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = f"data/raw/weather_{timestamp}.json"

    os.makedirs("data/raw", exist_ok=True)

    with open(file_path, "w") as f:
        json.dump(data, f)

    return file_path