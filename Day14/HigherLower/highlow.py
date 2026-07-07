import random

data = [
    {"name": "Instagram", "followers": 600},
    {"name": "Cristiano Ronaldo", "followers": 630},
    {"name": "Virat Kohli", "followers": 270},
    {"name": "Selena Gomez", "followers": 430},
    {"name": "Lionel Messi", "followers": 500},
    {"name": "Taylor Swift", "followers": 320},
    {"name": "Kylie Jenner", "followers": 400},
    {"name": "Narendra Modi", "followers": 95},
    {"name": "Shah Rukh Khan", "followers": 47},
    {"name": "Priyanka Chopra", "followers": 92}
]


def get_random_account():
    """Return a random account from the data list."""
    return random.choice(data)


def format_account(account):
    """Return a formatted string for displaying account details."""
    return account["name"]


def check_answer(user_guess, a_followers, b_followers):
    """Return True if the user's guess is correct, otherwise False."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"


def play_game():
    """Run the Higher Lower game."""
    score = 0
    account_a = get_random_account()
    account_b = get_random_account()

    while account_a == account_b:
        account_b = get_random_account()

    while True:
        print("\nCompare A:", format_account(account_a))
        print("VS")
        print("Against B:", format_account(account_b))

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        a_followers = account_a["followers"]
        b_followers = account_b["followers"]

        if check_answer(guess, a_followers, b_followers):
            score += 1
            print(f"Correct! Current score: {score}")
            account_a = account_b
            account_b = get_random_account()

            while account_a == account_b:
                account_b = get_random_account()
        else:
            print(f"Wrong! Final score: {score}")
            print(f"{account_a['name']} has {a_followers} million followers.")
            print(f"{account_b['name']} has {b_followers} million followers.")
            break


play_game()