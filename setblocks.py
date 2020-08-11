import time
import random 
from mcpi.minecraft import Minecraft
mc=Minecraft.create()



color=random.randrange(0,50)
while True:
    time.sleep(0.5)
    x,y,z=mc.player.getTilePos()
    mc.setBlocks(x+25,y-1,z+25,x-25,y-1,z-25,95,color)

