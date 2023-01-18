import time
import random
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
mc.player.setTilePos(random.randint(-1000, 1000), random.randint(30, 50), random.randint(-1000, 1000))
time.sleep(5)
mc.player.setTilePos(random.randint(-1000, 1000), random.randint(30, 50), random.randint(-1000, 1000))