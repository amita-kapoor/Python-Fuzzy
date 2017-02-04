import turtle as t
import numpy as np
from math import sin, pi

def at(x, y):
    """Sets the position """
    t.penup()
    t.setposition(x,y)
    t.pendown()

def hearts(color):
    """ Draws heart at random locations """
    size, shape=50,50
    inc_si,inc_sh=10,1
    x = np.random.randint(-200,200,len(color))  #array([-100, 50, -40, 60, 100, 200, 30])
    y = np.random.randint(-300,300,len(color))
    for iteration in range(0, len(color)):
        t.delay(20)
        t.setheading(0)
        at(x[iteration], y[iteration])
        love(size,shape,color[iteration])
        if(iteration>len(color)/2.0):
            inc_si, inc_sh = -10, -1
        size,shape=size+inc_si,shape+inc_sh


def love(size,shape,color):
    """ Draws a single heart"""
    t.pensize(5)
    t.pencolor(color)
    t.fillcolor(color)
    radius = size * sin(shape * pi / 180) / (1 + sin((90 - shape) * pi / 180))
    t.fill(True)
    t.left(shape)
    t.forward(size)
    t.circle(radius, 180 + shape)
    t.right(180)
    t.circle(radius, 180 + shape)
    t.forward(size)
    t.left(180 - shape)
    t.fill(False)

def wr(to,fr):
    """ Writes on Canvas """
    t.pencolor("red")
    at(-200, 200)
    t.write("Dearest "+to, True, align="left", font=("Helvetica", 30, "normal"))
    at(-250, 0)
    t.write("Happy Valentine's Day", True, align="left", font=("Helvetica", 50, "normal"))
    at(150, -200)
    t.write("From "+fr, True, align="left", font=("Helvetica", 30, "normal"))

if __name__ =="__main__":
    to=input("Enter the name of your loved one in double quotes")
    fr = input("Enter your name in double quotes")
    wn= t.Screen()
    t.screensize(400,300)
    wn.bgcolor("turquoise")
    t.title("Love you from the core of my heart "+fr)
    colors = ["red", "gold", "orange", "yellow", "green", "blue", "purple", "violet", "DarkBlue", "coral", "DarkGreen", "magenta"]
    hearts(colors)
    wr(to,fr)
    wn.exitonclick()
