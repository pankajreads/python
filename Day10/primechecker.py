def isprime(num):
    for i in range(2,num//2):
        if num%i!=0:
            return "Prime"
    else:
        return "Not Prime"
num=int(input("Enter no to check: "))
print(isprime(num))