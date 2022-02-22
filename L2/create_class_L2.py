from random import random
from venv import create
from pycat.core import Window,Sprite

window = Window()

class Flame(Sprite):

    def on_create(self):
        self.goto_random_position()
        self.image = "image/fireball.gif"
        self.rotation = 360*random()
        self.scale = 0.25+2.25*random()
        self.opacity = 100+155*random()
        self.set_random_color()

class Owl_png(Sprite):
    def on_create(self):
        self.goto_random_position()
        self.image = "image/owl.png"
        self.rotation = 360*random()
        self.scale = 0.25+2.25*random()

class Owl_gif(Sprite):
    def on_create(self):
        self.goto_random_position()
        self.image = "image/owl.gif"
        self.rotation = 360*random()
        self.scale = 0.25+2.25*random()

class Pig(Sprite):
    def on_create(self):
        self.goto_random_position()
        self.image = "image/pig.png"
        self.rotation = 360*random()
        self.scale = 0.25+2.25*random()


# for i in range(100):
#     window.create_sprite(Flame)
for i in range(500):
    window.create_sprite(Pig)
    window.create_sprite(Owl_png)
    window.create_sprite(Owl_gif)

window.run()