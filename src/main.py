from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    scelta = input(f"What would you like? ({menu.get_items()}): ").lower()

    if scelta == "off":
        break  # Il programma termina la propria esecuzione.
    elif scelta == "report":
        coffee_maker.report()  # Stampa lo stato attuale delle risorse della macchina del caffè.
        money_machine.report()  # Stampa lo stato attuale del denaro.
    elif scelta == "help":
        print(f"off, report, {menu.get_items()}")  # Stampa tutti i comandi possibili per aiutare l'utente.

    elif menu.find_drink(scelta):
        drink = menu.find_drink(scelta)  # drink contiene l'oggetto MenuItem
        if coffee_maker.is_resource_sufficient(drink):  # Verifica che le risorse siano sufficienti per il drink.
            if money_machine.make_payment(drink.cost):  # Consente di inserire il denaro e verifica che sia sufficiente.
                coffee_maker.make_coffee(drink)  # Prepara il drink e scala le risorse.
