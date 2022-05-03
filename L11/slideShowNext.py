from cProfile import label
from turtle import width
from pycat.core import Sprite, Window, Scheduler,Color

window = Window(height=600,width=1200)

picture = ["image/meerkat.jpg",
           "image/hedgehog.jpg",
           "image/cat.jpg",
           "image/bird.jpg",
           "image/cow.jpg",
           "image/sheep.jpg",
           "image/seal.jpg",
           "image/squirrel.jpg",
           "image/1.jpg",
           "image/2.jpg",
           "image/3.jpg",
           "image/4.jpg",
           "image/5.jpg",
           "image/6.jpg",
           "image/7.jpg",
           "image/8.jpg",
           "image/9.jpg",
           "image/10.jpg"]
labelname =  ["meerkat",
           "hedgehog",
           "cat",
           "bird",
           "cow",
           "sheep",
           "seal",
           "squirrel",
           "bus stop 1",
           "bus stop 2",
           "bus stop 3",
           "bus stop 4",
           "bus stop 5",
           "bus stop 6",
           "strawberry house",
           "watch out for shark",
           "cool stair",
           "roller coaster"]
textname = window.create_label(text="name of image",y=580,x=400,color = Color.WHITE)
textname.font_size = 40
class ButtonNext(Sprite):
    def on_create(self):
        self.scale = 0.25
        self.x = 220
        self.y = 80
        self.image = "image/arrow.png"
        self.image_number = 0
    def on_left_click(self):
        self.image_number += 1
        window.background_image = picture[self.image_number%len(picture)]
        textname.text = labelname[self.image_number%len(labelname)]

nextButton = window.create_sprite(ButtonNext)

class ButtonPrevious(Sprite):
    def on_create(self):
        self.scale = 0.25
        self.x = 80
        self.y = 80
        self.image = "image/arrow.png"
        self.rotation = 180
        self.image_number = 0
    def on_left_click(self):
        nextButton.image_number -= 1
        window.background_image = picture[nextButton.image_number%len(picture)]
        textname.text = labelname[nextButton.image_number%len(labelname)]

window.create_sprite(ButtonPrevious)




window.run()
