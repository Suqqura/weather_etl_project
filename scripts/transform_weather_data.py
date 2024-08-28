import os
import pandas as pd
import json

# file paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_file_path = os.path.join(BASE_DIR, 'data/raw_weather_data.json')
output_file_path = os.path.join(BASE_DIR, 'data/transformed_weather_data.csv')

def transform_weather_data():
    try:
        # data load
        with open(input_file_path, 'r') as f:
            data = json.load(f)
        
        # to df
        df = pd.DataFrame([{
            'timestamp': data['timestamp'],
            'city': data['name'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],
            'weather': data['weather'][0]['description']
        }])

        # save transformed data to csv
        df.to_csv(output_file_path, mode='a', header=not os.path.exists(output_file_path), index=False)
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        raise
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    transform_weather_data()
