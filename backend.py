import requests
import pygame
from terminaltables import AsciiTable
#pygame.init()
class Day:
    def __init__(self,temp,sum):
        self.temp = temp
        self.sum = sum
    def tellTemp(self):
        return (FtoC(self.temp))
    def tellSum(self):
        return self.sum

def FtoC(F):
    C = (int(F)-32) * (5/9)
    return str(C) + "°C"
'''
def makeTable(city,enn):
    api_adress = 'http://api.openweathermap.org/data/2.5/forecast?appid=0c42f7f6b53b244c78a418f4f181282a&q=' #this is mine!
    n = int(enn)
    if n > 39:
        return("You can't do that!!")

    url = api_adress + city
    json_data = requests.get(url).json()
    table_data = [
    ]
    days = [Day((json_data['list'][i]['main']['temp']),
                (json_data['list'][i]['weather'][0]['main']),
                (str(json_data['list'][i]['main']['humidity']))) for i in range(n)]
    for i in range(n):
        temp = [days[i].tellTemp(),days[i].tellMain(),days[i].tellHum()]
        table_data.append(temp)
    table = AsciiTable(table_data)
    return (table_data)
'''
def makeCurrent():
    key = '114a036fbe8618ec0e3c7b7694391c35'
    api_adress = 'https://api.darksky.net/forecast/'+ key +'/45.4215, -75.6972'
    url = api_adress
    json_data = requests.get(url).json()
    days = [Day((json_data['hourly']['data'][i*12]['temperature']),(json_data['hourly']['data'][i*12]['icon'])) for i in range(0,4)]
    listoDays = []
    for i in range(0,4):
        temp = [days[i].tellTemp(),days[i].tellSum()]
        listoDays.append(temp )
    print(json_data)
    return listoDays



def makeImage():
    image = pygame.display.set_mode((500,500))

print(makeCurrent())
