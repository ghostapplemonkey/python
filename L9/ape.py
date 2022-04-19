from random import randint
from pycat.core import Window,Scheduler,Sprite

window = Window()

class Ape(Sprite):
    def on_create(self):
        self.position = window.center
        self.image = "image/ape_waiting.png"
        self.scale = 5
        Scheduler.update(self.throw,3)
    def animate(self):
        if self.image == "image/ape_angry1.png":
            self.image = "image/ape_angry2.png"
        else:
            self.image = "image/ape_angry1.png"
    def throw(self):
        window.create_sprite(Bullet)
        self.image = "image/ape_waiting.png"
        Scheduler.wait(2,self.animate)
        Scheduler.wait(2.25,self.animate)
        Scheduler.wait(2.5,self.animate)
        Scheduler.wait(2.75,self.animate)
        
class Bullet(Sprite):
    def on_create(self):
        self.rotation = randint(45,135)
        self.position = window.center
        self.image = "image/barrel1.png"
        self.scale = 5
    def on_update(self, dt):
        self.move_forward(10)
        if self.y > 600:
            self.delete()

        
window.create_sprite(Ape)
window.run()