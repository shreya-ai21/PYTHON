#HANGMAN
import random
import os
words=['Red','Blue','Yellow','Brown','Green','Magenta','Purple','Gray','Black','White','Pink']
ans=random.choice(words).upper()
# line='_'*len(rand)
line=[]
backup=ans
chances=6

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
DEAD
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

for i in range(len(ans)):
    line.append("_")

index_val=0
while(index_val!=-1 and chances!=-1):
    print("\nThe word is:")
    for item in line:
        print(item,end=' ')
    test=input("\nGuess a letter: ").upper()

    os.system('cls')

    if test in ans:
        print(f"\n{test} is there!")
        line[ans.index(test)]=test
        ans=ans.replace(test,'_',1)
    else:
        print("Not there")
        print(stages[chances])
        chances-=1

    try:
        index_val=line.index('_')
    except ValueError:
        index_val=-1


if index_val==-1:
    print(f"\nThe word is {''.join(line)}.You won!")
else:
    print(f"\nThe word was {backup}.You lost and died.")
