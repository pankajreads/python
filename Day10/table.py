from prettytable import PrettyTable as pt
table=pt()
table.add_column("Serial No.",[i for i in range(1,9)])
table.add_column("Subject",["oops","maths","DS","CA","DE","IC","STRW","TRAINING"])
table.add_column("Marks",[65,104,101,67,89,40,42,72])
print(table)