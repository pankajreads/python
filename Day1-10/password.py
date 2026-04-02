import random
keyboard_symbols = [
    '`', '~', '!', '@', '#', '$', '%', '^', '&', '*',
    '(', ')', '-', '_', '=', '+', '[', ']', '{', '}',
    '\\', '|', ';', ':', "'", '"', ',', '<', '.', '>',
    '/', '?'
]
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z'
]
password=[]
alpha=int(input("Enter no of letters u want: "))
sn=int(input("Enter no. of symbol u want: "))
for i in range(0,alpha):
    password.append(random.choice(letters))
for s in range(0,sn):
    password.append(random.choice(keyboard_symbols))
random.shuffle(password)
password=''.join(password)
print(password)