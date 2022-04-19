from pycat.core import Sprite,Window,Scheduler

window = Window()

class Dino(Sprite):
    def on_create(self):
        self.image = "image/dino1.png"
        self.x = 100
        self.y = 200
        self.time = 0
    def on_update(self, dt):
        self.time += dt
        if self.time > 0.1:
            self.time = 0
            if self.image == "image/dino1.png":
                self.image = "image/dino2.png"
            else:
                self.image = "image/dino1.png"
        


window.create_sprite(Dino)
window.run()