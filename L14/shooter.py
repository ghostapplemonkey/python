from random import randint
from turtle import speed
from pycat.core import Sprite,Window,Color,KeyCode,Scheduler,Point

window = Window(width=1200,height=600)

class Enemy(Sprite):

    def on_create(self):
        self.color = Color.RED
        self.scale = 30
        self.y = randint(0,600)
        self.speed = 3
        self.time = 0
        self.add_tag("enemy")
    def on_update(self, dt):
        self.time += dt
        if self.time >= 1:
            bullet = window.create_sprite(EnemyBullet)
            self.time = 0
            bullet.position = self.position
            bullet.point_toward_sprite(player)
        self.point_toward_sprite(player)
        self.move_forward(self.speed)
        if self.is_touching_any_sprite_with_tag("bullet"):
            self.delete()
        self.speed += dt*0.3
        
class EnemyBullet(Sprite):
    def on_create(self):
        self.scale = 10
        self.color = Color.BLUE
        self.add_tag("enemybullet")

    def on_update(self, dt):
        self.move_forward(15)
        if self.is_touching_sprite(player):
            print("you lose")
            window.close()
        if self.is_touching_window_edge():
            self.delete()

class Player(Sprite):

    def on_create(self):
        self.color = Color.GREEN
        self.scale = 30
        self.speed = 10
        self.position = window.center
        self.time = 2

    def on_update(self, dt):
        self.time -= dt*0.05
        if window.is_key_pressed(KeyCode.W):
            self.y += self.speed
        if window.is_key_pressed(KeyCode.S):
            self.y -= self.speed 
        if window.is_key_pressed(KeyCode.D):
            self.x += self.speed
        if window.is_key_pressed(KeyCode.A):
            self.x -= self.speed    
        self.point_toward_mouse_cursor()
        
    def on_left_click_anywhere(self):
        window.create_sprite(Bullet)
        
        

player = window.create_sprite(Player)




class Bullet(Sprite):

    def on_create(self):
        self.goto(player)
        self.scale = 10
        self.color = Color.WHITE
        self.point_toward_mouse_cursor()
        self.add_tag("bullet")

    def on_update(self,dt):
        self.move_forward(20)
        if self.is_touching_window_edge():
            self.delete()
        # if self.is_touching_any_sprite_with_tag("enemy"):
        #     self.delete()
def create_enemy():
    window.create_sprite(Enemy)

Scheduler.update(create_enemy,player.time)

window.run()
