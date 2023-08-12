from turtle import Turtle,Screen
obj=Turtle()
obj.speed('fastest')
screen=Screen()
screen.listen()

def forward():
    obj.forward(10)
def back():
    obj.back(10)
def anti():
    obj.left(15)
def clock():
    obj.right(15)
def clear():
    obj.clear()
    obj.penup()
    obj.home()
    obj.pendown()
    # if key.lower=='w':
    #     obj.forward(10)
    # elif key.lower=='s':
    #     obj.back(10)
    # elif key.lower=='a':
    #     obj.left(5)
    # elif key.lower=='d':
    #     obj.right(5)
screen.onkey(key='w',fun=forward)
screen.onkey(key='s',fun=back)
screen.onkey(key='a',fun=anti)
screen.onkey(key='d',fun=clock)
screen.onkey(key='c',fun=clear)

screen.exitonclick()