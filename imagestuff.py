import pygame
pygame.init()
img = pygame.image.load('assets/snow.png')
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
screen.blit(img,(0,0))
pygame.display.flip()
pygame.image.save(screen, where+"/"+name+extension)
exit()
