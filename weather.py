import requests
import constants
import json
import sys


# Get weather data from openweathermap.org
def get_weather(city):
    api_key = constants.API_KEY
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    
    try:
        response = requests.get(base_url, params=params)
        data = json.loads(response.text)
        print(f"Weather in {city}: {data['weather'][0]['description']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Feels like: {data['main']['feels_like']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind: {data['wind']['speed']} m/s")
    except:
        print("Something went wrong. Check your internet connection or try again later.")


if __name__ == "__main__":
    # print(sys.argv) - prints the list of arguments passed to the script
    if len(sys.argv) < 2:
        print("Usage: python weather.py <city-name>")
        sys.exit(1)

    city = sys.argv[1]
    get_weather(city)
