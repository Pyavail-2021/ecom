
from pickle import GET
from unicodedata import name
from django.shortcuts import render
from pip import main
import requests

# Create your views here.
def weather(request):
    city=request.GET.get('city')
    city="mumbai"
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=bc7730ccbd44e54070cd1c231102cdb1'
    req=requests.get(url).json()
    city_weather = {
        'city': req['name'],
        'temperature': req['main']['temp'],
        'description': req['weather'][0]['description'],
        'icon': req['weather'][0]['icon'],
        'weather': req['weather'][0]['main'],
        'country': req['sys']['country'],
        'sunrise': req['sys']['sunrise'],
        'sunset': req['sys']['sunset'],
        'wind': req['wind']['speed'],
        'clouds': req['clouds']['all'],
        'humidity': req['main']['humidity'],
        'view': req['name'],
        'id': req['id'],

    }
    context={'city_weather':city_weather}
    print(context)
    return render(request , 'weather/weather.html', context)
