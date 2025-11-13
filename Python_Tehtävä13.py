import requests
import json

city_name = input("Enter municipality name: ")
API = "3973990f0863b548bf7c3bbaa254e050"

req = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API}&units=metric"

try:
    ans = requests.get(req)
    if ans.status_code==200:
        ans = requests.get(req).json()
        weather_data = ans["weather"][0]
        description = weather_data["description"]

        temperature_data = ans["main"]["temp"]

        #print("Weather: " + ans["weather"]["description"])

        print("Weather: " + description)
        print(f"Temperature: {temperature_data} Celcius")

except requests.exceptions.RequestException as e:
    print("Weather search could not be completed")
