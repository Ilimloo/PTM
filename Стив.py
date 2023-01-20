from mcpi.minecraft import Minecraft

mc = Minecraft.create()
pos = mc.player.getPos()
x, y, z = pos.x, pos.y, pos.z
mc.setBlocks(x, y, z, x + 7, y + 7, z, 159)# квадрат 8х8
#волосы
mc.setBlocks(x, y + 6, z, x + 7, y + 7, z, 17)
mc.setBlock(x, y + 5, z, 17)
mc.setBlock(x + 7, y + 5, z, 17)
#борода
mc.setBlocks(x + 2, y, z, x + 5, y, z, 17)
mc.setBlock(x + 2, y + 1, z, 17)
mc.setBlock(x + 5, y + 1, z, 17)
#глаза
mc.setBlock(x + 1, y + 3, z, 35)
mc.setBlock(x + 2, y + 3, z, 35, 11)
mc.setBlock(x + 5, y + 3, z, 35, 11)#blue wool
mc.setBlock(x + 6, y + 3, z, 35)
#нос
mc.setBlock(x + 3, y + 2, z, 35, 12)
mc.setBlock(x + 4, y + 2, z, 35, 12)
