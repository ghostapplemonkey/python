from turtle import window_height
from pycat.core import Window
from pycat.extensions import Turtle
window = Window(width = 1200,height = 600)
turtle = window.create_sprite(Turtle)
turtle.x = 200
turtle.y = 300
 
    
def draw_circle():    
    for _ in range(360):
        turtle.move_forward(2)
        turtle.turn_right(1)
def draw_circles():
    for _ in range(20):
        draw_circle()
        turtle.rotation += 18
for _ in range(9):
    draw_circles()
    turtle.pen_up()
    turtle.x += 100
    turtle.pen_down()
    
   

window.run()