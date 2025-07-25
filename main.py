import requests

city = input("What is the city you wanna check?: ")
api_key = input("Enter your OpenWeatherMap API key: ")
response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric")
# print(response.status_code) <--- to check whether the API key works
data = response.json()
temperature = data['main']['temp']
description = data['weather'][0]['description']
city_name = data['name']

print(f"The weather in {city_name} is {description} with a temperature of {temperature}°C.")    

