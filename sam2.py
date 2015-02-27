import mcpi.minecraft as minecraft
from mcpi import block
from time import sleep
from random import randint

def make_columns(pos):
    for i in range(20):
        mc.setBlock(pos.x+3, pos.y+i, pos.z, block.STONE.id)
        mc.setBlock(pos.x, pos.y+i, pos.z+3, block.STONE.id)
        mc.setBlock(pos.x, pos.y+i, pos.z-3, block.STONE.id)
        mc.setBlock(pos.x-3, pos.y+i, pos.z, block.STONE.id)


def random_fence(pos):
    for i in range(40):
        make_columns(pos)
        pos.x += randint(2, 8)
        sleep(0.5)
        


def wall(pos=None, width=50, height=10, thickness=0):
    if pos is None:
        pos = mc.player.getTilePos()
    mc.setBlocks(pos.x,
        pos.y,
        pos.z,
        pos.x + width,
        pos.y + height,
        pos.z + thickness,
        block.BEDROCK.id)

def clear(pos, size=10):
    mc.setBlocks(pos.x - size,
        pos.y - size,
        pos.z - size,
        pos.x + size,
        pos.y + size,
        pos.z + size,
        block.AIR.id)
    
def savefeet():
    pos = mc.player.getTilePos()
    b = mc.getBlock(pos.x, pos.y-1, pos.z)
    if b in [block.AIR.id, block.WATER_STATIONARY.id, block.WATER_FLOWING.id]:
        mc.setBlock(pos.x, pos.y-1, pos.z, block.GLASS.id)

mc = minecraft.Minecraft.create()
while True:
    sleep(0.5)
    savefeet()

