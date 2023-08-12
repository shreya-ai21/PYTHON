bill=float(input("What is the total bill? $"))
ppl=int(input("How many people are splitting the bill? "))
flag=0
while flag==0:
    perc=int(input("What percentage tip would you like to pay? (10/12/15)"))
    if perc==10 or perc==12 or perc==15:
        pay=(bill+(perc/100*bill))/ppl
        print(f"Each person has to pay ${round(pay,2)}")
        flag=1
    else:
        print("Enter a valid number")