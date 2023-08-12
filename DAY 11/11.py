#BLACKJACK CAPSTONE PROJECT

import random
import os

def display():
    print(f"\n\nYour final hand:{player},final score={sum(player)}")
    print(f"Dealer's final hand:{dealer}, final score={sum(dealer)}")

def deal_dealer():
    while sum(dealer)<17:
        dealer.append(int(random.choice(cards)))
        if sum(dealer)>21:
            if 11 in dealer:
                dealer[dealer.index(11)]=1
            


def deal():
    """Deals a card to the player's cards"""
    player.append(int(random.choice(cards)))
    if sum(player)<=21:
        print(f"Your cards:{player},current score={sum(player)}")
        print(f"Dealer's first card:{dealer[0]}")
        cont=input("Type 'y' to get another card, type 'n' to pass:")
    else:
        if 11 in player:
            player[player.index(11)]=1
            print(f"Your cards:{player},current score={sum(player)}")
            print(f"Dealer's first card:{dealer[0]}")
            cont=input("Type 'y' to get another card, type 'n' to pass:")
        else:
            cont='n'
    return cont

def algo():
    """Evaluates the winner of the game"""
    display()
    if sum(player)>21 or (sum(player)>21 and sum(dealer)>21):
        print("You went over. You lose :(")
    elif sum(dealer)>21:
        print("Dealer went over. You win!")
    elif sum(player)==sum(dealer):
            print("It's a draw")
    elif sum(player)==21:
        print("You won with blackjack!!")
    elif sum(dealer)==21:
        print("Dealer wins with blackjack!")
    elif sum(player)>sum(dealer):
            print("You win!")
    else:
        print("Dealer has a better hand. You lose.")
    print("\n\n")
    game=input("Do you want to play a game of blackjack?Type 'y' or 'n':")
    return game


#main
cards=[2,3,4,5,6,7,8,9,10,10,10,10,11]
game=input("Do you want to play a game of blackjack?Type 'y' or 'n':")
while game.upper()=='Y':
    player=[]
    dealer=[]

    for i in range(2):
        player.append(int(random.choice(cards)))
        dealer.append(int(random.choice(cards)))

    os.system('cls')

    print("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
""")
    print(f"Your cards:{player},current score={sum(player)}")
    print(f"Dealer's first card:{dealer[0]}")

    cont=input("Type 'y' to get another card, type 'n' to pass:")
    while cont.upper()=='Y':
        cont=deal()
    if cont.upper()=="N":
        deal_dealer()
        game=algo()





    

