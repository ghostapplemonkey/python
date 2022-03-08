from pycat.core import Window,KeyCode,Sprite,RotationMode, Scheduler
from random import Random, random

window = Window(background_image = "image/sea.png",width = 1200,height = 600)



class Owl(Sprite):
    def on_create(self):
        self.image = "image/owl.png"
        self.goto_random_position()
        self.rotation_mode = RotationMode.RIGHT_LEFT
        self.score = 0
        self.life = 3
        self.add_tag("player")
    def on_update(self, dt):
        if self.y < 480:
            if window.is_key_down(KeyCode.W):
                self.y += 160
        if self.y > 160:
            if window.is_key_down(KeyCode.S):
                self.y -= 160

        
class Ork(Sprite):
    def on_create(self):
        self.goto_random_position()
        self.image = "image/ork1.png"
        self.scale = 0.15
        self.x = 1000
        self.y = (1+random()*2)*160
    def on_update(self, dt):
        if self.is_touching_any_sprite_with_tag("player"):
            owl.life -= 1
            label_life.text = str("life : "+str(owl.life))
            self.delete()
        self.x -= 5
        if self.x < 100:
            self.delete()
class Rat(Sprite):
    def on_create(self):
        self.goto_random_position()
        self.image = "image/rat.png"
        self.x = 1000
        self.y = (1+random()*2)*160
        self.scale = 0.6
    def on_update(self, dt):
        if self.x < 100:
            self.delete()
        if self.is_touching_any_sprite_with_tag("player"):
            owl.score += 1
            label_score.text = str("score : "+str(owl.score))
            self.delete()
        self.x -= 5


owl = window.create_sprite(Owl,x = 100,y = 320)
ork = window.create_sprite(Ork)
rat = window.create_sprite(Rat)
label_score = window.create_label(text = "score : "+ str(owl.score))
label_life = window.create_label(text = "life : "+ str(owl.life),y = 550)

  

def make_enemies():
    ork = window.create_sprite(Ork)
def make_rat():
    rat = window.create_sprite(Rat)

Scheduler.update(make_enemies, 5) 
Scheduler.update(make_rat, 2)       

window.run()