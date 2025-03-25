import requests

class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city_name, units="metric"):
        params = {
            "q": city_name,
            "appid": self.api_key,
            "units": units
        }
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return None

# Example usage:
# Replace 'your_api_key_here' with your OpenWeatherMap API key
if __name__ == "__main__":
    api_key = "your_api_key_here"
    weather_api = WeatherAPI(api_key)
    city = "London"
    weather_data = weather_api.get_weather(city)
    if weather_data:
        print(weather_data)