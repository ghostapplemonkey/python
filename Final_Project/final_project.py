from matplotlib.pyplot import switch_backend
from pycat.core import Window, Sprite, Color, KeyCode, RotationMode, Scheduler

window = Window(width=1200,height=600)

window.create_sprite(position=window.center,scale=1200,color=Color.WHITE,layer=-1)
g = window.create_sprite(x=600,y=25,scale=100,scale_x=1200,color=Color.BLACK)
g1 = window.create_sprite(x=325,y=250,scale_y=15,scale_x=220,color=Color.BLACK)
g2 = window.create_sprite(x=875,y=250,scale_y=15,scale_x=220,color=Color.BLACK)
g3 = window.create_sprite(x=600,y=425,scale_y=15,scale_x=220,color=Color.BLACK)
g.add_tag("ground")
g1.add_tag("ground")
g2.add_tag("ground")
g3.add_tag("ground")
class Knife(Sprite):
    def on_create(self):
        self.image = "img/sword.png"
    def on_update(self, dt):
        self.x = p1.x - 30
        self.y = p1.y + 43
        self.rotation = 240
        self.scale = 0.2

class P1(Sprite):
    def on_create(self):
        self.x = 325
        self.y = 375
        self.image = "img/stop.png"
        self.ysp = 0
        self.is_jump = False
        self.layer = 2
        self.state = 0
        self.time = 0
        self.scale = 0.4
    def on_update(self, dt):
        self.time += dt
        if window.is_key_pressed(KeyCode.D):
            self.x += 7
            self.state = 1
        elif window.is_key_pressed(KeyCode.A):
            self.x -= 7
            self.state = -1
        else:
            self.state = 0
        if self.state == 0:
            self.time = 0
            self.image = "img/stop.png"
        if self.state == 1:
            if self.time <= 0.1:
                self.image = "img/move1.png"
            if self.time > 0.1 and dt <= 0.2:
                self.image = "img/move2.png"
            if self.time > 0.2 and dt <= 0.3:
                self.image = "img/move3.png"
            if self.time > 0.3 and dt <= 0.4:
                self.image = "img/move4.png"
            if self.time > 0.4 and dt <= 0.5:
                self.image = "img/move5.png"
            if self.time > 0.5:
                self.time = 0
            if knife.scale_x > 0:
                Scheduler.wait(0.1,knife_switch)
                knife.rotation = 240
            
        if self.state == -1:
            if self.time <= 0.1:
                self.image = "img/move1 (2).png"
            if self.time > 0.1 and dt <= 0.2:
                self.image = "img/move2 (2).png"
            if self.time > 0.2 and dt <= 0.3:
                self.image = "img/move3 (2).png"
            if self.time > 0.3 and dt <= 0.4:
                self.image = "img/move4 (2).png"
            if self.time > 0.4 and dt <= 0.5:
                self.image = "img/move5 (2).png"
            if self.time > 0.5:
                self.time = 0
        if window.is_key_pressed(KeyCode.W) and self.is_jump == False:
            self.ysp = 18
            self.is_jump = True
        self.y += self.ysp
        self.ysp -= 0.8
        ground = self.get_touching_sprites_with_tag("ground")
        if ground and self.ysp < 0:
            groundt = ground[0]
            self.y = groundt.y + groundt.height/2 + self.height/2
            self.is_jump = False
            self.ysp = 0

        
p1 = window.create_sprite(P1)
knife = window.create_sprite(Knife)
def knife_switch():
    knife.scale_x *= -1
window.run()