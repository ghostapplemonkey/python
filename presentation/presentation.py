from random import randint, random
from pycat.core import Sprite,Window,Scheduler,KeyCode

window = Window(width = 1200, enforce_window_limits = False)

scoretext = window.create_label(text="score : ", x=0, y=630, font_size=30)
class Timer(Sprite):
    def on_create(self):
        self.speed = 7.5
    def on_update(self, dt):
        self.speed += 0.005
timer = window.create_sprite(Timer)
class Dino(Sprite):
    def on_create(self):
        self.image = "image/D1.png"
        self.x = 100
        self.y = 200
        self.time = 0
        self.ysp = 0
        self.is_jump = False
        self.layer = 100
        self.stime = 0
        self.score = 0
    def on_update(self, dt):
        if self.is_touching_any_sprite_with_tag("Obstacle"):
            window.create_sprite(image="image/gameover.png", layer=101, position=window.center, x=480)
            window.create_sprite(image="image/gameover.png", layer=102, position=window.center)
            window.create_sprite(image="image/gameover.png", layer=101, position=window.center, x=700)
            window.create_sprite(image="image/gameover.png", layer=101, position=window.center, x=800)
            window.create_label(text="score : "+str(self.score), x=0, y=630, font_size=30, layer = 1000)
            self.delete()

        self.time += dt
        self.stime += dt
        if self.stime > 0.05:
            self.score += 1
            scoretext.text = "Score : "+str(self.score)
        if self.is_jump == False:    
            if self.time > 0.1:
                self.time = 0
                if self.image == "image/D1.png":
                    self.image = "image/D2.png"
                else:
                    self.image = "image/D1.png"
        self.y += self.ysp
        self.ysp -= 1
        if self.y < 200:
            self.y = 200
            self.is_jump = False
        if window.is_key_pressed(KeyCode.W) and self.is_jump == False:
            self.ysp = 25
            self.is_jump = True
        if self.is_jump == True:
            if self.ysp >= 0:
                self.image = "image/D_rising.png"
            if self.ysp > 0:
                self.image = "image/D_falling.png"    

check = window.create_sprite(x = 1200)
class Bg(Sprite):
    def on_create(self):
        self.position = window.center
        self.x = 1500
        self.image = "image/BG.png"
        self.is_create = False
        self.opacity = 130
    def on_update(self, dt):
        self.x -= timer.speed
        if self.x < -1500:
            self.delete()
        if not self.is_touching_sprite(check) and self.is_create == False:
            window.create_sprite(Bg)
            self.is_create = True

class Obstacle(Sprite):
    def on_create(self):
        self.image = "image/ob"+str(randint(1,3))+".png"
        self.x = 1500
        self.y = 200
        Scheduler.wait(randint(2,4),self.create_self)
        self.layer = 99
        self.scale = 0.4+random()*0.1
        self.add_tag("Obstacle")
    def on_update(self, dt):
        self.x -= timer.speed*2
        if self.x < -100:
            self.delete()
    def create_self(self):
        window.create_sprite(Obstacle)
        

window.create_sprite(Bg)
def create_obstacle():
    window.create_sprite(Obstacle)
Scheduler.wait(8,create_obstacle)


window.create_sprite(Dino)   
window.run()