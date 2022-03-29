from sched import scheduler
from pycat.core import Window,Scheduler
from pycat.extensions import Turtle
from math import sqrt
window = Window(width = 1200,height = 600)
turtle = window.create_sprite(Turtle)
turtle.x = 0
turtle.y = 0
i = 0
def draw_triangles():
    global i
    if i < 35:
        i += 1
        turtle.rotation = 0
        turtle.move_forward(1200)
        for _ in range(60):
            turtle.rotation = 120
            turtle.move_forward(20)
            turtle.rotation = 240
            turtle.move_forward(20)
        turtle.y += 10 * sqrt(3)
        turtle.rotation = 0
        turtle.move_forward(1200)
        turtle.y += 10 * sqrt(3)
        for _ in range(60):
            turtle.rotation = 240
            turtle.move_forward(20)
            turtle.rotation = 120
            turtle.move_forward(20)
        
    

Scheduler.update(draw_triangles,0.5)




 
    

    
   

window.run()