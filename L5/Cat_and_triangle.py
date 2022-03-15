from pycat.core import Sprite, Window, KeyCode, RotationMode, Scheduler
from random import Random, randint, random



window = Window(width = 1200,height = 600,background_image = "img/beach_03.png")
    
          

class Cat(Sprite):
    def on_create(self):
        self.x = 600
        self.image = "img/cat.png"
        self.y = 50
        self.rotation_mode = RotationMode.RIGHT_LEFT
        self.score = 0
        self.add_tag("player")
        self.speed = 5
        self.yspeed = 0
        
    def on_update(self, dt):
        if window.is_key_pressed(KeyCode.A):
            self.rotation = 180
            self.x -= self.speed
        if window.is_key_pressed(KeyCode.D):
            self.rotation = 0
            self.x += self.speed
        if self.is_touching_any_sprite_with_tag("triangle"):
            self.score += 1
            labelscore.text = ("score : "+str(player.score))
        if window.is_key_down(KeyCode.W):
            self.yspeed = 15
            self.y = 51
            self.jump = True
        if self.y > 50:
            self.y += self.yspeed
            self.yspeed -= 1
            
        else:
            self.y = 50
            self.yspeed = 0
        
            
            
            
class Speeduplogo(Sprite):
    def on_create(self):
        self.x = 600
        self.y = 300
        self.image = "img/speed_powerup.png"
        self.opacity = 255
        self.scale = 1
        self.is_visible = False
        self.grow = False
    def on_update(self, dt):
        if self.grow == True:
            self.scale += 0.01
            self.opacity -= 4
            self.is_visible = True
            if self.opacity < 30:
                self.grow = False
                self.opacity = 255
                self.scale = 0.5
                self.is_visible = False

class Triangle(Sprite):
    def on_create(self):
        self.add_tag("triangle")
        self.y = 600
        self.x = random()*1200
        self.imagenumber = randint(1,5)
        if self.imagenumber == 1:
            self.image = "img/gem_shiny01.png"
        elif self.imagenumber == 2:
            self.image = "img/gem_shiny02.png"
        elif self.imagenumber == 3:
            self.image = "img/gem_shiny03.png"
        elif self.imagenumber == 4:
            self.image = "img/gem_shiny04.png"
        elif self.imagenumber == 5:
            self.image = "img/gem_shiny05.png"
        self.scale = 0.3
    def on_update(self,dt):
        if self.is_touching_any_sprite_with_tag("player"):
            self.delete()
        if self.y < 10:
            self.delete()
        self.y -= 3
class Speedup(Sprite):
    def on_create(self):
        self.add_tag("speedup")
        self.y = 600
        self.x = random()*1200
        self.image = "img/speed_powerup.png"
        self.scale = 0.5
    def on_update(self, dt):
        self.y -= 6
        if self.is_touching_any_sprite_with_tag("player"):
            self.delete()
            player.speed += 3
            speeduplogo.grow = True
            print("grow")
        if self.y < 10:
            self.delete()

player = window.create_sprite(Cat)        
labelscore = window.create_label(text = "score : "+str(player.score),color = (0,0,0))
speeduplogo = window.create_sprite(Speeduplogo)
def make_triangle():
    window.create_sprite(Triangle)
def make_speedup():
    window.create_sprite(Speedup)

    

Scheduler.update(make_triangle, 1) 
Scheduler.update(make_speedup,5) 
window.run()