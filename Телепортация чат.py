import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
mc.player.setTilePos(123, 30, 200)
mc.postToChat(mc.player.getPos().x)
mc.postToChat(mc.player.getPos().y)
mc.postToChat(mc.player.getPos().z)

