from mcpi.minecraft import Minecraft
import math
import random
mc = Minecraft.create()
pos = mc.player.getPos()
x, y, z = pos.x, pos.y, pos.z
destX = random.randint(-50, 5)
destZ = random.randint(-50, 5)
destY = mc.getHeight(destX, destZ)
block = 57
mc.setBlock(destX, destY, destZ, block)
mc.postToChat("Блок создан")
while True:
    pos = mc.player.getPos()
    distance = math.sqrt((pos.x - destX) ** 2 + (pos.z - destZ) ** 2)
    if distance > 100:
        mc.postToChat("Замерзнешь")
    elif distance > 50:
        mc.postToChat("Холодно")
    elif distance > 25:
        mc.postToChat("Тепло")
    elif distance > 12:
        mc.postToChat("Горячо")
    elif distance > 6:
        mc.postToChat("Обожжешься!")
    elif distance <= 3:
        mc.postToChat("Блок найден")
        break