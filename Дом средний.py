from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
mc.setBlocks(x, y, z, x + 9, y + 9, z + 9, 45) #строим куб 10x10
mc.setBlocks(x + 1, y + 1, z + 1, x + 8, y + 8, z + 8, 0) # Делаем куб полым
mc.setBlocks(x + 2, y + 5, z, x + 3, y + 6, z, 20) # 1 окно.Можно использовать setBlock,потребуется 4 строки кода на 1 окно
mc.setBlocks(x + 6, y + 5, z, x + 7, y + 6, z, 20) # 2 окно
mc.setBlocks(x + 4, y + 1, z, x + 5, y + 2, z, 0) # дверь
mc.setBlocks(x + 1, y + 1, z + 1, x + 8, y + 1, z + 8, 171) # ковер из шерсти
mc.setBlocks(x, y + 10, z, x + 9, y + 10, z + 9, 98) # крыша