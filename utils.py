import requests

# ✅ Weatherstack API Key (use your actual key)
WEATHERSTACK_API_KEY = "71a3c1cd61ee50f4d26fa6f49a63177d"

def get_weather_data(location):
    try:
        url = "http://api.weatherstack.com/current"
        params = {
            "access_key": WEATHERSTACK_API_KEY,
            "query": location,
            "units": "m"
        }

        response = requests.get(url, params=params)
        data = response.json()
        print("🌦 Weatherstack API response:", data)

        # Check for API errors or missing data
        if not data.get("current") or data.get("success") is False:
            print("⚠️ Weatherstack returned no data or error.")
            return None

        return {
            "temp": data["current"]["temperature"],
            "description": data["current"]["weather_descriptions"][0],
            "humidity": data["current"]["humidity"],
            "lat": data["location"]["lat"],
            "lon": data["location"]["lon"]
        }

    except Exception as e:
        print("❌ Exception in get_weather_data:", e)
        return None


def get_aqi_data(location):
    try:
        weather_info = get_weather_data(location)
        if not weather_info:
            return None

        lat = weather_info["lat"]
        lon = weather_info["lon"]

        url = "https://air-quality-api.open-meteo.com/v1/air-quality"
        params = {
            "latitude": lat,
            "longitude": lon,
            "hourly": "pm10",
            "timezone": "auto"
        }

        response = requests.get(url, params=params)
        data = response.json()
        print("🌫 Open-Meteo AQI response:", data)

        pm10_values = data.get("hourly", {}).get("pm10", [])
        if not pm10_values:
            print("⚠️ No PM10 data available.")
            return None

        pm10 = pm10_values[0]

        # Convert PM10 to rough AQI-like scale
        if pm10 <= 50:
            aqi = 50    # Good
        elif pm10 <= 100:
            aqi = 100   # Moderate
        elif pm10 <= 150:
            aqi = 150   # Unhealthy for sensitive groups
        elif pm10 <= 200:
            aqi = 200   # Unhealthy
        else:
            aqi = 300   # Very Unhealthy

        return {
            "aqi": aqi,
            "pm10": pm10,
            "lat": lat,
            "lon": lon
        }

    except Exception as e:
        print("❌ Exception in get_aqi_data:", e)
        return None
