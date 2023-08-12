from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from line import Line
import time

screen=Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600)
screen.title('Pong')
# screen.tracer(0)

paddle1=Paddle()
paddle1.paddle.setposition(x=-350,y=0)
paddle2=Paddle()
paddle2.paddle.setposition(x=350,y=0)
ball=Ball()
scoreboard=Scoreboard()
line=Line()

game_on=True
while(game_on):
    time.sleep(0.01)
    screen.update()
    ball.move()
    
    screen.listen()
    screen.onkeypress(fun=paddle2.up,key='Up')
    screen.onkeypress(fun=paddle2.down,key='Down')
    screen.onkeypress(fun=paddle1.up,key='w')
    screen.onkeypress(fun=paddle1.down,key='s')
    
    # Detect collision w ball and bounce
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
        
    # Detect collision w paddle
    if (ball.distance(paddle2.paddle)<50 and ball.xcor()>330) or (ball.distance(paddle1.paddle)<50 and ball.xcor()<-330):
        ball.bounce_x()
        
    elif (ball.xcor()>340 and ball.xcor()>=0):
        ball.reset_pos()
        scoreboard.l_point()
        scoreboard.update_score()
        
    elif (ball.xcor()<-340 and ball.xcor()<=0):
        ball.reset_pos()
        scoreboard.r_point()
        scoreboard.update_score()

screen.exitonclick()