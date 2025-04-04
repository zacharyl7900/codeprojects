import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
turtle.colormode(255)
t = turtle.Turtle()
t.speed("fastest")

def draw_firework(x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    firework_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    t.color(firework_color)
    
    for _ in range(36): 
        t.forward(size)
        t.backward(size)
        t.right(10)

for _ in range(10): 
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    
    size = random.randint(60, 100) if random.random() < 0.8 else random.randint(20, 50)
    
    draw_firework(x, y, size)

turtle.done()