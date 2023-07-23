import requests
import get
class Weather:
    def __init__(self, city, api_key):
        self.city = city
        self.api_key = api_key
        self.url = "https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=fa61564e81adf3a3c9f2510026486e04"

    def town(self):
        self.city = misto
        a = requests.get(self.url.format(city=self.city))
        self.temp = a.json()['main']['temp']
        self.ftemp = a.json()['main']['feels_like']
        self.weather = a.json()['weather'][0]['description']

misto = get.b
w1 = Weather(misto, 'fa61564e81adf3a3c9f2510026486e04')
w1.town()


