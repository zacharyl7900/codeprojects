import turtle

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")

angle = 59
num_steps = 500
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

for i in range(num_steps):
    t.pencolor(colors[i % len(colors)])  
    
    t.fd(i / 5)
    t.lt(angle)

turtle.done()