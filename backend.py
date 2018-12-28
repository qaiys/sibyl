import requests
import pygame
from terminaltables import AsciiTable
from geopy.geocoders import Nominatim
import datetime
pygame.init()
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
    return str(int(C)) + "°C"

def makeCoords(city): #takes coords from geopy and makes them readable by darksky. Not really well typed but it just werks
    geolocator = Nominatim(user_agent="Sibyl")
    location = geolocator.geocode(city)
    coords = str((location.latitude,location.longitude))
    coords = coords.split(', ')
    lat = coords[0]
    long = coords[1]
    lat=lat.replace('(','')
    long=long.replace(')','')
    lat = lat.split('.')
    long = long.split('.')
    longi = long[1]
    longi = str(long[0])+'.'+str((longi[0:4]))
    latind = lat[1]
    lati = str(lat[0])+'.'+str((latind[0:4]))
    coords = lati +', '+longi
    return coords

def makeCurrent(city): #gets weather information and returns a list
    key = '114a036fbe8618ec0e3c7b7694391c35'
    while True:
        try:
            coords = makeCoords(city)
            break
        except:
            pass
    api_adress = 'https://api.darksky.net/forecast/'+ key +'/'+ coords
    #print(coords)
    url = api_adress
    json_data = requests.get(url).json()
    days = [Day((json_data['hourly']['data'][i*12]['temperature']),(json_data['hourly']['data'][i*12]['icon'])) for i in range(0,4)]
    listoDays = []
    for i in range(0,4):
        temp = [days[i].tellTemp(),days[i].tellSum()]
        listoDays.append(temp)
    return listoDays

def makeImage(listoDays, name, where, extension, city): #puts assets on a pygame surface and takes a screenshot.
    white = (255, 255, 255)
    w = 1280
    h = 720
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))
    running = 1
    screen.fill((white))
    myfont = pygame.font.SysFont('Arial', 30)
    why = 64
    city = (city[0]).capitalize() + (city[1:(len(city))])
    theCity = myfont.render(city,True,(0,0,0))
    for i in range(0,4):
        img = pygame.image.load('assets/'+str(listoDays[i][1])+'.png')
        temperature = myfont.render(str(listoDays[i][0]), True, (0, 0, 0))
        screen.blit(img,(why,256))
        screen.blit(theCity,(0,100))
        screen.blit(temperature,(why,386))
        why += 320
    pygame.display.flip()
    if where == '':
        where = 'pictures'
    if name == '':
        now = datetime.datetime.now()
        name = now.strftime("%Y-%m-%d")
    saveHere = (str(where)+"/"+str(name)+str(extension))
    print(saveHere)
    pygame.image.save(screen, saveHere)

    exit()
