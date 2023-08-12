#Password Generator
import random
print("Password Generator")
char_no=int(input("How many characters do you want in your password? "))
symbol_no=int(input("How many symbols? "))
num_no=int(input("How many numbers?"))
password=[]

for i in range(0,char_no-symbol_no-num_no):
    char=chr(random.randint(65,122))
    while 90<ord(char)<97:
        char=chr(random.randint(65,122))
    password.append(char)

for j in range(0,symbol_no):
    password.append(chr(random.randint(33,48)))

for k in range(0,num_no):
    password.append(random.randint(0,9))

random.shuffle(password)
print(f"Your password can be:")
for i in password:
    print(i,end='')






