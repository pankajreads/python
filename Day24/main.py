with open("name.txt") as file:
    name=file.read().split("\n")
    print(name)
with open("example.txt") as demo:
    dem=demo.read()
    
for n in name:
    letter=dem.replace("name",n)
    print(letter)
    with open(f"./send/letter_{n}.txt","w+") as r_letter:
        r_letter.write(letter)