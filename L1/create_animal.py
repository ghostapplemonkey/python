from pycat.core import Window

window = Window()

window.background_image = "forest_background.jpg"


animal_image = input("Which animal do you like?(pig,rat,owl,elephant,rooster,tiger,wildcat)")+".png"
animal_number = input("How many?(1~3)")
if animal_number == "1":        
    animal1 = window.create_sprite()
    animal1.image = animal_image 
    animal1.x = int(input("It's x?"))
    animal1.y = int(input("And it's y?"))
    animal1.scale = int(input("How about the size(normal is 1)"))
if animal_number == "2":        
    animal1 = window.create_sprite()
    animal2 = window.create_sprite()
    animal1.image = animal_image
    animal2.image = animal_image
    animal1.x = int(input("First x?"))
    animal1.y = int(input("And it's y?"))
    animal2.x = int(input("Second x?"))
    animal2.y = int(input("And it's y?"))
    animal1.scale = int(input("How about the size(normal is 1)"))
    animal2.scale = animal1.scale
if animal_number == "3":        
    animal1 = window.create_sprite()
    animal2 = window.create_sprite()
    animal3 = window.create_sprite()
    animal1.image = animal_image
    animal2.image = animal_image
    animal3.image = animal_image
    animal1.x = int(input("First x?"))
    animal1.y = int(input("And it's y?"))
    animal2.x = int(input("Second x?"))
    animal2.y = int(input("And it's y?"))
    animal3.x = int(input("Third x?"))
    animal3.y = int(input("And it's y?"))
    animal1.scale = int(input("How about the size(normal is 1)"))
    animal2.scale = animal1.scale
    animal3.scale = animal1.scale


window.run()