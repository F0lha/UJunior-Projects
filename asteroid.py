# Permite usar o modulo do Sense HAT
from sense_hat import SenseHat
from time import sleep
import pygame,sys,random

sense = SenseHat()


pygame.init()
pygame.display.set_mode()

sense.clear(0,0,0)

#initial postition
player = (4,4)



#game cycle
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = 1
                updateWorld()
            elif event.key == pygame.K_DOWN:
                direction = 3
                updateWorld()
            elif event.key == pygame.K_RIGHT:
                direction = 0
                updateWorld()
            elif event.key == pygame.K_LEFT:
                direction = 2
                updateWorld() 
