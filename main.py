from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

on = True
while on:
    answer = input(f"What would you like? {menu.get_items()}? ").lower()
    if answer == "off":
        on = False
    elif answer == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(answer)
        if drink != None:
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
