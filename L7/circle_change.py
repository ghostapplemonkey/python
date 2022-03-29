from turtle import window_height
from pycat.core import Window
from pycat.extensions import Turtle
window = Window(width = 1200,height = 600)
turtle = window.create_sprite(Turtle)
turtle.x = 200
turtle.y = 300
 
    
def draw_circle(size):    
    for _ in range(360):
        turtle.move_forward(size)
        turtle.turn_right(1)
draw_circle(3)



    
   

window.run()