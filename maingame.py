from atexit import register
import turtle
import keyboard
import time
import tkinter as tk
import random

root = tk.Tk()
canvas = tk.Canvas(root,width=400,height=400)
canvas.pack()
wn = turtle.TurtleScreen(canvas)

snake = turtle.RawTurtle(wn)
snake.penup()
snake.pensize(5)
snake.Alive = True

dshape =((0, 0), (10, 10), (20, 0), (10, -10))

class Food:
    touched = False
    diamond = turtle.RawTurtle(wn)
    wn.register_shape('Diamond', dshape)
    diamond.shape('Diamond')
    diamond.pu()
    diamond.goto(random.randrange(1,200),random.randrange(1,200))


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


def powerUP():
    diamond.goto(random.randrange(1,200),random.randrange(1,200))
    time.sleep(6)
    


def snakeDied():
    snake.Alive = False
    print(snake.Alive)


#new = Food

while snake.Alive == True:
    snake.fd(0.5)
    wn.onkeypress(toLeft,'Left')
    wn.onkeypress(toRight,'Right')
    wn.onkeypress(toUp,'Up')
    wn.onkeypress(toDown,'Down')
    if snake.xcor() == 200 or snake.ycor() == 200:
        print('reached maxed')
        snakeDied()

    """ if snake.pos() == (turtle.window_width,0):
        print('limit reached')
        break """



    wn.listen()






wn.mainloop()
