from turtle import Turtle

ALIGNMENT='center'
FONT=('Courier',20,'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(x=0,y=270)
        
    def show(self):
        self.clear()
        self.score+=1
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT,font=FONT)
        
    def quit(self):
        self.home()
        self.write(arg=f'GAME OVER!\n SCORE:{self.score}',align=ALIGNMENT,font=FONT)
        