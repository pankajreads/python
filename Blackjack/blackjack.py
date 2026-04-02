import random
will=input("Do you want to play Blackjack? Type 'Yes' or 'No' ").lower()
cards = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        10, 10, 10,   # J, Q, K
        11            # Ace
    ]*4
if will=="yes":
    your=[cards.pop(random.choice(cards)),cards.pop(random.choice(cards))]
    print("Your cards: ",your)
    cpu=[cards.pop(random.choice(cards)),cards.pop(random.choice(cards))]
    print(sum(cpu))
    hit=input("Do you Want to 'Hit' or 'Pass' ").lower()
    while (hit=="hit"):
        your.append(cards.pop(random.choice(cards)))
        print(your)
        if sum(your)>21:
            print( "YOU LOOSE")
            break
        hit=input("Do you Want to 'Hit' or 'Pass' ").lower()
    dealer=sum(cpu)
    if (hit=="pass"):
        while(dealer<16):
            if dealer==sum(your):
                print("Draw")
                break
            if dealer>sum(your):
                print("Dealer Win")
                break
            if dealer>21:
                print(cpu)
                print("You Win")
            cpu.append(cards.pop(random.choice(cards)))
            print(cpu)
            dealer=sum(cpu)
        else:
            print("you win")