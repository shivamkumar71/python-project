import requests

def get_coordinates(city):
    # Use geocoding API to get latitude and longitude for a given city name
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city, "count": 1}
    
    response = requests.get(geo_url, params=params)
    if response.status_code == 200:
        data = response.json()
        # Check if results are found for the city
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

def get_weather(latitude, longitude):
    # Use weather API to get current temperature and wind speed for given coordinates
    weather_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude, # Latitude of the location
        "longitude": longitude, # Longitude of the location
        "current_weather": True
    }

    response = requests.get(weather_url, params=params)
    if response.status_code == 200:
        data = response.json()
        # Extract and print temperature and wind speed from the API response
        temperature = data['current_weather']['temperature']
        wind_speed = data['current_weather']['windspeed']
        print(f"🌡️ Temperature: {temperature}°C")
        print(f"💨 Wind Speed: {wind_speed} km/h")
    else:
        print("Weather API error:", response.status_code)

def main():
    # Main function to prompt user for city and display weather information
    city = input("Enter your city name: ")
    lat, lon = get_coordinates(city)
    if lat and lon:
        print(f"\n📍 Location: {city} (Lat: {lat}, Lon: {lon})")
        get_weather(lat, lon)

if __name__ == "__main__":
    main()
