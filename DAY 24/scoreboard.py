from turtle import Turtle

ALIGNMENT='center'
FONT=('Courier',20,'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('DAY 24\highscore.txt','r') as data:
            self.highscore=int(data.read())
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(x=0,y=270)
        self.show()
        
    def show(self):
        self.clear()
        self.write(arg=f"Score: {self.score}\t High Score:{self.highscore}", align=ALIGNMENT,font=FONT)
        
    def resetgame(self):
        if self.score>self.highscore:
            self.highscore=self.score
        self.score=0
        self.show()
        with open('DAY 24\highscore.txt','w') as hs:
            hs.write(f"{self.highscore}")
        
    # def quit(self):    
        # self.home()
        # self.write(arg=f'GAME OVER!\n SCORE:{self.score}',align=ALIGNMENT,font=FONT)
    