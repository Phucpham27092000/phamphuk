import requests

DATA = []
def getWeatherData(city):    
    url = 'https://api.openweathermap.org/data/2.5/weather?q='
    apiKey = '6d30679d1f0b8aa1b5deb986899bf20c'
    get_api = url + city + '&appid=' + apiKey
    data = requests.get(get_api).json()
    
    City = data['name']
    Country = data['sys']['country']
    weatherState = data['weather'][0]['main']
    Cdegree = data['main']['temp']-273.15
    DoC = str(round(Cdegree,2)) + "°C"
    Fdegree = (data['main']['temp']-273.15)*1.8+32
    DoF = str(round(Fdegree,2)) + "°F"
    Humidity = data['main']['humidity']  
    windSPD = data['wind']['speed']

    DATA.append(City)
    DATA.append(Country)
    DATA.append(weatherState)
    DATA.append(DoC)
    DATA.append(DoF)
    DATA.append(Humidity)
    DATA.append(windSPD)
    # print(DATA)


