from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    decision = input(f"What would you like? ({menu.get_items()}): ").lower()
    
    if decision == 'report':
        coffee_machine.report()
        money_machine.report()
    elif decision == 'off':
        is_on = False
    else:
        order = menu.find_drink(decision)
        if coffee_machine.is_resource_sufficient(order):
            if money_machine.make_payment(order.cost):
                coffee_machine.make_coffee(order)