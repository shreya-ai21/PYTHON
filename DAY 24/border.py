from turtle import Turtle

DIRECTIONS=[270,180,90,0]

class Border(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(300,300)
        self.speed('fastest')
        self.draw()
        
    def draw(self):
        self.pendown()
        for i in DIRECTIONS:
            self.setheading(i)
            self.forward(600)