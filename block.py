import mcpi.minecraft as minecraft
from mcpi import block

mc = minecraft.Minecraft.create()

x, y, z = mc.player.getPos()
mc.setBlock(x+1, y, z, 1) # with id
mc.setBlock(x+3, y, z, block.STONE.id) # with const
mc.setBlock(x+2, y, z, block.WOOL.id, 2) # with color