# src/weather_api.py
import requests

def get_weather(api_key, city='London'):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    weather = data.get('weather', [{}])[0].get('description', 'No description')
    temp = data.get('main', {}).get('temp', 'No temperature data')
    return f"Weather: {weather}, Temperature: {temp}°C"

# Example usage
if __name__ == "__main__":
    api_key = 'YOUR_API_KEY'
    weather = get_weather(api_key)
    print(weather)
