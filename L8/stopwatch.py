from pycat.core import Window, Sprite, Color, Label

window = Window(width = 1200,height = 600)

class Time(Label):
    def on_create(self):
        self.x = 50
        self.y = 550
        self.time = 0
        self.text = str(round(self.time,2))
        self.font_size = 100
    def on_update(self, dt: float):
        if start.color == Color.RED:
            self.time += dt
            self.text = str(round(self.time,2))
        else:
            pass

timer = window.create_label(Time)
class Start(Sprite):
    def on_create(self):
        self.x = 300
        self.y = 100
        self.scale = 100
        self.color = Color.GREEN
    def on_left_click(self):
        if self.color == Color.RED:
            self.color = Color.GREEN
        else:
            self.color = Color.RED


class Reset(Sprite):
    def on_create(self):
        self.x = 600
        self.y = 100
        self.scale = 100
        self.color = Color.BLUE
    def on_left_click(self):
        if start.color == Color.GREEN:
            timer.time = 0
            timer.text = str(round(timer.time,2))
        else:
            pass

        

start = window.create_sprite(Start)
reset = window.create_sprite(Reset)

window.run()