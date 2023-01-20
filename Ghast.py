from mcpi.minecraft import Minecraft

mc = Minecraft.create()
pos = mc.player.getPos()
x, y, z = pos.x, pos.y, pos.z
mc.setBlocks(x, y, z, x + 7, y + 7, z, 35)# квадрат 8х8
#Строим глаза и рот гаста
#35, 15 = black wool
mc.setBlock(x + 3, y + 2, z, 35, 15)
mc.setBlock(x + 4, y + 2, z, 35, 15)
mc.setBlock(x + 1, y + 5, z, 35, 15)
mc.setBlock(x + 2, y + 5, z, 35, 15)
mc.setBlock(x + 5, y + 5, z, 35, 15)
mc.setBlock(x + 6, y + 5, z, 35, 15)
