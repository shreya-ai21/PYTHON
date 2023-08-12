#COFFEE MACHINE
from coffee import MENU,resources

money=0
cash=0
def report():
    global money,cash
    print("\t\t***REPORT***")
    for key in resources:
        print(f"{key}:{resources[key]}g")
    if cash!=0:
        print(f'Money:${cash}')
    print("\n\n")

def insert():
    print("Cash register:")
    quarters=int(input("How many quarters?"))
    dimes=int(input("How many dimes?"))
    nickels=int(input("How many nickels?"))
    pennies=int(input("How many pennies?"))
    inserted=0.25*quarters+0.10*dimes+0.05*nickels+0.01*pennies
    print(f"You inserted {inserted}")
    return round(inserted,3)

def ingredients(select:int):
    match select:
        case 1:
            for key in MENU["espresso"]["ingredients"]:
                resources[key]-=MENU["espresso"]["ingredients"][key]
        case 2:
            for key in MENU["latte"]["ingredients"]:
                resources[key]-=MENU["latte"]["ingredients"][key]
        case 3:
            for key in MENU["cappuccino"]["ingredients"]:
                resources[key]-=MENU["cappuccino"]["ingredients"][key]

    
# def bill(select:int):
#     global money
#     match select:
#         case 1:
            
#         case 2:
#             money=MENU["latte"]["cost"]
#         case 3:
#             money=MENU["cappuccino"]["cost"]
#     return money

def compare():
    global cash,money
    inserted=insert()
    if inserted==money:
        print("Here's your order!")
        cash+=money        
    elif inserted<money:
        print("Sorry, that's not enough money.")
        return 0
    else:
        print(f"Here's your order with a change of ${round(inserted-money,2)}!\n")
        cash+=money
    return 1


def check(select:int):
    global money
    match select:
        case 1:
            for key in MENU["espresso"]["ingredients"]:
                if MENU["espresso"]["ingredients"][key]>resources[key]:
                    print(f"Sorry, we don't have enough {key}.")
                    return 0
            money=MENU["espresso"]["cost"]
            print(f'\n\nCost of espresso:${money}')
            return 1                    
        case 2:
            for key in MENU["latte"]["ingredients"]:
                if MENU["latte"]["ingredients"][key]>resources[key]:
                    print(f"Sorry, we don't have enough {key}.\n")
                    return 0
            money=MENU["latte"]["cost"]
            print(f'\n\nCost of latte:${money}')
            return 1 
        case 3:
            for key in MENU["cappuccino"]["ingredients"]:
                if MENU["cappuccino"]["ingredients"][key]>resources[key]:
                    print(f"Sorry, we don't have enough {key}.")
                    return 0
            money=MENU["cappuccino"]["cost"]
            print(f'\n\nCost of cappuccino:${money}')
            return 1
                
# main
menu=1
while menu!=3:
    menu=int(input("What would you like to do?\n1.Order a drink\n2.Check report\n3.Exit\nChoose: "))
    match menu:
        case 1:
            select=int(input("What would you like to order?\n1.Espresso\n2.Latte\n3.Cappuccino\nChoose your drink: "))
            if(check(select)):
                if compare():
                    ingredients(select)
                else:
                    continue
        case 2:
            report()
            
exit(0)
