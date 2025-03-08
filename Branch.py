import turtle

pen = turtle.Turtle()

pen.penup()
pen.goto(0, -200)
pen.pendown()

pen.setheading(90)
pen.pensize(7)
pen.pencolor('Green')


def branch(pen_list, branch_len):
    if branch_len > 15:
        new_list = []
        turtle.tracer(4)
        for pen in pen_list:
            pen.ht ()
            pen.forward(branch_len)
            new_pen = pen.clone()
            pen.left(65)
            new_pen.right(65)
            new_list.append(pen)
            new_list.append(new_pen)
        branch(new_list, branch_len * 0.618)
        turtle.tracer(1)

for i in range(20,000):
    branch([pen], 200) 
turtle.done()