from mcpi.minecraft import Minecraft
import math
import random

# Подключаемся к игре Minecraft
mc = Minecraft.create()

# Получаем текущую позицию игрока
pos = mc.player.getPos()
x, y, z = pos.x, pos.y, pos.z

# Выбираем случайное место для блока
destX = x + random.randint(-50, 50)
destZ = z + random.randint(-50, 50)
destY = mc.getHeight(destX, destZ) + 1  # блок будет находиться на вершине столба

# Устанавливаем блок в выбранном месте
block = 57  # Блок из алмазного блока
mc.setBlock(destX, destY, destZ, block)

# Начинаем цикл, который будет проверять расстояние между игроком и блоком
while True:
    pos = mc.player.getPos()
    distance = math.sqrt((pos.x - destX) ** 2 + (pos.y - destY) ** 2 + (pos.z - destZ) ** 2)

    # Выводим подсказки в зависимости от расстояния
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
        break  # Выходим из цикла, когда игрок находится достаточно близко к блоку


