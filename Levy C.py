#WHAT IS A LEVY C CURVE?
#In mathematics, the Lévy C curve is a self-similar fractal curve that was first described and whose differentiability properties were analysed by Ernesto Cesàro in 1906 and Georg Faber in 1910, but now bears the name of French mathematician Paul Lévy, who was the first to describe its self-similarity properties as well as to provide a geometrical construction showing it as a representative curve in the same class as the Koch curve. It is a special case of a period-doubling curve, a de Rham curve.
# See https://en.wikipedia.org/wiki/Levy_C_curve

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
