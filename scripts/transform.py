import json
import pandas as pd
import os

def transform_weather(raw_file_path):
    """
    Transform raw weather JSON into structured CSV format.
    Returns processed file path.
    """

    with open(raw_file_path, "r") as f:
        data = json.load(f)

    record = {
        "city": data.get("name"),
        "temperature": data.get("main", {}).get("temp"),
        "humidity": data.get("main", {}).get("humidity"),
        "weather": data.get("weather")[0].get("description")
    }

    df = pd.DataFrame([record])

    os.makedirs("data/processed", exist_ok=True)

    processed_file_path = raw_file_path.replace("raw", "processed").replace(".json", ".csv")

    df.to_csv(processed_file_path, index=False)

    return processed_file_path