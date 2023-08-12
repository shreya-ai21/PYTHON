from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self)-> None:
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.level=0
        self.update_score()
    
    def update_score(self):
        self.level+=1
        self.speed(10)
        self.clear()
        self.goto(0,290)
        self.write(arg=f"Level:{self.level}",align='center',font=('Courier',24,'bold'))

    def collide(self):
        text=Turtle()
        text.write(arg=f'GAME OVER\n Score:{self.level-1}',font=('Courier',24,'bold'),align='center')
        text.penup()