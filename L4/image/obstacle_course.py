from pycat.core import Window,KeyCode,Sprite

window = Window(background_image = "image/sea.png")

class Owl(Sprite):
    def on_create(self):
        self.image = "image/owl.png"
        self.goto_random_position()
    def on_update(self, dt):
        if window.is_key_down(KeyCode.W):
            self.rotation = 90
        if window.is_key_down(KeyCode.A):
            self.rotation = 180
        if window.is_key_down(KeyCode.S):
            self.rotation = 270
        if window.is_key_down(KeyCode.D):
            self.rotation = 0
        self.move_forward(5)
        if self.is_touching_sprite(ork):
            print("You lose")
            window.close()
        if self.is_touching_sprite(rat):
            print("You win")
            window.close()
class Ork(Sprite):
    def on_create(self):
        self.goto_random_position()
        self.image = "image/ork1.png"
        self.scale = 0.3
class Rat(Sprite):
    def on_create(self):
        self.goto_random_position()
        self.image = "image/rat.png"


window.create_sprite(Owl)
ork = window.create_sprite(Ork)
rat = window.create_sprite(Rat)
        

window.run()