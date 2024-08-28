import os
from dotenv import load_dotenv
import requests
import json
from datetime import datetime

# Load environment variables from the .env file
load_dotenv()

API_KEY = os.getenv('WEATHER_API_KEY')
CITY = 'Helsinki'
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

# absolute paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BASE_DIR, 'data/raw_weather_data.json')

def fetch_weather_data():
    try:
        response = requests.get(URL)
        response.raise_for_status()
        data = response.json()

        # timestamp to data
        data['timestamp'] = datetime.now().isoformat()

        # check if data directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # save to json
        with open(file_path, 'w') as f:
            json.dump(data, f)
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        raise

if __name__ == "__main__":
    fetch_weather_data()
