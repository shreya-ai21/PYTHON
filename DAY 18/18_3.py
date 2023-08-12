# random walk
from turtle import Turtle,Screen
import random as rd

directions=[0,90,180,270]
obj=Turtle()
# obj.penup()
# obj.setpos(-100,400)
# obj.pendown()
obj.pensize(10)
screen=Screen()
screen.colormode(255)
# obj.forward(30)
for i in range(50):
    # n=rd.randint(0,100)
    # if 0<=n<=25:
    #     obj.left(90)
    # elif 25<n<=50:
    #     obj.right(90)
    # elif 50<n<=75:
    #     obj.forward(30)
    # else:
    #     obj.back(30)
    obj.pencolor(rd.randint(0,255),rd.randint(0,255),rd.randint(0,255))
    obj.forward(30)
    obj.setheading(rd.choice(directions))
    obj.speed('fastest')

screen.exitonclick()