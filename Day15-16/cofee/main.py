from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffeeMaker=CoffeeMaker()
menu=Menu()
money=MoneyMachine()

is_on=True
while is_on:
    option=menu.get_items()
    choice=input(f"What you want to have {option} ").lower()
    if choice=="off":
        is_on=False
    elif choice=="creport":
        coffeeMaker.report()
    elif choice=="mreport":
        money.report()
    else :
        item=menu.find_drink(choice)
        if item!=None:
            if coffeeMaker.is_resource_sufficient(item):
                print(f"Your Coffee cost {item.cost}")
                if money.make_payment(item.cost):
                    coffeeMaker.make_coffee(item)