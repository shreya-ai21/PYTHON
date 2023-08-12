# polygons
from turtle import Turtle,Screen
import random as rd
obj=Turtle()
screen=Screen()
screen.colormode(255)
# obj.penup()
# obj.setposition(-150,400)
# obj.pendown()
def polygon(no:int):
    obj.color(rd.randint(0,255),rd.randint(0,255),rd.randint(0,255))
    for i in range(0,no):
        obj.forward(100)
        obj.right(360/no)        
    # obj.home()
for i in range(3,11):
    polygon(i)

screen.exitonclick()
    


