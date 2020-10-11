

import pygame                   #pygame pakage
from pygame.locals import *     #constantes et fonctions pygame
from sys import exit            # exit script

pygame.init()


window = pygame.display.set_mode((1024, 768))

menu_background = pygame.image.load("./assets/menu.png").convert()
window.blit(menu_background, (0, 0))

pygame.display.flip()

run = 1
while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = 0
            