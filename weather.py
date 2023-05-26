import requests
import constants
import json
import sys
from datetime import datetime, timedelta

weather_icons = {
    "01d": "☀️",
    "01n": "🌙",
    "02d": "⛅",
    "02n": "⛅",
    "03d": "☁️",
    "03n": "☁️",
    "04d": "☁️",
    "04n": "☁️",
    "09d": "🌧️",
    "09n": "🌧️",
    "10d": "🌦️",
    "10n": "🌦️",
    "11d": "⛈️",
    "11n": "⛈️",
    "13d": "❄️",
    "13n": "❄️",
    "50d": "🌫️",
    "50n": "🌫️",
}

# Get weather data from openweathermap.org


def get_weather(city):
    api_key = constants.API_KEY
    weather_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(weather_url, params=params)
        data = json.loads(response.text)
        # prints the current weather data
        print(f"Weather in {city}: {data['weather'][0]['description']}")
        print(f"{weather_icons[data['weather'][0]['icon']]}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Feels like: {data['main']['feels_like']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind: {data['wind']['speed']} m/s")

        # prints the forecast for the rest of the day
        get_forecast(city, api_key)

    except requests.exceptions.ConnectionError:
        print("Something went wrong. Check your internet connection or try again later.")
    except requests.exceptions.Timeout:
        print(
            "Oh no! Seems like the server is taking too long to respond. Try again later.")
    except:
        print("Seems like you entered wrong city name. Try again.")


def get_forecast(city, api_key):
    forecast_url = "https://api.openweathermap.org/data/2.5/forecast"
    forecast_params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    try:
        forecast_response = requests.get(forecast_url, params=forecast_params)
        forecast_data = json.loads(forecast_response.text)
        forecast_temperatures = []
        forecast_humidity = []
        forecast_dates = []
        forecast_icons = []
        now = datetime.now()
        for forecast in forecast_data['list']:
            forecast_date = datetime.fromtimestamp(forecast['dt'])
            if forecast_date.date() == now.date() and forecast_date >= now:
                forecast_dates.append(forecast_date)
                forecast_temperatures.append(forecast['main']['temp'])
                forecast_humidity.append(forecast['main']['humidity'])
                forecast_icons.append(forecast['weather'][0]['icon'])

        print("\nWeather Forecast for the rest of the day:")
        for i in range(len(forecast_dates)):
            forecast_time = forecast_dates[i].strftime("%H:%M")
            temperature = forecast_temperatures[i]
            humidity = forecast_humidity[i]
            weather_icon = weather_icons.get(forecast_icons[i], "")
            print(
                f"{forecast_time} - {weather_icon} Temperature: {temperature}°C, Humidity: {humidity}%")
    except:
        print("Something went wrong. Try again.")


def main():
    # print(sys.argv) - prints the list of arguments passed to the script
    if len(sys.argv) < 2:
        print("Usage: py weather.py <city-name>")
        sys.exit(1)

    city = sys.argv[1]
    get_weather(city)


if __name__ == "__main__":
    main()
