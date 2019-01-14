import requests
import pygame
#from terminaltables import AsciiTable
from geopy.geocoders import Nominatim
import datetime
import os

pygame.init()
class Day:
    def __init__(self,temp,sum,pt,ptper):
        self.temp = temp
        self.sum = sum
        self.pt = pt
        self.ptper = ptper
    def tellTemp(self):
        return (FtoC(self.temp))
    def tellSum(self):
        return self.sum
    def tellPt(self):
        return self.pt
    def tellPtper(self):
        return self.ptper

def FtoC(F):
    C = (int(F)-32) * (5/9)
    return str(int(C)) + "°C"

def getFonts():
    return pygame.font.get_fonts()

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

def precipGetter(list,n): #since not all of the json list parts have precip, this is just to stop any errors from happenening when the days objects is made
    try:
        return list['hourly']['data'][n*12]['precipType']
    except:
        return ''
def precipChanceGetter(list,n):
    try:
        return int((list['hourly']['data'][n*12]['precipProbability'])*100)
    except:
        return ''

def centralizor(widthOfIcon, widthOfText):
    return ((widthOfIcon - (widthOfText)) / 2)

def makeCurrent(city): #gets weather information and returns a list
    key = '114a036fbe8618ec0e3c7b7694391c35'
    #114a036fbe8618ec0e3c7b7694391c35
    while True:
        try:
            coords = makeCoords(city)
            break
        except:
            pass
    api_adress = 'https://api.darksky.net/forecast/'+ key +'/'+ coords
    url = api_adress
    try:
        json_data = requests.get(url).json()
    except:
        return 3
    days = [Day((json_data['hourly']['data'][i*12]['temperature']),
                (json_data['hourly']['data'][i*12]['icon']),
                (precipGetter(json_data,i)),
                (precipChanceGetter(json_data,i)))
                for i in range(0,4)]
    listoDays = []
    for i in range(0,4):
        temp = [days[i].tellTemp(),days[i].tellSum(),days[i].tellPt(),days[i].tellPtper()]
        listoDays.append(temp)
    return listoDays

def titalize(word):
    capped_word = (word[0]).capitalize() + (word[1:(len(word))])
    return capped_word

def makeImage(listoDays, where, cityName, backgroundLocation): #puts assets on a pygame surface and takes a screenshot.
    white = (255, 255, 255)
    black = (0,0,0)
    w = 1280
    h = 720
    bg = pygame.image.load(backgroundLocation)
    #bg = pygame.draw.rect(screen,(0,255,0),(0,0,1280,720))
    screen = pygame.display.set_mode((w, h))
    logo = pygame.image.load("assets/logo.png")
    #screen.fill((0,255,0))
    #screen.fill((white))
    myfont = pygame.font.SysFont('Arial', 30)
    titalFont = pygame.font.SysFont('Arial', 110)
    smolFont = pygame.font.SysFont('Arial', 20)
    why = 64
    titalOfCity = titalize(cityName)
    theCity = titalFont.render(titalOfCity,True,(black))
    screen.blit(bg,(0,0))
    times = ["Now","Later","Tomorrow","Afternoon"]
    for i in range(0,4):
        img = pygame.image.load('assets/'+str(listoDays[i][1])+'.png')
        temperature = myfont.render(str(listoDays[i][0]), True, (black))
        theTime = myfont.render(str(times[i]), True, (black))
        txtMoveby = centralizor(img.get_width(),temperature.get_width())
        screen.blit(temperature,(why + txtMoveby,386))
        timeMoveby = centralizor(img.get_width(),theTime.get_width())
        typeOfPrecip = myfont.render(str(listoDays[i][2]), True, (black))
        if str(listoDays[i][3]) != '0':
            placeholder = str(listoDays[i][3]) + "%" + " chance of " + str(listoDays[i][2])
            precipChance = smolFont.render(str(placeholder), True, (black))
            txtMoveby = centralizor(img.get_width(),precipChance.get_width())
            screen.blit(precipChance,(why + txtMoveby,420 + 40))
        pygame.draw.rect(screen, (black),((why-3),253 + 40,134,134))
        pygame.draw.rect(screen, (255,255,255),[(why + timeMoveby-2),195-2 + 40,(theTime.get_width()+4),(theTime.get_height()+4)])
        pygame.draw.rect(screen, (black),[(why + timeMoveby-2),195-2 + 40,(theTime.get_width()+4),(theTime.get_height()+4)],2)
        screen.blit(img,(why,296))
        screen.blit(theCity,(15 ,0))
        screen.blit(theTime,(why + timeMoveby,195 + 40))
        screen.blit(logo,(1190,10))
        why += 320
    pygame.display.flip()
    saveHere = (str(where))
    pygame.image.save(screen, "temp.png")

    try:
        pygame.display.quit()
        os.rename("temp.png", str(saveHere)+".png")
        return 1 #I stole this idea from C programming. All functions have a return 1 or 0 built in and I didn't know how to prompt for overwriting with tkinter so when life gives you errors I guess.
        exit()
    except FileExistsError:
        pygame.display.quit()
        return 0
        exit()
