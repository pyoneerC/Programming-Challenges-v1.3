from tkinter import *
from ball import * # importing ball classes
import time

window = Tk()

# defining canvas size
WIDTH = 500
HEIGHT = 500

canvas = Canvas(window,width=WIDTH,height=HEIGHT) # clearing and assigning variables and canvas size
canvas.pack() # packing

# as we defined the class in the class module, we only need to stablish some parameters and all will be ready, as we using the values from the ball classes already
volley_ball = Ball(canvas,0,0,100,1,1,"white")
tennis_ball = Ball(canvas,0,0,50,4,3,"yellow")
basket_ball = Ball(canvas,0,0,125,3,5,"orange")
bowling_ball = Ball(canvas,0,0,75,2,1,"black")

while True: # forever
    # calling move function that inherits from ball, we only call var and .move()
    volley_ball.move() 
    tennis_ball.move()
    basket_ball.move()
    bowling_ball.move()
    window.update() # update window (per every .01 second)
    time.sleep(0.01) # each .01 second

    window.mainloop() # open GUI