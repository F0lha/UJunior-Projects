# Permite usar o modulo do Sense HAT
from sense_hat import SenseHat
from time import sleep
from enum import enum
import random,numpy

class Color(enum):
    EMPTY = 0
    RED = 1
    BLUE = 2

sense = SenseHat()

class ConnectFour:
    player = 0
    board = 0

    def __init__(self):
        self.player = 0
        self.board = getNewBoard()

def getNewBoard():
    return numpy.zeros(8,8)

def getPossiblePlays(board)

