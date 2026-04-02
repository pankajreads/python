uppercase=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

lowercase= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encode(message,shift):
    encoded=[]
    for char in message:
        if char in uppercase:
            encoded.append(uppercase[(uppercase.index(char)+shift)%26])
        elif char in lowercase:
            encoded.append(lowercase[(lowercase.index(char)+shift)%26])
        else:
            encoded.append(char)
    return (''.join(encoded))
def decode(message,shift):
    decoded=[]
    for char in message:
        if char in uppercase:
            decoded.append(uppercase[(uppercase.index(char)-shift)%26])
        elif char in lowercase:
            decoded.append(lowercase[(lowercase.index(char)-shift)%26])
        else:
            decoded.append(char)
    return (''.join(decoded))
option=input('''Type encode of encoding
decode for decoding and
exit to exit ''')
while(option!="exit"):
    if option=="encode":
        message=input("Enter your message ")
        shift=int(input("Enter the shift no."))
        print(encode(message=message,shift=shift))
    elif option=="decode":
        message=input("Enter your message ")
        shift=int(input("Enter the shift no."))
        print(decode(message=message,shift=shift))
    else:
        print(" choose a valid option ")
    option=input('''Type encode of encoding
decode for decoding and
exit to exit ''')