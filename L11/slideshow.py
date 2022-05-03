from pycat.core import Sprite, Window, Scheduler, Color

window = Window(height=600,width=1200)

picture = ["image/meerkat.jpg","image/hedgehog.jpg","image/cat.jpg"]

class Button1(Sprite):
    def on_create(self):
        self.scale = 100
        self.x = 300
        self.y = 100
        self.color = Color.RED
    def on_left_click(self):
        window.background_image = picture[0]

class Button2(Sprite):
    def on_create(self):
        self.scale = 100
        self.x = 600
        self.y = 100
        self.color = Color.GREEN
    def on_left_click(self):
        window.background_image = picture[1]

class Button3(Sprite):
    def on_create(self):
        self.scale = 100
        self.x = 900
        self.y = 100
        self.color = Color.BLUE
    def on_left_click(self):
        window.background_image = picture[2]

window.create_sprite(Button1)
window.create_sprite(Button2)
window.create_sprite(Button3)


window.run()
