from turtle import Turtle,Screen
obj=Turtle()
screen=Screen()
screen.colormode(255)


def move_forward():
    obj.forward(10)
    
screen.listen()
screen.onkey(key='space',fun=move_forward)
screen.exitonclick()