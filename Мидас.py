from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z
air = 0
water = 9
while True:
    pos = mc.player.getTilePos()
    x, y, z = pos.x, pos.y, pos.z
    blockBelow = mc.getBlock(x, y - 1, z) # блок под нами
    if blockBelow != air  and blockBelow != 8:
        mc.setBlocks(x - 1, y - 1, z - 1, x + 1, y - 1, z + 1, 41) # заменяем блок на золото


