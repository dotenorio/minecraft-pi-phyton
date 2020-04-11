import time
import mcpi.minecraft as minecraft

mc = minecraft.Minecraft.create()

mc.postToChat("Oi seu Joaquim, voe...")

time.sleep(2)

x, y, z = mc.player.getPos()
mc.player.setPos(x, y + 50, z)

time.sleep(2)

mc.postToChat("Voou :)")