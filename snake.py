# Permite usar o modulo do Sense HAT
from sense_hat import SenseHat
from time import sleep
import pygame,sys,random

sense = SenseHat()


pygame.init()
pygame.display.set_mode()

snakeHead = [5,5]

snake = [snakeHead]

fruit = list(snakeHead)

def randomFruit(snake):
    global fruit
    while fruit in snake:
        fruit = [random.randrange(8),random.randrange(8)]

randomFruit(snake)

updateWorldID = pygame.USEREVENT + 1

direction = 1

        
def moveSnake(direction):
    global fruit, snake
    head = list(snake[0])
    if(direction == 0):
        head[0] = (head[0] + 1) % 8
    elif(direction == 1):
        head[1] = (head[1] - 1) % 8
    elif(direction == 2):
        head[0] = (head[0] - 1) % 8
    elif(direction == 3):
        head[1] = (head[1] + 1) % 8
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
        if head != fruit:
            snake.pop(-1)
        else:
            randomFruit(snake)

def drawWorld(snake):
    global fruit
    sense.clear(0,0,0)
    for point in snake:
        sense.set_pixel(point[0],point[1],255,255,255)
    sense.set_pixel(fruit[0],fruit[1],0,255,0)

def updateWorld():
    moveSnake(direction)
    drawWorld(snake)
    pygame.time.set_timer(updateWorldID, 250)


pygame.time.set_timer(updateWorldID, 250)

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
