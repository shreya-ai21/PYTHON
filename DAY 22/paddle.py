from turtle import Turtle
class Paddle:
    
    def __init__(self):
        self.paddle=Turtle()
        self.paddle.seth(90)
        self.paddle.penup()
        self.paddle.color('white')
        self.paddle.shape('square')
        self.paddle.shapesize(1,4,0)
        
        
    def up(self):
        self.paddle.forward(20)
        
    def down(self):
        self.paddle.backward(20)