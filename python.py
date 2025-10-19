import requests

api_key = "09db3556b993a5d7d4abf78542a142a3"

city = input("Enter the city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

weather_icons = {
    "Clear": "☀️",
    "Clouds": "☁️",
    "Rain": "🌧️",
    "Drizzle": "🌦️",
    "Thunderstorm": "⛈️",
    "Snow": "❄️",
    "Mist": "🌫️",
    "Smoke": "💨",
    "Haze": "🌫️",
    "Fog": "🌫️",
    "Dust": "🌪️",
    "Sand": "🏜️",
    "Ash": "🌋",
    "Squall": "💨",
    "Tornado": "🌪️"
}

try:
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        condition = weather['main']
        icon = weather_icons.get(condition, "🌈")  # default icon

        print(f"""
🌆 City: {city.title()}
{icon} Weather: {weather['description'].title()}
🌡️ Temperature: {main['temp']}°C
🤗 Feels Like: {main['feels_like']}°C
💧 Humidity: {main['humidity']}%
""")
    else:
        print("City not found or error fetching data.")
except requests.exceptions.RequestException as e:
    print("Error fetching data:", e)