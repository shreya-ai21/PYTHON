from turtle import Screen
import time
from snake_class import Snake
from food import Food
from scoreboard import Scoreboard
from border import Border

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.colormode(255)
screen.tracer(0)

border=Border()
snake=Snake()
food=Food()
score=Scoreboard()

game_end=False

while not game_end:
    
    screen.listen()
    screen.onkey(snake.up,key='Up')
    screen.onkey(snake.down,key='Down')
    screen.onkey(snake.left,key='Left')
    screen.onkey(snake.right,key='Right')
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    
    if snake.header.distance(food) < 15:
        snake.color=food.colour
        food.refresh()
        snake.grow()
        score.score+=1
        score.show()
        
    if snake.border() or snake.tail():
        score.resetgame()
        reset=screen.textinput(title='Do you want to play again?',prompt="Press Y to play again.\nPress Cancel to quit.")
        if reset.lower()=='y':
            snake.resetsnek()
        else:
            game_end=True
screen.exitonclick()