from logging import root
import turtle
import keyboard
import time
import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root,width=500,height=500)
canvas.pack()
wn = turtle.TurtleScreen(canvas)

snake = turtle.RawTurtle(wn)
snake.pensize(5)



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
    if snake.xcor() == wn.window_height():
        print('reached maxed')
        break

    """ if snake.pos() == (turtle.window_width,0):
        print('limit reached')
        break """



    wn.listen()






wn.mainloop()
