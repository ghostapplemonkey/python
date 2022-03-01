from pycat.core import Window,Sprite

window = Window()



class Elephant(Sprite):
    
    def on_create(self):
        self.goto_random_position()
        self.image = "image/elephant.png"
        self.move = "right"
        self.x = 0
    def on_update(self, dt):
        
        if self.distance_to(window.mouse_position) > 11:
            self.point_toward_mouse_cursor()
            self.move_forward(10)

        



window.create_sprite(Elephant)

window.run()