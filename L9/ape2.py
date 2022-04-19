from random import randint
from pycat.core import Window,Scheduler,Sprite

window = Window()

class Ape(Sprite):
    def on_create(self):
        self.position = window.center
        self.image = "image/ape_waiting.png"
        self.scale = 5
        self.time = 0
        self.state = 1
        self.beating = 0
    def on_update(self, dt):
        self.time += dt
        if self.state == 1:
            self.image = "image/ape_waiting.png"
            if self.time >= 2:
                self.state = 2
                self.time = 0
        if self.state == 2:
            if self.time > 0.25:    
                if self.image == "image/ape_angry1.png":
                    self.image = "image/ape_angry2.png"
                else:
                    self.image = "image/ape_angry1.png"
                self.beating += 1
                self.time = 0
            if self.beating == 4:
                self.beating = 0
                self.state = 3
        if self.state == 3:
            self.throw()
            self.state = 1
        
    def throw(self):
        window.create_sprite(Bullet)
        
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