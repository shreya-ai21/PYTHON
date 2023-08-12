from turtle import Turtle,Screen
import random

is_race_on=False

global ypos
def caly(n):
    global ypos
    ypos=-400/7

    return (-400/2.35)- (7-n)*(ypos)
    

screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race?")

colors=['red','orange','yellow','green','blue','indigo','violet']

turtles=[]

for i in range(7):
    turt=Turtle(shape='turtle')
    turt.color(f'{colors[i]}')
    turt.penup()
    turt.goto(x=-230,y=caly(i+1))
    turt.speed('fast')
    turtles.append(turt)

if user_bet:
    is_race_on=True

while is_race_on:
    
    for turtle in turtles:
        num=random.randint(0,10)
        turtle.forward(num)
        if turtle.xcor()>230:
            is_race_on=False
            print(f'The {turtle.pencolor()} turtle won!')
            if user_bet==turtle.pencolor():
                print("You win!")
            else:
                print("You lost")
            
        

screen.exitonclick()