from turtle import Screen
import time
from snake_class import Snake
from food import Food
from scoreboard import Scoreboard
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.colormode(255)
screen.tracer(0)

snake=Snake()
food=Food()
score=Scoreboard()

screen.listen()
screen.onkey(snake.up,key='Up')
screen.onkey(snake.down,key='Down')
screen.onkey(snake.left,key='left')
screen.onkey(snake.right,key='Right')
game_end=False

while not game_end:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    
    
    if snake.header.distance(food) < 15:
        snake.color=food.colour
        food.refresh()
        snake.grow()
        score.show()
        
    
    if snake.border() or snake.tail():
        game_end=True
        score.quit()
    
screen.exitonclick()