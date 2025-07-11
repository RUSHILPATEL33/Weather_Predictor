import requests

api_key = ""
city = input("Enter a city name:")
url=f"http://dataservice.accuweather.com/locations/v1/cities/search?q={city}&apikey={api_key}"
def fetchLocationKey():
    location_url = url
    response = requests.get(location_url)
    data = response.json()
    if response.status_code == 200 and data:
        location_Key = data[0]['Key']
        return location_Key
    else:
      print("error fetching location key")
location_Key = fetchLocationKey()
weather_url = f"http://dataservice.accuweather.com/currentconditions/v1/{location_Key}?apikey={api_key}"
response = requests.get(weather_url)
if response.status_code == 200:
    weather_data = response.json()
    if weather_data:
      temperature = weather_data[0]['Temperature']['Metric']['Value']
      unit = weather_data[0]['Temperature']['Metric']['Unit']
      description = weather_data[0]['WeatherText']
      print(f"Current weather in {city}: {description}, {temperature}°c{unit}  ")
    else:
        print("No weather date found")
else:
  print (f"Failed to fetch weather. Status: {response.status_code}")
