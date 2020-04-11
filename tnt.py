import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()

tnt = 46

x, y, z = mc.player.getPos()
mc.setBlock(x+1, y, z, tnt, 1)