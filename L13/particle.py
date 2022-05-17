from random import randint
from pycat.core import Sprite,Window,Scheduler,Color,KeyCode

window = Window()

class Particle(Sprite):
    def on_create(self):
        self.position = window.center
        self.y = 100
        self.scale = 10
        self.rotation = randint(50,130)
        self.add_tag("particle")
    def on_update(self,dt):
        self.move_forward(10)
        if self.is_touching_window_edge():
            self.delete()
class Button(Sprite):
    def on_create(self):
        self.x = 200
        self.y = 100
        self.scale = 200
    def on_left_click(self):
        lst = window.get_sprites_with_tag("particle")
        for particle in lst:
            particle.color = 255,255,0
        
window.create_sprite(Button)
def create_particle():
        window.create_sprite(Particle)
Scheduler.update(create_particle,0.01)

window.run()