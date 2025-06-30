import requests

def get_coordinates(city):
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city, "count": 1}
    response = requests.get(geo_url, params=params)
    if response.status_code == 200:
        data = response.json()
        if "results" in data and data["results"]:
            latitude = data["results"][0]["latitude"]
            longitude = data["results"][0]["longitude"]
            return latitude, longitude
        else:
            print("City not found.")
            return None, None
    else:
        print("Geocoding API error:", response.status_code)
        return None, None

def interpret_weather_code(code):
    # Based on Open-Meteo weather codes: https://open-meteo.com/en/docs
    weather_conditions = {
        0: "Clear sky ☀️",
        1: "Mainly clear 🌤️",
        2: "Partly cloudy ⛅",
        3: "Overcast ☁️",
        45: "Foggy 🌫️",
        48: "Depositing rime fog 🌫️",
        51: "Light drizzle 🌦️",
        53: "Moderate drizzle 🌦️",
        55: "Dense drizzle 🌧️",
        56: "Light freezing drizzle 🧊🌧️",
        57: "Dense freezing drizzle 🧊🌧️",
        61: "Slight rain 🌦️",
        63: "Moderate rain 🌧️",
        65: "Heavy rain 🌧️",
        66: "Light freezing rain 🧊🌧️",
        67: "Heavy freezing rain 🧊🌧️",
        71: "Slight snow fall 🌨️",
        73: "Moderate snow fall 🌨️",
        75: "Heavy snow fall 🌨️",
        77: "Snow grains 🌨️",
        80: "Slight rain showers 🌦️",
        81: "Moderate rain showers 🌦️",
        82: "Violent rain showers ⛈️",
        85: "Slight snow showers 🌨️",
        86: "Heavy snow showers 🌨️",
        95: "Thunderstorm ⛈️",
        96: "Thunderstorm with slight hail ⛈️",
        99: "Thunderstorm with heavy hail ⛈️"
    }
    return weather_conditions.get(code, "Unknown weather")

def get_weather(latitude, longitude):
    weather_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True
    }
    response = requests.get(weather_url, params=params)
    if response.status_code == 200:
        data = response.json()
        temperature = data['current_weather']['temperature']
        wind_speed = data['current_weather']['windspeed']
        weather_code = data['current_weather'].get('weathercode', None)
        print(f"🌡️ Temperature: {temperature}°C")
        print(f"💨 Wind Speed: {wind_speed} km/h")
        if weather_code is not None:
            condition = interpret_weather_code(weather_code)
            print(f"🌦️ Weather Condition: {condition}")
    else:
        print("Weather API error:", response.status_code)

def main():
    city = input("Enter your city name: ")
    lat, lon = get_coordinates(city)
    if lat and lon:
        print(f"\n📍 Location: {city} (Lat: {lat}, Lon: {lon})")
        get_weather(lat, lon)

if __name__ == "__main__":
    main()
