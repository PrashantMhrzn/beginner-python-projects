from Utils.menu import Resto

items = {
    1: 3.50,
    2: 2.50,
    3: 4.00,
    4: 3.5,
    5: 1.75,
    6: 1.50,
    7: 2.25,
    8: 3.75,
    9: 1.25
}


def total(order):
    item = [int(n) for n in order]
    totals = 0
    for unit in item:
        totals += items.get(unit)
    return totals


cont = int(input("enter 0 for exit 1 for continue"))
while cont != 0:
    if cont == 1:
        print(Resto.MENU)
        order = input("enter your order: ")
        if len(order) <= 0:
            print("")
        print(f"your total bill is ${total(order)}")
    cont = int(input(f"enter 0 for exit 1 for continue"))
print("Thanks!!!")
