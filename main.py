import requests

city = input("What is the city you wanna check?: ")
api_key = "1099801032105d29423416bef379a595"
response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric")
print(response.status_code)
data = response.json()
print(data)
temperature = data['main']['temp']
description = data['weather'][0]['description']
city_name = data['name']

print(f"The weather in {city_name} is {description} with a temperature of {temperature}°C.")    

