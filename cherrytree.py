from turtle import *
import random
from time import sleep

def tree(branch_length):
    if branch_length > 3:
            if 8 <= branch_length <= 12:
                if random.randint(0,2) == 0:
                     color('snow')
                else: color('lightcoral')
                pensize(branch_length / 3) # Make the branch thicker for flowers
            elif branch_length < 8:
                color("pale violet red")
                circle(branch_length) # Draw a circle for small branches/flowers
            else:
                color('sienna')
                pensize(branch_length / 10) # Thicker for main branches
            forward(branch_length)
            a = 1.5 * random.random()
            right(20*a)
            b = 1.5 * random.random()
            tree(branch_length-10*b) # Recursively call for left branch
            left(40*a)
            tree(branch_length-10*b) # Recursively call for right branch
            right(20*a)
            up()
            backward(branch_length)
            down()
bgcolor("skyblue") # Set background color
up()
setheading(90)
back(200)
down()
tracer(60, 0)
tree(60)
exitonclick()