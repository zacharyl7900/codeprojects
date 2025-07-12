from turtle import *
from time import sleep
import random

def tree (branchLen):
    if branchLen > 3:
        if 8 <= branchLen <= 12:
            if random.randint (0, 2) == 0:
                color("snow")
            else:
                color('lightcoral')
            pensize(branchLen / 3)

elif branchLen < 8:
            if random.randint(0, 1) == 0:
                color("snow")
            else:
                color('lightcoral')
                pensize(branchLen / 2)

elif:
    color('sienna')
    pensize(branchLen / 10)

forward(branchLen)
    a = 1.5 * random.random()
    right(20 * a)
    b = 1.5 * random.random()

def tree(branchLen):
     if branchLen > 3:
          if 8 <= branchLen <= 12:
               if random.randint(0, 2) == 0:
                    color('snow')
                else:
                    color('lightcoral')
                pensize(branchLen / 3)