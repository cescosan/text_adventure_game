#definitions for events
import random
from objects_ import *


def attack(x,y):
    def attack_amount():
        t=0
        while t<2:
            prob=random.randint(1,x.item[0].miss)
            if prob != 0:
                y.health-=(x.item[0].attack+random.randint(-x.item[0].attack_range,x.item[0].attack_range))
            else:
                if x==player:
                    print('You missed.')
                else:
                    print(f'{x.name} missed.')
            t+=x.item[0].recharge



    if x is player:
        print(f'You attack {y.name}!')
        attack_amount()
        if y.health >0:
            print(f'{y.name}\'s health is now {y.health}.')
        else:
            y.health = 0
            print(f'{y.name}\'s health is now 0.')
    elif x is villain:
        print(f'{x.name} attacks you!')
        attack_amount()
        if y.health > 0:
            print(f'Your health is now {y.health}.')
        else:
            y.health = 0
            print(f'Your health is now 0.')


def shop_event():
    shop_inventory = {x.name:x for x in Weapon.weapons}
    print('The shopkeeper says "Hello there traveller, and welcome to my humble shop!"\n\n')
    while True:
        print("Here are the available items:\n")
        for item_name, item in shop_inventory.items():
            print(item_name+': '+str(item.price))
        else:
            print('Your cash is ' + str(player.cash) + '.\n\n')
        choice = input('What would you like to buy?: ')
        if choice in shop_inventory:
            x = shop_inventory[choice]
            if x.price <= player.cash:
                player.inventory.setdefault(choice,x)
                player.cash -= x.price
                print("You bought a {0}.".format(choice)+"\n")
                quit = input("Is that all?: ")
                if quit.upper() == "YES":
                    break
                else:
                    print("\n")
                    continue
            else:
                print("You don't have enough cash for a {0}.".format(choice)+"\n")
                quit = input("Is that all?: ")
                if quit.upper() == "YES":
                    break
                else:
                    print("\n")
                    continue
        else:
            print("The shop doesn't have a {0}.".format(choice)+"\n")
            quit = input("Is that all?: ")
            if quit.upper() == "YES":
                break
            else:
                print("\n")
                continue




  

    


