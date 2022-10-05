from curses import window
from tkinter import W
import turtle
import keyboard
import time

wn = turtle.Screen()
wn.screensize(400,400)

snake = turtle.Turtle()
snake.pensize(5)

h = wn.canvheight
w = wn.canvwidth

print(h,w)




def toRight():
    if snake.heading() != 180:
        if snake.heading() != 0:
            snake.setheading(0)
    
def toLeft():
    if snake.heading() != 0:
        if snake.heading() != 180:
            snake.setheading(180)

def toUp():
    if snake.heading() != 270:
        if snake.heading() != 90:
            snake.setheading(90)

def toDown():
    if snake.heading() != 270:
        if snake.heading() != 90:
            snake.setheading(270)
        

while True:
    snake.fd(0.5)
    wn.onkeypress(toLeft,'Left')
    wn.onkeypress(toRight,'Right')
    wn.onkeypress(toUp,'Up')
    wn.onkeypress(toDown,'Down')
    if snake.pos() == (w,0):
        print('Nax reach')
        break


    """ if snake.pos() == (turtle.window_width,0):
        print('limit reached')
        break """



    wn.listen()






wn.mainloop()
