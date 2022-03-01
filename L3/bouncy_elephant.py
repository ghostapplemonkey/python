from pycat.core import Window,Sprite

window = Window()



class Elephant(Sprite):
    
    def on_create(self):
        self.goto_random_position()
        self.image = "image/elephant.png"
        self.move = "right"
        self.x = 0
    def on_update(self, dt):
        if self.move == 0:
            self.x += 5
            self.image = "image/elephant.png"
        else:
            self.x -= 5
            self.image = "image/elephant_left.png"
        if self.x > 1200:
            self.move = 1
        if self.x < 80:
            self.move = 0

window.create_sprite(Elephant)

window.run()