import random


def get_attempts(level):
    """Return the number of attempts based on difficulty level."""
    if level == 1:
        return 10   # Easy
    elif level == 2:
        return 7    # Medium
    elif level == 3:
        return 5    # Hard
    else:
        return 0


def play_game():
    """Run the number guessing game with difficulty levels."""
    print("\nWelcome to the Number Guessing Game!")
    print("Choose Difficulty Level:")
    print("1. Easy   (10 attempts)")
    print("2. Medium (7 attempts)")
    print("3. Hard   (5 attempts)")

    level = int(input("Enter your choice (1/2/3): "))
    attempts = get_attempts(level)

    if attempts == 0:
        print("Invalid difficulty level!")
        return

    secret_number = random.randint(1, 100)
    print("\nI have chosen a number between 1 and 100.")

    while attempts > 0:
        try:
            guess = int(input(f"Enter your guess ({attempts} attempts left): "))

            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print("Congratulations! You guessed the number correctly.")
                return

            attempts -= 1

        except ValueError:
            print("Invalid input! Please enter a number.")

    print("You have used all your attempts.")
    print("The correct number was:", secret_number)


def main():
    """Control the game and allow replay."""
    while True:
        play_game()
        again = input("\nDo you want to play again? (yes/no): ").lower()

        if again != "yes":
            print("Thanks for playing, have a nice day ")
            break


main()