# Password Generator
import random


class Password():
    def __init__(self):
        self.generate()

    def generate(self):
        char_no = random.randint(2, 7)
        symbol_no = random.randint(2, 4)
        num_no = random.randint(2, 4)
        password = []

        for i in range(0, char_no):
            char = chr(random.randint(65, 122))
            while 90 < ord(char) < 97:
                char = chr(random.randint(65, 122))
            password.append(char)

        for j in range(0, symbol_no):
            password.append(chr(random.randint(33, 48)))

        for k in range(0, num_no):
            password.append(random.randint(0, 9))

        random.shuffle(password)
        password = ''.join(str(i) for i in password)
        return password
