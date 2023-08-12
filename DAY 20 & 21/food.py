from turtle import Turtle
import random as rd
class Food(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape('circle')
        self.shapesize(0.5,0.5,1)
        self.penup()
        self.speed('fastest')
        self.colour=(rd.randint(1,255),rd.randint(0,255),rd.randint(0,255))
        self.create_food()

        
    def create_food(self):    
        self.color((self.colour))    
        self.xpos=rd.randint(-280,280)
        self.ypos=rd.randint(-280,280)
        self.goto(self.xpos,self.ypos)
        
    
    def refresh(self):
        self.colour=(rd.randint(1,255),rd.randint(0,255),rd.randint(0,255))
        self.color((self.colour))        
        new_x=rd.randint(-290,290)
        new_y=rd.randint(-290,290)
        self.goto(new_x,new_y)
