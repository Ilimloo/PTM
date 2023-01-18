import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
#начало телепортационного тура
mc.player.setTilePos(123, 30, 200)
time.sleep(5)
mc.player.setTilePos(-123, 30, -200)
time.sleep(5)
mc.player.setTilePos(900, 30, -700)
