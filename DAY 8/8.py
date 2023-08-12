# CEASER CIPHER
def encode():
    message=input("Enter your message: ")
    shift=int(input("Enter the shift number: "))
    encoded=''
    for i in message:
        c_shift=ord(i)+shift
        if c_shift>90 and c_shift<97:
            c_shift=64+(c_shift-90)
        elif c_shift>122:
            c_shift=96+(c_shift-122)
        encoded=encoded+(chr(c_shift))
    
    print(f"The encoded message is {encoded}")
    decode(encoded,shift) if input("Do you want to decode the message?(yes/no)").upper()=='YES' else exit(0)

def decode(encoded: str, shift: int):
    decoded=''
    for i in encoded:
        c_shift=ord(i)-shift
        if c_shift<65:
            c_shift=91-(65-c_shift)
        elif c_shift<97 and c_shift>91:
            c_shift=123-(97-c_shift)
        decoded=decoded+(chr(c_shift))
    print(f"The decoded message is {decoded}")
    encode() if input("Do you want to encode another message?(yes/no)").upper()=='YES' else exit(0)

choice=input("Press e for encoding/Press d for decoding: ")
if choice.upper()=='E':
    encode() 
elif choice.upper()=='D':
    message=input("Enter your message: ")
    shift=int(input("Enter the shift number: "))
    decode(message,shift)


# #Write your code below this line 👇
# def paint_calc(height: int, width: int, cover:5):
#     no=(height*width)/cover
#     if no>int(no): 
#           no=int(no+1) 
#     print(f"You'll need {no} cans of paint.")



# #Write your code above this line 👆
# # Define a function called paint_calc() so that the code below works.   

# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)



