import random as rd
from turtle import Turtle
COLORS=['green','blue','red','black','violet','orange','pink','maroon','cyan','indigo','yellow']

HEAD=180
STARTING_MOVE=5
MOVE_INCREMENT=10

class Cars:
    def __init__(self) -> None:
        self.all_cars=[]
        self.finishline()
        self.car_speed=STARTING_MOVE
        
    def finishline(self):
        line=Turtle()
        line.hideturtle()
        line.penup()
        line.goto(x=-400,y=280)
        line.width(5)
        line.pendown()
        line.forward(900)
    
    def create_cars(self):
        random_chance=rd.randint(1,5)
        if random_chance==1:
            new_car=Turtle(shape='square')
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.speed('slowest')
            new_car.penup()
            new_car.color(rd.choice(COLORS))
            new_car.goto(300,rd.randint(-250,250))
            new_car.setheading(HEAD)
            self.all_cars.append(new_car)
        
    def move(self):
        for car in self.all_cars:
            car.forward(self.car_speed)
    
    def speed(self):
        self.car_speed+=MOVE_INCREMENT
    
        
    