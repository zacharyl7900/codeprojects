from turtle import *
from time import sleep

setup(600, 600, 807, 117)
bgcolor("#08203D")

def go(x, y):
    up()
    goto(x, y)
    down()

def ref_line():
    pencolor("Grey")
    pensize(1)
    speed(0)
    
    #Horizontal line
    row_y = 300
    for i in range(int(600 / 15 - 1)):
        row_y -= 15
        go(-300, row_y)
        fd(600)
    left(90)
    #Vertical line
    column_x = -300
    for i in range(int(600/15 - 1)):
        column_x += 15
        go(column_x, 300)
        fd(600)
    right(90)
    go(0, 0)

ref_line()

a, b = 0 , 15
while a < 500:
    color("DeepSkyBlue", "SkyBlue")
    pensize(2)
    begin_fill()
    for i in range(4):
        forward(a)
        left(90)
    pencolor("OrangeRed")
    circle(a, 90)
    temp = a
    a = b
    b = temp + b
mainloop()