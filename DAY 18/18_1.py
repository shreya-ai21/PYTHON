# dashed line
from turtle import Turtle,Screen
obj=Turtle()
for i in range(15):
    obj.forward(5)
    obj.penup()
    obj.forward(5)
    obj.pendown()


screen=Screen()
screen.exitonclick()