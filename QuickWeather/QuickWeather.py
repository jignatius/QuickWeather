#! python3
# QuickWeather.py - Prints the weather for a location from the command line

import json, requests, sys

def current(location):
    # Download the JSON data from OpenWeatherMap.org's API
    url = "http://api.openweathermap.org/data/2.5/weather?q=%s&units=metric&APPID=2c72b19f0de8d493671eb73e9c4cf39c" % (location)
    response = requests.get(url)

    # Load JSON data into a Python variable
    weatherData = json.loads(response.text)

    # Print weather description
    w = weatherData['weather']
    print('Current weather in %s' % (location))
    print()
    print(w[0]['main'], '-', w[0]['description'])
    m = weatherData['main']
    print('Current temperature is %3.2fC but feels like %3.2fC' % (m['temp'], m['feels_like']))
    print()

def forecast(location):
    url = "http://api.openweathermap.org/data/2.5/forecast?q=%s&APPID=2c72b19f0de8d493671eb73e9c4cf39c" % (location)
    response = requests.get(url)

    # Load JSON data into a Python variable
    weatherData = json.loads(response.text)

    w = weatherData['list']
    print('Tomorrow:')
    print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
    print()
    print('Day after tomorrow:')
    print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
    print()

def main():
    # Compute location from the command line arguments
    if len(sys.argv) < 2:
        print('Usage: QuickWeather.py location')
        sys.exit()
    location = ' '.join(sys.argv[1:])
    current(location)
    forecast(location)

if __name__ == "__main__":
    main()