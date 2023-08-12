from turtle import Turtle

STARTING_POS=(0,-280)
MOVE_DIST=10
FINISH=280

class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.speed(10)
        self.goto(STARTING_POS)
        self.color('black')
        self.setheading(90)
        
    def move(self):
        self.forward(MOVE_DIST)
    
    
    def level_up(self):
        if self.ycor()>=FINISH:
            return True
        else:
            return False
        
        
    def next_level(self):
        self.goto(STARTING_POS)