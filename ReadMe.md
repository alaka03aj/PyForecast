# PyForecast
## Weather Forecasting Tool - Using Python
## Made for GitHub Copilot Hackathon

## Description
This is a simple weather forecasting tool that uses the OpenWeatherMap API to retrieve weather data for a given city using Python. The tool displays current weather conditions, as well as the upcoming weather of the day in a 3 hour interval basis. 

## Tools Used
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Requests](https://img.shields.io/badge/requests-3670A0?style=for-the-badge&logo=requests&logoColor=ffdd54)
![OpenWeatherMap](https://img.shields.io/badge/openweathermap-ED8B00?style=for-the-badge&logo=openweathermap&logoColor=ffdd54)
<!-- ![Matplotlib](https://img.shields.io/badge/matplotlib-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) -->

## Installation
To install the tool, simply clone the repository and run the following command in the terminal:
```
# Warning: Make sure to have Python installed on your system.
py weather.py <cityname>
```

Make sure to have the following libraries installed:
- [Requests](https://docs.python-requests.org/en/master/)
```
pip install requests
```
or
```
py -m pip install requests
```

## Usage
To use the tool, simply enter the name of the city you wish to retrieve weather data for. The tool will then display the current weather conditions, as well as the forecast for the rest of the day.
```
py weather.py <cityname>
```

## Use Cases
This tool can be used to retrieve weather data for any city in the world. It can be used to plan trips, or to simply check the weather in your area.

## Credits
- [OpenWeatherMap API](https://openweathermap.org/api) to retrieve weather data for a given city.
<!-- - The tool uses the [Matplotlib](https://matplotlib.org/) library to display a graph of the temperature and humidity for the next 5 days. -->
- [Requests](https://docs.python-requests.org/en/master/) library to make HTTP requests to the OpenWeatherMap API.
- [JSON](https://docs.python.org/3/library/json.html) library to parse the JSON data retrieved from the OpenWeatherMap API.
- [Datetime](https://docs.python.org/3/library/datetime.html) library to convert the UNIX timestamp to a readable date and time.
- [Sys](https://docs.python.org/3/library/sys.html) library to retrieve the city name from the command line arguments.
- [Github Copilot](https://copilot.github.com/) to help with the code.

## Team Name - Girl Boss
### Team Members
- [Alaka A J](github.com/alaka03aj)