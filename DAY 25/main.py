import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
img = "./blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv('./50_states.csv')
states = data['state'].to_list()
guessed = []


while len(guessed) < 50:
    ans = screen.textinput(title=f"{len(guessed)}/50 states correct",
                           prompt="What's another state name?").title()
    if ans in states:
        guessed.append(ans)
        states.remove(ans)
        answer = turtle.Turtle()
        answer.hideturtle()
        answer.speed('fastest')
        answer.penup()
        state_data = data[data.state == ans]
        answer.goto(int(state_data.x), int(state_data.y))
        answer.write(arg=ans)
    elif ans == 'Exit':
        with open('./states_to_learn.csv.txt', 'w') as f:
            for state in states:
                f.write(state, end='\n')
        break
