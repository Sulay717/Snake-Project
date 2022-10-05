import turtle
import keyboard
import time

wn = turtle.Screen()
snake = turtle.Turtle()

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
    if keyboard.is_pressed('Left'):
        toLeft()
    elif keyboard.is_pressed('Right'):
        toRight()
    elif keyboard.is_pressed('Up'):
        toUp()
    elif keyboard.is_pressed('Down'):
        toDown()




wn.onkey(toRight,'a')


wn.listen()
wn.mainloop()
