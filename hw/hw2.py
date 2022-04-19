from pycat.core import Window,Sprite
from random import random,randint

window = Window()

class Square(Sprite):
    def on_create(self):
        self.scale = randint(50,200)
        self.goto_random_position()
        self.set_random_color()
    def on_update(self, dt):
        self.y -= 5

for i in range(100):
    window.create_sprite(Square)

window.run()