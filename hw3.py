from pycat.core import Window,Sprite
from random import random,randint

window = Window()

class Square1(Sprite):
    def on_create(self):
        self.scale = randint(50,200)
        self.goto_random_position()
        self.set_random_color()
    def on_update(self, dt):
        self.y -= 5
class Square2(Sprite):
    def on_create(self):
        self.scale = randint(50,200)
        self.goto_random_position()
        self.set_random_color()
    def on_update(self, dt):
        self.x -= 5

for i in range(50):
    window.create_sprite(Square1)
    window.create_sprite(Square2)

window.run()