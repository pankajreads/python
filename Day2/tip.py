bill=input("Enter the total bill amount: ")
tip_percent=input("Enter the tip percentage you would like to give: ")
tip_amount=(tip_percent/100)*bill
total_bill=bill+tip_amount
split=input("Enter the number of people to split the bill: ")
bill_per_person=total_bill/split
print("Each person should pay: " + str(bill_per_person))