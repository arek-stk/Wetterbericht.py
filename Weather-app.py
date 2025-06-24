import requests

API_Key = "17ac6b96e482d7ed6e1722ccec8fc311"
lon = "11.57549"
lat = "48.13743"
request_url= f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_Key}'

response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    print(data)
    weather_description = data["weather"][0]["description"]
    temperature = round(data["main"]["temp"]-273.15)
    luftfeuchtigkeit = data["main"]["humidity"]
    city = data["name"]
    country = data["sys"]["country"]
    Celsius = "°C"
    print(f'Stadt:{city}')
    print(f'Land:{country}')
    print(f'Temperatur:{temperature}{Celsius}')
    print(f'Wetterstatus:{weather_description}')
    print(f'luftfeuchtigkeit:{luftfeuchtigkeit}')
else:
    print("Fehler")
