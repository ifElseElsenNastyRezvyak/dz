from mcpi.minecraft import Minecraft

mc = Minecraft.create()

class home():
    def __init__(self, x, y, z, w, h, d):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        self.h = h
        self.d = d

    def build(self):
       mc.setBlocks(self.x, self.y, self.z, self.x + self.w, self.y + self.h, self.z + self.d, 4)
       #mc.setBlock(self.x + 1, self.y + 1, self.z + 1, self.x + self.w, self.y + self.h - 1, self.z + self.d - 1, 0)

pos = mc.player.getTilePos()

x = home(pos.x, pos.y, pos.z, 10, 10 ,10)
x.build()
