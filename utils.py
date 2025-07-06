import requests

API_KEY = "2f432c0065bcef1a1ee158f3a5ac13e1"

def get_weather_data(location):
    try:
        print(f"\nSearching for location: {location}")
        url = f"http://api.weatherstack.com/current?access_key={API_KEY}&query={location}"
        print(f"Sending request to: {url}")
        res = requests.get(url).json()
        print("Weather API response:", res)

        if "error" in res:
            print(f"Weather API error: {res['error'].get('info')}")
            return None

        return {
            "temp": res["current"]["temperature"],
            "description": res["current"]["weather_descriptions"][0],
            "lat": res["location"]["lat"],
            "lon": res["location"]["lon"]
        }

    except Exception as e:
        print(f"Exception in get_weather_data: {e}")
        return None

def get_aqi_data(location):
    print("AQI data is not available in Weatherstack Free Plan.")
    return None
