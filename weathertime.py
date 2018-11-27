import requests
from terminaltables import AsciiTable as ast

api_adress = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q=' #this is my 
city = input('City Name: ')
url = api_adress + city
json_data = requests.get(url).json()
wMain = json_data['weather'][0]['main']
wDesc = json_data['weather'][0]['description']
curTemp = str(int(json_data['main']['temp']- 273))+"°C"
maxTemp = "max: " + str(json_data['main']['temp_max'])
minTemp = "min: " + str(json_data['main']['temp_min'])
humidty = str(json_data['main']['humidity']) + "%"

table_info = [
    [wMain, wDesc, curTemp],
    [humidty,maxTemp, minTemp]
]
table = ast(table_info)
print(json_data)
print(table.table)
