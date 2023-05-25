import requests
import constants
import json
import sys

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
        print(f"Weather in {city}: {data['weather'][0]['description']}")
        print(f"{weather_icons[data['weather'][0]['icon']]}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Feels like: {data['main']['feels_like']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind: {data['wind']['speed']} m/s")
    except requests.exceptions.ConnectionError:
        print("Something went wrong. Check your internet connection or try again later.")
    except requests.exceptions.Timeout:
        print("Oh no! Seems like the server is taking too long to respond. Try again later.")
    except:
        print("Seems like you entered wrong city name. Try again.")

def main():
    # print(sys.argv) - prints the list of arguments passed to the script
    if len(sys.argv) < 2:
        print("Usage: py weather.py <city-name>")
        sys.exit(1)

    city = sys.argv[1]
    get_weather(city)

if __name__ == "__main__":
    main()
