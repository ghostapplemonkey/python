from random import random,randint
from pycat.core import Window, Sprite, Color, KeyCode, RotationMode, Scheduler

window = Window(width=1200,height=600)
window.create_sprite(position=window.center,scale=1200,color=Color.WHITE,layer=-100)
g = window.create_sprite(x=600,y=25,scale=100,scale_x=1200,color=Color.BLACK)
g1 = window.create_sprite(x=325,y=250,scale_y=15,scale_x=220,color=Color.BLACK)
g2 = window.create_sprite(x=875,y=250,scale_y=15,scale_x=220,color=Color.BLACK)
g3 = window.create_sprite(x=600,y=425,scale_y=15,scale_x=220,color=Color.BLACK)
window.create_sprite(x=165,y=530,image="img/p1text.png",scale=0.5,layer=-2)
window.create_sprite(x=1035,y=530,image="img/p2text.png",scale=0.5,layer=-2)
window.create_sprite(x=50,y=495,image="img/woodCD.png",scale=0.17,layer=-1)
window.create_sprite(x=1150,y=495,image="img/rockCD.png",scale=0.17,layer=-1)
window.create_sprite(x=120,y=495,image="img/knife1CD.png",scale=0.17,layer=-1)
window.create_sprite(x=1080,y=495,image="img/knife2CD.png",scale=0.17,layer=-1)
window.create_sprite(x=190,y=495,image="img/dashCD.png",scale=0.17,layer=-1)
window.create_sprite(x=1010,y=495,image="img/fireballCD.png",scale=0.17,layer=-1)
woodCD = window.create_sprite(x=50,y=495,scale=60,color=Color.BLACK)
woodCD.opacity = 150
rockCD = window.create_sprite(x=1150,y=495,scale=60,color=Color.BLACK)
rockCD.opacity = 150
knife1CD = window.create_sprite(x=120,y=495,scale=60,color=Color.BLACK)
knife1CD.opacity = 150
knife2CD = window.create_sprite(x=1080,y=495,scale=60,color=Color.BLACK)
knife2CD.opacity = 150
dashCD = window.create_sprite(x=190,y=495,scale=60,color=Color.BLACK)
dashCD.opacity = 150
fireballCD = window.create_sprite(x=1010,y=495,scale=60,color=Color.BLACK)
fireballCD.opacity = 150
g.add_tag("ground")
g1.add_tag("ground")
g2.add_tag("ground")
g3.add_tag("ground")
hp_bar_back1 = window.create_sprite(x=200, y=575, color=Color.BLACK, layer=-1)
hp_bar_back1.scale_x = 200
hp_bar_back1.scale_y = 20
p1_hp_bar = window.create_sprite(x=200, y=575, color=Color.RED)
p1_hp_bar.scale_x = 200
p1_hp_bar.scale_y = 20
hp_bar_back2 = window.create_sprite(x=1000, y=575, color=Color.BLACK, layer=-1)
hp_bar_back2.scale_x = 200
hp_bar_back2.scale_y = 20
p2_hp_bar = window.create_sprite(x=1000, y=575, color=Color.RED)
p2_hp_bar.scale_x = 200
p2_hp_bar.scale_y = 20
p1_energy_back = window.create_sprite(image="img/energyp1.png",x=200,y=550,scale=0.2,layer=-1)
p1_energy_back.scale_x = 1.45
p2_energy_back = window.create_sprite(image="img/energyp2.png",x=1000,y=550,scale=0.2,layer=-1)
p2_energy_back.scale_x = 1.45
p1_energy = window.create_sprite(x=200,y=550,color=Color.BLACK)
p1_energy.scale_x = 200
p1_energy.scale_y = 9.5
p2_energy = window.create_sprite(x=1000,y=550,color=Color.BLACK)
p2_energy.scale_x = 200
p2_energy.scale_y = 9.5
class Knife_attack(Sprite):
    def on_create(self):
        self.add_tag("attackp2")
        self.image = "img/attack1.png"
        self.scale = 0.15
        self.scale_x = -self.scale_x
        self.position = p1.position
        self.point_toward_sprite(p2)
    def on_update(self, dt):
        self.move_forward(10)
        if self.is_touching_window_edge():
           self.delete()
        if self.is_touching_sprite(p2):
            Scheduler.wait(0.1,self.delete_self)
    def delete_self(self):
        self.delete()

class Knife_attack2(Sprite):
    def on_create(self):
        self.add_tag("attackp1")
        self.image = "img/attack2.png"
        self.scale = 0.15
        self.scale_x = -self.scale_x
        self.position = p2.position
        self.point_toward_sprite(p1)
    def on_update(self, dt):
        self.move_forward(10)
        if self.is_touching_window_edge():
           self.delete()
        if self.is_touching_sprite(p1):
            Scheduler.wait(0.1,self.delete_self)
    def delete_self(self):
        self.delete()

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
        if window.is_key_down(KeyCode.E):
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

class Attack_dash_shadow(Sprite):
    def on_create(self):
        self.image = "img/attack_dash.png"
        self.scale = 0.2
        if p1.attack_dash:
            self.position = p1.attack_dash.position
            self.scale_x = p1.attack_dash.scale_x
        else:
            self.delete()
    def on_update(self, dt):
        self.opacity -= 15
        if self.opacity <= 1:
            self.delete()

class Attack_dash(Sprite):
    def on_create(self):
        self.scale_x = -self.scale_x
        self.image = "img/attack_dash.png"
        self.position = p1.position
        self.scale = 0.2
        self.rotation_mode = RotationMode.NO_ROTATION
        Scheduler.wait(5,self.self_delete)
    def on_update(self, dt):
        window.create_sprite(Attack_dash_shadow)
        self.move_forward(35)
        if self.is_touching_window_edge():
            self.scale_x = -self.scale_x
            self.rotation += 180

        
    def self_delete(self):
        p1.attack_dash = None
        self.delete()

class Fireball(Sprite):
    def on_create(self):
        self.scale = 0.1
        self.position = p2.position
        self.add_tag("fireball")
        self.image = "img/fireball.png"
        if p2.x < p1.x:
            self.rotation = 0
        else:
            self.rotation = 180
            
        
    def on_update(self, dt):
        self.move_forward(35)
        if self.is_touching_window_edge():
            self.delete()

class AmazingFireball(Sprite):
    def on_create(self):
        self.scale = 0.1
        self.position = p2.position
        self.add_tag("fireball")
        self.image = "img/fireball.png"
    def on_update(self, dt):
        self.move_forward(35)
        self.point_toward_sprite(p1)
        if self.is_touching_window_edge():
            self.delete()
        if self.is_touching_sprite(p1):
            Scheduler.wait(0.01,self.delete_self)
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
        self.speed = 7
        self.xsp = 0
        self.is_hit = False
        self.flying_direction = 0
        self.knife_attack_CD = 0
        self.wood_CD = 0
        self.dash_CD = 0
        self.attack_dash = None
    def on_update(self, dt):
        woodCD.scale_y = (self.wood_CD*(60/12))/60
        woodCD.y = 465+(self.wood_CD*(60/12))/2
        knife1CD.scale_y = (self.knife_attack_CD*(60/8))/60
        knife1CD.y = 465+(self.knife_attack_CD*(60/8))/2
        dashCD.scale_y = (self.dash_CD*(60/40))/60
        dashCD.y = 465+(self.dash_CD*(60/40))/2
        if self.knife_attack_CD >= 0:
            self.knife_attack_CD -= dt
        if self.wood_CD >= 0:
            self.wood_CD -= dt
        if self.dash_CD >= 0:
            self.dash_CD -= dt    
        self.time += dt
        self.xsp *= 0.95
        if self.is_touching_sprite(knife2) and (knife2.rotation >= 10 or knife2.rotation <= -10):
            p1_hp_bar.scale_x -= 0.5
            p1_hp_bar.x -= 0.25
            self.xsp = 10
            self.ysp = 5
            self.is_hit = True
            if self.x < p2.x:
                self.flying_direction = -1
            else:
                self.flying_direction = 1
        if self.is_touching_any_sprite_with_tag("fireball"):
            p1_hp_bar.scale_x -= 1
            p1_hp_bar.x -= 0.5
            self.speed = 2.5
            Scheduler.wait(3,self.speed_back)
        if self.is_hit == True:
            if self.flying_direction == 1:
                self.x += self.xsp
            else:
                self.x -= self.xsp
        if self.xsp <= 3:
            self.is_hit = False
        if window.is_key_down(KeyCode.Y) and self.dash_CD <= 0.5:
            self.attack_dash = window.create_sprite(Attack_dash)
            self.dash_CD = 40
        if self.is_hit == False:
            if window.is_key_pressed(KeyCode.D):
                self.x += self.speed
                self.state = 1
            elif window.is_key_pressed(KeyCode.A):
                self.x -= self.speed
                self.state = -1
            else:
                self.state = 0
        if self.is_touching_any_sprite_with_tag("attackp1"):
            p1_hp_bar.scale_x -= 1
            p1_hp_bar.x -= 0.5
            self.speed = 2.5
            Scheduler.wait(3,self.speed_back)
        if self.state == 0:
            self.time = 0
            self.image = "img/stop.png"
        if self.state != 0 and p1_energy.scale_x > 0.1:
            p1_energy.x += dt*2
            p1_energy.scale_x -= dt*4
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
        if window.is_key_down(KeyCode.R) and self.wood_CD <= 0.5:
            window.create_sprite(Wood)
            self.ysp = 25
            self.wood_CD = 12
        if window.is_key_down(KeyCode.T) and self.knife_attack_CD <= 0.5:
            window.create_sprite(Knife_attack)
            self.knife_attack_CD = 8
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
    def speed_back(self):
        self.speed = 7

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
        self.speed = 7
        self.scale = 0.4
        self.xsp = 0
        self.is_hit = False
        self.flying_direction = 0
        self.knife_attack_CD = 0
        self.rock_CD = 0
        self.firetime = 0
        self.fireball_CD = 0
        self.is_fire = False
        self.is_amazing = False
    def on_update(self, dt):
        rockCD.scale_y = (self.rock_CD*(60/12))/60
        rockCD.y = 465+(self.rock_CD*(60/12))/2
        knife2CD.scale_y = (self.knife_attack_CD*(60/8))/60
        knife2CD.y = 465+(self.knife_attack_CD*(60/8))/2
        fireballCD.scale_y = (self.fireball_CD*(60/40))/60
        fireballCD.y = 465+(self.fireball_CD*(60/40))/2
        if p2_hp_bar.scale_x < 0:
            print("p1 win")
            # window.close()
        if p1_hp_bar.scale_x < 0:
            print("p2 win")
            # window.close()
        if self.knife_attack_CD >= 0:
            self.knife_attack_CD -= dt
        if self.rock_CD >= 0:
            self.rock_CD -= dt
        if self.fireball_CD >= 0:
            self.fireball_CD -= dt
        self.time += dt
        self.xsp *= 0.95
        if self.is_touching_sprite(knife) and (knife.rotation >= 10 or knife.rotation <= -10):
            p2_hp_bar.scale_x -= 0.5
            p2_hp_bar.x += 0.25
            self.xsp = 10
            self.ysp = 5
            self.is_hit = True
            if self.x < p1.x:
                self.flying_direction = -1
            else:
                self.flying_direction = 1
        if p1.attack_dash != None:    
            if self.is_touching_sprite(p1.attack_dash):
                p2_hp_bar.scale_x -= 4.5
                p2_hp_bar.x += 2.25
                self.speed = 2.5
                Scheduler.wait(3,self.speed_back)
        if self.is_hit == True:
            if self.flying_direction == 1:
                self.x += self.xsp
            else:
                self.x -= self.xsp
        if self.xsp <= 3:
            self.is_hit = False
        if self.is_hit == False:    
            if window.is_key_pressed(KeyCode.RIGHT):
                self.x += self.speed
                self.state = 1
            elif window.is_key_pressed(KeyCode.LEFT):
                self.x -= self.speed
                self.state = -1
            else:
                self.state = 0
        if self.is_touching_any_sprite_with_tag("attackp2"):
            p2_hp_bar.scale_x -= 1
            p2_hp_bar.x += 0.5
            self.speed = 2.5
            Scheduler.wait(3,self.speed_back)
        if self.state == 0:
            self.time = 0
            self.image = "img/stop.png"
        if self.state != 0 and p2_energy.scale_x > 0.1:
            p2_energy.x -= dt*2
            p2_energy.scale_x -= dt*4
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
        if window.is_key_down(KeyCode.N) and self.rock_CD <= 0.5:
            window.create_sprite(Rock)
            self.ysp = 25
            self.rock_CD = 12
        if window.is_key_down(KeyCode.K):
            self.is_fire = True
            self.fireball_CD = 40
            Scheduler.wait(5,self.no_fire)
            if p2_energy.scale_x < 2:
                self.is_amazing = True
        if self.is_fire == True:
            if self.is_amazing == False:
                self.firetime += dt
                if self.firetime > 0.2:
                    window.create_sprite(Fireball)
                    self.firetime = 0
            else:
                self.firetime += dt
                if self.firetime > 0.08:
                    window.create_sprite(AmazingFireball)
                    self.firetime = 0
            
        if window.is_key_down(KeyCode.B) and self.knife_attack_CD <= 0.5:
            window.create_sprite(Knife_attack2)
            self.knife_attack_CD = 8
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
    def speed_back(self):
        self.speed = 7
    def no_fire(self):
        self.is_fire = False
        self.firetime = 0
        

        
p1 = window.create_sprite(P1)
p2 = window.create_sprite(P2)
knife = window.create_sprite(Knife)
knife2 = window.create_sprite(Knife2)
window.run()