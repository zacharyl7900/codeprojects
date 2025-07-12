#l = []
#while True:
#    itemToOrder = input("What item from the store would you like: ")
#    l.append(item)
#    print(l)

#number1 = input("Enter 1 or 0: ")
#number2 = input("Enter 1 or 0: ")
#if number1 == number2:
#    print(True)
#else:
#    print(False)

#number = input("Enter a two-digit number: ")
#digits = [digit for digit in number]
#print(digits)
import turtle
import random

colors = ["red", "blue", "green", "purple", "orange", "pink", "brown", "gray"]

t = turtle.Turtle()

for i in range(16):
    
    random_color = random.choice(colors)
    t.pencolor(random_color)
    t.forward(100)
    t.right(90)

turtle.done()