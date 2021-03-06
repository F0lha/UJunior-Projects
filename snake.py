# Permite usar o modulo do Sense HAT
from sense_hat import SenseHat
from time import sleep
import pygame,sys,random

sense = SenseHat()


pygame.init()
pygame.display.set_mode()

sense.clear(0,0,0)

snakeHead = [5,5]

snake = [snakeHead]

fruit = list(snakeHead)

def randomFruit(snake):
    global fruit
    fruit = [random.randrange(8),random.randrange(8)]
    while fruit in snake:
        fruit = [random.randrange(8),random.randrange(8)]

randomFruit(snake)

updateWorldID = pygame.USEREVENT + 1

direction = 1

        
def moveSnake():
    global fruit, snake, direction
    removed = None
    head = list(snake[0])
    if(direction == 0):
        head[0] = (head[0] + 1) % 8
    elif(direction == 1):
        head[1] = (head[1] - 1) % 8
    elif(direction == 2):
        head[0] = (head[0] - 1) % 8
    elif(direction == 3):
        head[1] = (head[1] + 1) % 8

    #if eats fruit
    if head != fruit:
        removed = snake.pop(-1)
    else:
        randomFruit(snake)
        
    if head in snake:
        sense.set_pixel(head[0],head[1],255,0,0)
        finalScreen = sense.get_pixels()
        for x in range(0, 6):
            if x % 2 == 0:
                sense.clear(0,0,0)
            else:
                sense.set_pixels(finalScreen)
            sleep(0.5)
        sense.show_message("Score = " + str(len(snake)))
        sys.exit()
    else:
        snake = [head] + snake
    return removed


def drawWorld(removed):
    global fruit, snake
    first = True
    if removed is not None:
        sense.set_pixel(removed[0],removed[1],0,0,0)
    for point in snake:
        if first:
            sense.set_pixel(point[0],point[1],255,255,0)
            first = False
        else: sense.set_pixel(point[0],point[1],255,255,255)
    sense.set_pixel(fruit[0],fruit[1],0,255,0)

def updateWorld():
    removed = moveSnake()
    drawWorld(removed)
    pygame.time.set_timer(updateWorldID, 250)
        
pygame.time.set_timer(updateWorldID, 250)

sense.set_rotation(180)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 3:
                direction = 1
                updateWorld()
            elif event.key == pygame.K_DOWN and direction != 1:
                direction = 3
                updateWorld()
            elif event.key == pygame.K_RIGHT and direction != 2:
                direction = 0
                updateWorld()
            elif event.key == pygame.K_LEFT and direction != 0:
                direction = 2
                updateWorld()
        elif event.type == updateWorldID:
            updateWorld()
