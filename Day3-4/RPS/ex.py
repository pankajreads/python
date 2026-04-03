import random
choices = ['rock', 'paper', 'scissors']
computer = random.choice(choices)
user =(input("Enter your choice among rock, paper and scissors: "))
if user not in choices:
    print("Invalid choice. Please choose rock, paper, or scissors.")
elif user == computer:
    print(f"Both chose {user}. It's a tie!")
elif (user == 'rock' and computer == 'scissors') or \
     (user == 'paper' and computer == 'rock') or \
     (user == 'scissors' and computer == 'paper'):
    print(f"You chose {user}, computer chose {computer}. You win!")
else:
    print(f"You chose {user}, computer chose {computer}. Computer wins!")