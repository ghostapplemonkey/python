from re import X
from pycat.core import Window

window = Window()

window.background_image = "image/forest_background.jpg"


animal = window.create_sprite()
animal.image = "image/"+input("Which animal do you like?(pig,rat,owl,elephant,rooster,tiger,wildcat)")+".png" 
animal.x = int(input("It's x?"))
animal.y = int(input("And it's y?"))
animal.scale = int(input("How about the size(normal is 1)"))
animal.rotation = int(input("Where should it point to?"))

msg = ("animal image = "+str(animal.image)+
       ", x = "+str(animal.x)+
       ", y = "+str(animal.y)+
       ", scale = "+str(animal.scale)+
       ", rotation = "+str(animal.rotation))
print(msg)
# print("animal image = ", animal.image)
# print("x = ", animal.x)
# print("y = ", animal.y)
# print("scale = ", animal.scale)
# print("rotation = ", animal.rotation)


window.run()