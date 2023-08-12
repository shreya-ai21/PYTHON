from turtle import Turtle

class Line(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0,300)
        self.setheading(270)
        self.draw()
    
    def draw(self):
        for i in range(30):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
            