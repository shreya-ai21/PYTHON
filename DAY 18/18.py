from turtle import Turtle,Screen
obj1=Turtle()
obj1.shape('turtle')
obj1.color('red')

def square(obj1:Turtle):
    if obj1.xcor()!=0 or obj1.ycor()!=0:
        obj1.left(90)
        obj1.forward(100)
        square(obj1)
    else:
        return

screen=Screen()  
obj1.forward(100)
square(obj1)   
screen.exitonclick()