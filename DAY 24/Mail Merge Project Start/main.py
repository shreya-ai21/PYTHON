# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('.\Input\Letters\starting_letter.txt', 'r') as start:
    content = start.read()

# with open("./Input/Names/invited_names.txt") as names_file:
#     names=names_file.readlines()
names = ['Aang',
         'Zuko',
         'Appa',
         'Katara',
         'Sokka',
         'Momo',
         'Uncle Iroh',
         'Toph']
for i in range(1, len(names)):
    with open(f'.\Output\ReadyToSend\{i}.txt', 'w') as new_file:
        string = content.replace("[name]", names[i-1], -1)
        new_file.write(string)
        # for j in range(1, len(content)):
        #     new_file.write(content[j])
