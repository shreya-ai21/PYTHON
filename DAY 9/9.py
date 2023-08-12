#BLIND AUCTION
import os
auction={}
flag='yes'


print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')


while flag.upper()=='YES' or flag.upper()=="Y":
    # person=[]
    key=input("Enter your name: ")
    auction[key]=float(input("What's your bid:$"))
    # person.append(name)
    # person.append(bid)
    # auction[name]=person
    flag=input("Are there any other bidders?")
    while flag.upper()!='YES':
        if flag.upper()=='NO':
            break
        flag=input("Enter a valid option. Are there any other bidders?")
    os.system('cls')
max=0
for key in auction:
    if auction[key]>max:
        max=auction[key]
        name=key
print(f"{name} wins the auction with a bid of ${max}!")