import requests
import json
import pandas as pd
import os


# Функция для загрузки данных о погоде
def download_weather_data(**kwargs):
    city = "London"
    api_key = os.getenv("WEATHER_API_KEY")  # Получение API ключа из переменных окружения
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    weather_data = response.json()
    file_path = '/tmp/weather_data.json'
    with open(file_path, 'w') as f:
        json.dump(weather_data, f)


# Функция для обработки данных о погоде
def process_weather_data(**kwargs):
    file_path = '/tmp/weather_data.json'
    with open(file_path, 'r') as f:
        weather_data = json.load(f)

    main_data = weather_data.get('main', {})  # Извлечение основного блока данных из ответа
    temp = main_data.get('temp', None)

    if temp is None:
        raise KeyError("Key 'temp' is missing in 'main' data")

    df = pd.DataFrame([main_data])  # Преобразование данных в DataFrame
    df['temp_celsius'] = df['temp'] - 273.15

    csv_path = '/tmp/processed_weather_data.csv'
    df.to_csv(csv_path, index=False)


def save_weather_data(**kwargs):
    csv_path = '/tmp/processed_weather_data.csv'
    parquet_path = '/tmp/weather.parquet'
    df = pd.read_csv(csv_path)
    df.to_parquet(parquet_path)
