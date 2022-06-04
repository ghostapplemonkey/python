from cgitb import text
from pycat.core import Window, Sprite, Color, KeyCode, RotationMode, Scheduler

window = Window(width=1200,height=600)
window.create_sprite(position=window.center,scale=1200,color=Color.WHITE,layer=-100)
g = window.create_sprite(x=600,y=25,scale=100,scale_x=1200,color=Color.BLACK)
g1 = window.create_sprite(x=325,y=250,scale_y=15,scale_x=220,color=Color.BLACK)
g2 = window.create_sprite(x=875,y=250,scale_y=15,scale_x=220,color=Color.BLACK)
g3 = window.create_sprite(x=600,y=425,scale_y=15,scale_x=220,color=Color.BLACK)
g.add_tag("ground")
g1.add_tag("ground")
g2.add_tag("ground")
g3.add_tag("ground")
hp_bar_back1 = window.create_sprite(x=200, y=550, color=Color.BLACK, layer=-1)
hp_bar_back1.scale_x = 200
hp_bar_back1.scale_y = 20
p1_hp_bar = window.create_sprite(x=200, y=550, color=Color.RED)
p1_hp_bar.scale_x = 200
p1_hp_bar.scale_y = 20
hp_bar_back2 = window.create_sprite(x=1000, y=550, color=Color.BLACK, layer=-1)
hp_bar_back2.scale_x = 200
hp_bar_back2.scale_y = 20
p2_hp_bar = window.create_sprite(x=1000, y=550, color=Color.RED)
p2_hp_bar.scale_x = 200
p2_hp_bar.scale_y = 20
class Knife_attack(Sprite):
    def on_create(self):
        self.image = "img/attack1.png"
        self.scale = 0.3
        self.scale_x = -self.scale_x
        self.position = p1.position
        self.point_toward_sprite(p2)
    def on_update(self, dt):
        self.move_forward(10)
        # if self.is_touching_window_edge:
        #     self.delete()

class Knife(Sprite):
    def on_create(self):
        self.image = "img/sword.png"
        self.scale = 0.3
        self.is_following = True
    def on_update(self, dt):
        if self.is_following == True:
            if self.scale_x < 0:
                self.x = p1.x + 30
                self.y = p1.y + 38
                self.rotation = 0
            else:
                self.x = p1.x - 30
                self.y = p1.y + 38
                self.rotation = 0
        else:
            if self.scale_x < 0:
                self.x = p1.x + 66
                self.y = p1.y
                self.rotation = -60
            else:
                self.x = p1.x - 66
                self.y = p1.y 
                self.rotation = 60
        if window.is_key_down(KeyCode.R):
            if self.scale_x < 0:
                self.is_following = False
                Scheduler.wait(0.15,self.knife_back)
            else:
                self.is_following = False
                Scheduler.wait(0.15,self.knife_back)
        
    def knife_back(self):
        if self.scale_x < 0:
            self.is_following = True
        else:
            self.is_following = True
                
class Knife2(Sprite):
    def on_create(self):
        self.image = "img/sword.png"
        self.scale = 0.3
        self.is_following = True
    def on_update(self, dt):
        if self.is_following == True:
            if self.scale_x < 0:
                self.x = p2.x + 30
                self.y = p2.y + 38
                self.rotation = 0
            else:
                self.x = p2.x - 30
                self.y = p2.y + 38
                self.rotation = 0
        else:
            if self.scale_x < 0:
                self.x = p2.x + 66
                self.y = p2.y
                self.rotation = -60
            else:
                self.x = p2.x - 66
                self.y = p2.y 
                self.rotation = 60
        if window.is_key_down(KeyCode.M):
            if self.scale_x < 0:
                self.is_following = False
                Scheduler.wait(0.15,self.knife_back)
            else:
                self.is_following = False
                Scheduler.wait(0.15,self.knife_back)
        
    def knife_back(self):
        if self.scale_x < 0:
            self.is_following = True
        else:
            self.is_following = True
class Wood(Sprite):
    def on_create(self):
        self.image = "img/wood.png"
        self.position = p1.position
        self.ysp = 0
        self.scale = 0.2
        Scheduler.wait(3,self.delete_self)
    def on_update(self, dt):
        if self.is_touching_any_sprite_with_tag("ground"):
            self.ysp = 0
        else:
            self.ysp -= 0.8  
        self.y += self.ysp
        
    def delete_self(self):
        self.delete()

class Rock(Sprite):
    def on_create(self):
        self.image = "img/rock.png"
        self.position = p2.position
        self.ysp = 0
        self.scale = 0.3
        Scheduler.wait(3,self.delete_self)
    def on_update(self, dt):
        if self.is_touching_any_sprite_with_tag("ground"):
            self.ysp = 0
        else:
            self.ysp -= 0.8  
        self.y += self.ysp
        
    def delete_self(self):
        self.delete()     

class P1(Sprite):
    def on_create(self):
        self.x = 325
        self.color = Color.BLUE
        self.y = 375
        self.image = "img/stop.png"
        self.ysp = 0
        self.is_jump = False
        self.layer = 2
        self.state = 0
        self.time = 0
        self.scale = 0.4
        self.xsp = 0
        self.is_hit = False
        self.flying_direction = 0
    def on_update(self, dt):
        self.time += dt
        self.xsp *= 0.95
        if self.is_touching_sprite(knife2) and (knife2.rotation >= 10 or knife2.rotation <= -10):
            p1_hp_bar.scale_x -= 1
            p1_hp_bar.x -= 0.5
            self.xsp = 10
            self.ysp = 5
            self.is_hit = True
            if self.x < p2.x:
                self.flying_direction = -1
            else:
                self.flying_direction = 1
        if self.is_hit == True:
            if self.flying_direction == 1:
                self.x += self.xsp
            else:
                self.x -= self.xsp
        if self.xsp <= 3:
            self.is_hit = False
        if self.is_hit == False:
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
                knife.scale_x *= -1
                
            
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
            if knife.scale_x < 0:
                knife.scale_x *= -1
        if window.is_key_down(KeyCode.T):
            window.create_sprite(Wood)
            self.ysp = 25
        if window.is_key_down(KeyCode.Y):
            window.create_sprite(Knife_attack)
        if window.is_key_pressed(KeyCode.W) and self.is_jump == False and self.is_hit == False:
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


class P2(Sprite):
    def on_create(self):
        self.x = 825
        self.y = 375
        self.image = "img/stop.png"
        self.color = Color.RED
        self.ysp = 0
        self.is_jump = False
        self.layer = 2
        self.state = 0
        self.time = 0
        self.scale = 0.4
        self.xsp = 0
        self.is_hit = False
        self.flying_direction = 0
    def on_update(self, dt):
        self.time += dt
        self.xsp *= 0.95
        if self.is_touching_sprite(knife) and (knife.rotation >= 10 or knife.rotation <= -10):
            p2_hp_bar.scale_x -= 1
            p2_hp_bar.x += 0.5
            self.xsp = 10
            self.ysp = 5
            self.is_hit = True
            if self.x < p1.x:
                self.flying_direction = -1
            else:
                self.flying_direction = 1
        if self.is_hit == True:
            if self.flying_direction == 1:
                self.x += self.xsp
            else:
                self.x -= self.xsp
        if self.xsp <= 3:
            self.is_hit = False
        if self.is_hit == False:    
            if window.is_key_pressed(KeyCode.RIGHT):
                self.x += 7
                self.state = 1
            elif window.is_key_pressed(KeyCode.LEFT):
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
            if knife2.scale_x > 0:
                knife2.scale_x *= -1
                
            
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
            if knife2.scale_x < 0:
                knife2.scale_x *= -1
        if window.is_key_down(KeyCode.N):
            window.create_sprite(Rock)
            self.ysp = 25
        if window.is_key_pressed(KeyCode.UP) and self.is_jump == False and self.is_hit == False:
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
p2 = window.create_sprite(P2)
knife = window.create_sprite(Knife)
knife2 = window.create_sprite(Knife2)
window.run()