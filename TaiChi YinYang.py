from turtle import *

def draw_half_circle(radius, color_fill):
    color("black", color_fill)
    begin_fill()
    circle(radius, 180)
    circle(radius // 2, 180)
    circle(-radius // 2, 180)
    end_fill()

def draw_tai_chi():
    speed(0)
    penup()
    goto(0, -200)
    pendown()
    color("black", "white")
    begin_fill()
    circle(200)
    end_fill()
    
    penup()
    goto(0, 0)
    setheading(90)
    pendown()
    draw_half_circle(200, "black")
    
    penup()
    goto(0, 0)
    setheading(270)
    pendown()
    draw_half_circle(200, "white")
    
    penup()
    goto(0, 100)
    pendown()
    color("black", "black")
    begin_fill()
    circle(20)
    end_fill()
    
    penup()
    goto(0, -100)
    pendown()
    color("white", "white")
    begin_fill()
    circle(20)
    end_fill()

def main():
    setup(600, 600)
    bgcolor("white")
    hideturtle()
    draw_tai_chi()
    done()

if __name__ == '__main__':
    main()