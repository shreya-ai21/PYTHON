# spirograph
from turtle import Turtle,Screen
import random as rd

obj1=Turtle()
screen=Screen()
screen.colormode(255)
obj1.hideturtle()
obj1.width(2)
obj1.speed('fastest')
no=5
for i in range(int(360/no +1)):
    obj1.circle(100)
    obj1.left(no)
    obj1.color(rd.randint(0,255),rd.randint(0,255),rd.randint(0,255))
    

screen.exitonclick()