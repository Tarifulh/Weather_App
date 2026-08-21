import requests

while True:
 city = input("Enter city name: ").lower()

 if city.lower() == "q":
   print("Goodbye!")
   break

 # API 1: CITY - COORDINATES
 response = requests.get(
     "https://geocoding-api.open-meteo.com/v1/search",
     params={
         "name": city
     }
 )

 data = response.json()
 if not data.get("results"): 
    print("City not found. Try nearby!")
 else:

  latitude = data["results"][0]["latitude"]
  longitude = data["results"][0]["longitude"]


  # API 2: COORDINATES - WEATHER
  weather_response = requests.get(
      "https://api.open-meteo.com/v1/forecast",
      params={
          "latitude": latitude,
          "longitude": longitude,
          "current": "temperature_2m,relative_humidity_2m,apparent_temperature,wind_speed_10m,precipitation,snowfall,visibility,weather_code"
      }
  )

  weather_data = weather_response.json()

 current = weather_data["current"]

 temperature = current["temperature_2m"]
 humidity = current["relative_humidity_2m"]
 feels_like = current["apparent_temperature"]
 wind_speed = current["wind_speed_10m"]
 precipitation = current["precipitation"]
 snowfall = current["snowfall"]
 visibility = current["visibility"]
 weather_code = current["weather_code"]
 weather_conditions = {
   0: "Clear sky",
   1: "Mainly clear",
   2: "Partly cloudy",
   3: "Overcast",
   45: "Fog",
   48: "Depositing rime fog",
   51: "Light drizzle",
   53: "Moderate drizzle",
   55: "Dense drizzle",
   61: "Slight rain",
   63: "Moderate rain",
   65: "Heavy rain",
   71: "Slight snow",
   73: "Moderate snow",
   75: "Heavy snow",
   80: "Slight rain showers",
   81: "Moderate rain showers",
   82: "Violent rain showers",
   95: "Thunderstorm",
   96: "Thunderstorm with slight hail",
   99: "Thunderstorm with heavy hail"
 }

 print()
 print(f"Weather in {city}")
 print(f"Temperature: {temperature}^C")
 print(f"Feels like: {feels_like}^C")
 print(f"Humidity: {humidity}%")
 print(f"Wind speed: {wind_speed}km/h")
 print(f"precipitation: {precipitation}mm")
 print(f"Snowfall: {snowfall}mm")
 print(f"Visibility: {visibility}")
 print()
 condition = weather_conditions.get(weather_code, "Unknown")
 print(f"Condition: {condition}")