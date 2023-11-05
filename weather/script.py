# comment
import requests


def get_weather(city):
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'units': 'metric', 'appid': 'a06bd8016ba5c8dd7e7d1a4da947e00d'}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        temperature = data['main']['temp']
        weather = data['weather'][0]['description']
        print('Temperature -', temperature, 'C')
        print('Weather -', weather)
    except:
        print('No such city')


if __name__ == "__main__":
    city = input("Write the name of the city - ")
    get_weather(city)
