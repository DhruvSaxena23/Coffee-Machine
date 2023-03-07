from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

Coffee_machine = True
while Coffee_machine:
    items = Menu().get_items()
    choice = input(f"What would you like? ({items}):").lower()
    order = Menu().find_drink(choice)
    if choice == "report":
        print(CoffeeMaker().report())
        print(MoneyMachine().report())
    elif choice == "off":
        Coffee_machine = False
    else:
        if CoffeeMaker().is_resource_sufficient(order):
            if MoneyMachine().make_payment(order.cost):
                CoffeeMaker().make_coffee(order)