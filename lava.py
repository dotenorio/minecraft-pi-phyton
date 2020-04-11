import time
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x, y, z = mc.player.getPos()

lava = 10
water = 8
air = 0

# mc.setBlock(x+3, y+3, z, lava)
# mc.setBlock(x+3, y+3, z, water)

mc.setBlock(x+3, y+3, z, air)