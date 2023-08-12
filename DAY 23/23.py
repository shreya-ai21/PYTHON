# Turtle crossing game
from turtle import Screen
from player import Player
import time
from cars import Cars
from scoreboard import Scoreboard

screen=Screen()
screen.tracer(0)
screen.screensize(600,600,'white')
player=Player()
cars=Cars()
score=Scoreboard()
game_on=True
screen.listen()
screen.onkey(fun=player.move,key='w')

while(game_on):
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move()
    
    for car in cars.all_cars:
        if car.distance(player)<20:
            game_on=False
            score.collide()
    
    if(player.level_up()):
        player.next_level()
        cars.speed()
        score.update_score()
        
    

screen.exitonclick()