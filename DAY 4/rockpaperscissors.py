import random
moves=['rock','paper','scissors']
computer_move=random.choice(moves)
your_move=input("Choose your move (rock/paper/scissors): ")
moves={
    "rock": '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',

"paper": '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',

"scissors": '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
}
print(f"Your move: {moves[your_move]}\n{your_move}\nComputer's move:{moves[computer_move]}\n{computer_move}\n")
if computer_move[0].upper()==your_move[0].upper():
    print("it's a tie!")
elif computer_move.upper()=='ROCK' and your_move.upper()=='PAPER':
    print('You win!')
elif computer_move.upper()=='ROCK' and your_move.upper()=='SCISSORS':
    print('Computer wins!')
elif computer_move.upper()=='PAPER' and your_move.upper()=='ROCK':
    print('Computer wins!')
elif computer_move.upper()=='PAPER' and your_move.upper()=='SCISSORS':
    print('You win!')
elif computer_move.upper()=='SCISSORS' and your_move.upper()=='ROCK':
    print('You win!')
elif computer_move.upper()=='SCISSORS' and your_move.upper()=='PAPER':
    print('Computer wins!')
else:
    print('Enter a valid input')
    