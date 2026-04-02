print("Welcome to the secret auction Program.")
ds={}
def newbidder():
    ds[int(input("What's your bid? : $"))]=input("What is your Name?: ")
newbidder()
option=input("Are ther any other bidders? Type 'yes' or 'no' ."  )
while option=="yes":
    print("\n"*20)
    newbidder()
    option=input("Are ther any other bidders? Type 'yes' or 'no' ."  )
Winner=max(list(ds.keys()))
print(ds[Winner],f"is the winner of this auction with ${Winner}")