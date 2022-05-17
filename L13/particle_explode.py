from random import randint, random
from pycat.core import Sprite,Window,Scheduler,Color,KeyCode,Point
from sklearn.inspection import PartialDependenceDisplay

window = Window(width=1200,height=600)

class Particle(Sprite):
    def on_create(self):
        self.position = window.center
        self.y = 400
        self.scale = 0.05+random()*0.25
        self.image = "particle1.png"
        self.rotation = randint(0,360)
        self.time = 0
        self.speed = random()*7
    def on_update(self,dt):
        self.speed *= 0.99
        self.y -= 1
        self.scale += 0.005
        self.opacity -= 3
        self.move_forward(self.speed)
        if self.opacity < 10:
            self.delete()
class Particle2(Sprite):
    def on_create(self):
        self.position = window.center
        self.y = 400
        self.scale = 0.05+random()*0.25
        self.image = "particle2.png"
        self.rotation = randint(0,360)
        self.time = 0
        self.speed = random()*7
    def on_update(self,dt):
        self.speed *= 0.99
        self.y -= 1
        self.scale += 0.005
        self.opacity -= 3
        self.move_forward(self.speed)
        if self.opacity < 10:
            self.delete()
class Shoot(Sprite):
    def on_create(self):
        self.point_toward(Point(600,400))
        self.image = "particle1.png"
        self.scale = 0.5
    def on_update(self, dt):
        self.move_forward(5)
        if self.x > 600:
            for i in range(200):
                window.create_sprite(Particle)
            for i in range(100):
                window.create_sprite(Particle2)
            self.delete()

window.create_sprite(Shoot)

window.run()