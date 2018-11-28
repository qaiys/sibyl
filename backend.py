import requests
import pygame
from terminaltables import AsciiTable
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
    return str(C) + "°C"

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
    return listoDays

def makeImage(listoDays):
    name = input("Name of image: ")
    where = input("Where to store: ")
    extension = input("Extension: ")
    white = (255, 255, 255)
    w = 500
    h = 500
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))
    running = 1
    screen.fill((white))
    myfont = pygame.font.SysFont('Arial', 30)
    textsurface = myfont.render('Some Text', True, (255, 0, 0))
    screen.blit(textsurface,(0,0))
    why = 0
    for i in range(0,4):
        img = pygame.image.load('assets/'+str(listoDays[i][1])+'.png')
        screen.blit(img,(0,why))
        why += 100
    pygame.display.flip()
    pygame.image.save(screen, where+"/"+name+extension)
    exit()
