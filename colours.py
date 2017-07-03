# Permite usar o modulo do Sense HAT
from sense_hat import SenseHat
from mcpi.minecraft import Minecraft
from time import sleep

sense = SenseHat()
mc = Minecraft.create()

# blocos
grass = 2
water = 9
sand = 12
air = 0


# cores
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)

# bloco: cor
colours = {
    air: white,
    grass: green,
    water: blue,
    sand: yellow,
}

known_blocks = {}

def get_blocks():
    blocks = []
    x, y, z = mc.player.getTilePos()
    y -= 1
    for dz in range(z-3, z+5):
        for dx in range(x-3, x+5):
            b = (dx, y, dz)
            if b in known_blocks:
                block = known_blocks[b]                    
            else:
                block = mc.getBlock(dx, y, dz)
                known_blocks[b] = block
                altura = y
                while block == air:
                    altura = altura - 1
                    block = mc.getBlock(dx, altura, dz)
                    known_blocks[b] = block
            blocks.append(block)
    return blocks

def lookup_colour(block):
    if block in colours:
        return colours[block]
    else:
        return white
    
def map_blocks_to_colours(blocks):
    return [lookup_colour(block) for block in blocks]

player_pos = 27
while True:
    blocks = get_blocks()
    pixels = map_blocks_to_colours(blocks)
    pixels[player_pos] = black
    sense.set_pixels(pixels)

