from Garlic_bread import Garlic_bread
from Money import Money
from Pastry import Pastry
from Pizza import Pizza

money=Money()
order='yes'
try:
    order=input("Hi! To order click 'yes'. To cancel press 'off'.")
    error=0
except TypeError:
    print("Error! The key you selected does not exist")
    error=1
while error==1 or (order!='yes' and order!='off'):
    try:
        order = input("Error! To order click yes. To cancel press off.")
    except TypeError:
        print("Error! The key you selected does not exist")
if order=='off':
    print("Good bye 🙋")
while order=='yes':
    newPastry=Pastry()
    newPastry.choosePastryName()
    newPastry.chooseFlourType()
    if newPastry.name=='pizza':
        newPizza = Pizza()
        newPizza.chooseSize()
        newPizza.addExtras()
        cost=newPizza.cost
    else:
        newGarlicBread=Garlic_bread()
        newGarlicBread.chooseShape()
        newGarlicBread.ask_for_sauce()
        cost=newGarlicBread.cost
    print(f"You have to pay {cost} shekels.")
    money.payment(cost)
    try:
        order = input("To order another pastry click 'yes'. To cancel press 'off'. To see the report press 'report'.")
        error=0
    except TypeError:
        print("Error! The key you selected does not exist")
        error=1
    while error==1 or (order != 'yes' and order != 'off' and order!='report'):
        try:
            order = input("To order click 'yes'. To cancel press 'off'. To see the report press 'report'.")
            error=0
        except TypeError:
            print("Error! The key you selected does not exist")
            error=1
    if order == 'off':
        print("Good bye 🙋")
    else:
        if order=='report':
             money.report()