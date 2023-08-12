import random
import os
from data import data

def algo(guess:str):
    global opt1,opt2
    if opt1['follower_count']>opt2['follower_count']:
        answer=opt1['name']
        data.remove(opt2)
    elif opt1['follower_count']<opt2['follower_count']:
        answer=opt2['name']
        data.remove(opt1)
        opt1=opt2
    elif opt1['follower_count']==opt2['follower_count']:
        return 1
    if guess==answer:
        return 1
    else:
        return 0
    
logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

score=0
answer=1
opt1=random.choice(data)
opt2=random.choice(data)
if opt1==opt2:
    opt2=random.choice(data)
while answer==1:
    os.system('cls')
    if answer==1 and score>0:
        print(f"Correct! Your score is {score}")
    print(logo)
    print(f'Compare A: {opt1["name"]}, a {opt1["description"]}, from {opt1["country"]}. ')
    print(vs)
    print(f'Against B: {opt2["name"]}, a {opt2["description"]}, from {opt2["country"]}. ')
    guess=input(f"Who has higher followers?\nA:{opt1['name']}\nB:{opt2['name']}\nChoose(A/B): ")
    if guess.upper()=='A':
        guess=opt1['name']
    else:
        guess=opt2['name']
    answer=algo(guess)
    if answer:
        opt2=random.choice(data)
        if opt1==opt2:
            opt2=random.choice(data)
        score+=1
    else:
        print(f"\nSorry, that's wrong! You lost with a score of {score}")


