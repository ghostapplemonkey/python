from pycat.core import Window,Sprite,KeyCode

window = Window()



class Elephant(Sprite):
    
    def on_create(self):
        self.goto_random_position()
        self.image = "image/elephant.png"
    def on_update(self, dt):
        if window.is_key_pressed(KeyCode.W):
            self.y += 5
            self.rotation = 90
            self.image = "image/elephant.png"
        if window.is_key_pressed(KeyCode.S):
            self.y -= 5
            self.rotation = 270
            self.image = "image/elephant.png"
        if window.is_key_pressed(KeyCode.D):
            self.x += 5
            self.image = "image/elephant.png"
            self.rotation = 0
        if window.is_key_pressed(KeyCode.A):
            self.x -= 5
            self.image = "image/elephant_left.png"
            self.rotation = 0

class Rat(Sprite):
    
    def on_create(self):
        self.goto_random_position()
        self.image = "image/rat.png"
        self.score = 0
    def on_update(self, dt):
        if self.is_touching_sprite(elephant):
            self.goto_random_position()
            self.score += 1
            label.text = "score : "+str(rat.score)



elephant = window.create_sprite(Elephant)
rat = window.create_sprite(Rat)
label = window.create_label(text = "score : "+str(rat.score))
window.run()