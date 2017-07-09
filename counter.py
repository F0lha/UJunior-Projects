# Permite usar o modulo do Sense HAT
from sense_hat import SenseHat
from time import sleep
import pygame,sys,random

sense = SenseHat()


pygame.init()
pygame.display.set_mode()

#initial spot
speed = random.randrange(200,1500)

counter = 8

hide = random.randrange(3,5)

sense.show_letter(str(counter))

ticks = pygame.time.get_ticks()

#updateCounter
updateCounterID = pygame.USEREVENT + 1

def updateCounter():
    global counter, ticks, hide
    counter -= 1
    ticks = pygame.time.get_ticks()
    #update sensehat
    if counter >= hide:
        sense.show_letter(str(counter))
    else:
        sense.show_letter('?')


def gameover():
    diff = pygame.time.get_ticks() - ticks
    secs = abs((diff/ float(speed) + (counter - 1)))
    sense.show_message("Falhaste por " + '{:.3f}'.format(secs) + " sec!",0.06)
    sys.exit()

pygame.time.set_timer(updateCounterID,speed)


while 1:
    for event in pygame.event.get():
        senseEvents = sense.stick.get_events()
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gameover()
        elif event.type == updateCounterID:
            updateCounter()
            if counter < - 5:
                gameover()
        elif len(senseEvents) > 0:
            gameover()
