# Spot painting
import colorgram as clr
from turtle import Turtle,Screen
import random as rd
obj=Turtle()
screen=Screen()
screen.colormode(255)
# colorgram doesnt owrk in vs code
# colors=clr.extract('E:\\UDEMY\\PYTHON\\DAY 18\\colorgram\\download.jpeg',50)
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
rgb = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

obj.penup()
obj.speed('fastest')
obj.setheading(225)
obj.forward(353)
obj.seth(0)
dots=100
for i in range(1,dots+1):        
    obj.dot(20,rd.choice(rgb))
    obj.forward(50)
    if i%10==0:
        obj.seth(90)
        obj.forward(50)
        obj.seth(180)
        obj.forward(500)
        obj.seth(0)
obj.hideturtle()

screen.exitonclick()
   

