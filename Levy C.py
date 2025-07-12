from turtle import *

setup(600, 600, 512, 168)

bgcolor("black")
pensize(2)
penup()
goto(-145, -100)
pendown()
hideturtle()

def levy(n):
    global r, g, b
    r = r + 1
    g = g + 2
    b = b + 3
    pencolor( r % 200, g % 200 , b % 200 )
    if n < 12:
        forward(5)
        return
    n =(n ** 2 / 2) **0.5
    left(45)
    levy(n)
    right(90)
    levy(n)
    left(45)


speed(0)
tracer(20)
colormode(255)
r = 128
g = 128
b = 128
pencolor("white")
levy(5000)
tracer(1)
mainloop()