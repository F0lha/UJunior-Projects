# Permite usar o modulo do Sense HAT
from sense_hat import SenseHat
from time import sleep
import pygame,sys,random


sense = SenseHat()


red = [255,0,0]
green = [0,255,0]
yellow = [255,255,0]
black = [0,0,0]
white = [255,255,255]

pygame.init()
pygame.display.set_mode()

sense.clear(0,0,0)

#direction, 0-right, 1-up, etc

#initial postition
player = [3,4]

IDIndex = pygame.USEREVENT + 1

#list of enemy : [x,y,direction]
enemies = {}

def movePlayer(direction):
    global player
    sense.set_pixel(player[0],player[1], black)
    if direction == 0:
        player[0] -= 1
    #up
    elif direction == 1:
        player[1] += 1
    #left
    elif direction == 2:
        player[0] += 1
    #down
    elif direction == 3:
        player[1] -= 1

    for key,value in enemies.items():
        if value != None:
            gameover(value)
    
    sense.set_pixel(player[0],player[1], green)

def moveEnemy(enemy):
    sense.set_pixel(enemy[0],enemy[1], black) #clear
    
    #right
    if enemy[2] == 0:
        enemy[0] -= 1
    #up
    elif enemy[2] == 1:
        enemy[1] += 1
    #left
    elif enemy[2] == 2:
        enemy[0] += 1
    #down
    elif enemy[2] == 3:
        enemy[1] -= 1
        
    if (enemy[0] < 0 or enemy[0] > 7) or (enemy[1] < 0 or enemy[1] > 7):
        removeEnemy(enemy)
    else:
        #gameover here
        gameover(enemy)
        drawEnemy(enemy)

def drawEnemy(enemy):
    sense.set_pixel(enemy[0],enemy[1], red) #draw

def gameover(enemy):
    global start
    if player[0] == enemy[0] and player[1] == enemy[1]:
        end = pygame.time.get_ticks()
        for x in range(0,3):
            sense.set_pixel(enemy[0],enemy[1], yellow)
            sleep(0.5)
            sense.set_pixel(enemy[0],enemy[1], white)
            sleep(0.5)
        sense.set_rotation(180)
        sense.show_message("Score = " + str((end - start)/1000))
        sys.exit()
        
def getIndex():
    global IDIndex
    if IDIndex < 32:
        index = IDIndex
        IDIndex += 1
        return index
    else:
        for key, value in enemies.items():
            if value == None:
                return key

def removeEnemy(enemy):
    pygame.time.set_timer(enemy[3],0)
    enemies[enemy[3]] = None

def createEnemy():
    global createEnemyID
    randomDirection = random.randrange(4)
    if randomDirection == 0:
        x = 7
        y = random.randrange(8)
    #up
    elif randomDirection == 1:
        y = 0
        x = random.randrange(8)
    #left
    elif randomDirection == 2:
        x = 0
        y = random.randrange(8)
    #down
    elif randomDirection == 3:
        y = 7
        x = random.randrange(8)
    index = getIndex()
    enemy = [x,y,randomDirection, index]
    enemies[index] = enemy
    print(index)
    pygame.time.set_timer(index,1000)
    drawEnemy(enemy)
    pygame.time.set_timer(createEnemyID,random.randrange(1500,2500))

createEnemyID = IDIndex
IDIndex += 1

pygame.time.set_timer(createEnemyID,random.randrange(1500,2500))
movePlayer(0)

start = pygame.time.get_ticks()

#game cycle
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and player[1] < 7:
                movePlayer(1)
            elif event.key == pygame.K_DOWN and player[1] > 0:
                movePlayer(3)
            elif event.key == pygame.K_RIGHT and player[0] > 0:
                movePlayer(0)
            elif event.key == pygame.K_LEFT and player[0] < 7:
                movePlayer(2)
        elif event.type in enemies:
            moveEnemy(enemies[event.type])
        elif event.type == createEnemyID:
            createEnemy()
        
