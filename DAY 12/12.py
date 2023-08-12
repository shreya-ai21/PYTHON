#NUMBER GUESSING GAME
import random
import os

answer=random.randint(1,100)
tries=1
def logic(guess:int,chances:int):
    global tries
    if chances==1 and guess!=answer:
        print(f"\nYou've run out of chances. The answer was {answer}.\n")
        return
    if guess==answer:
        print(f"\nYou guessed it! The answer is {answer}. You took {tries} tries.\n")
    elif guess<answer:
        guess=int(input(f"Too low. You have {chances-1} chances left.\nGuess a higher number: "))
        tries+=1
        logic(guess,chances-1)
    else:
        guess=int(input(f"Too high. You have {chances-1} chances left.\nGuess a lower number: "))
        tries+=1
        logic(guess,chances-1)
    
game='y'
while game.upper()=='Y':
    os.system('cls')
    print(
        """

   ____ _   _ _____ ____ ____          
  / ___| | | | ____/ ___/ ___|         
 | |  _| | | |  _| \___ \___ \         
 | |_| | |_| | |___ ___) |__) |        
 |_____|_____|_____|____/____/         
 |_   _| | | | ____|                   
   | | | |_| |  _|                     
   | | |  _  | |___                    
  _|_|_|_| |_|______ ____  _____ ____  
 | \ | | | | |  \/  | __ )| ____|  _ \ 
 |  \| | | | | |\/| |  _ \|  _| | |_) |
 | |\  | |_| | |  | | |_) | |___|  _ < 
 |_| \_|\___/|_|  |_|____/|_____|_| \_|
                                       

    """
    )
    print("Welcome to the Number Guessing Game!")
    print("The answer is a number between 1 to 100.")
    chances=int(input("Levels-\nPress 1 for easy\nPress 2 for hard\nChoose a difficulty(easy/hard): "))
    if chances==1:
        chances=10
    else:
        chances=5
    print(f"You have {chances} chances to guess the number.")
    guess=int(input("Make a guess:"))
    logic(guess,chances)
    game=input("Would you like to play again?(y/n)")


