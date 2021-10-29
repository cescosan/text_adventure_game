# definitions for events
import random
from objects_ import *


def attack(x, y):
    def attack_amount():
        t = 0
        while t < 2:
            prob = random.randint(1, x.inventory["Main Weapon"].miss)
            if prob != 0:
                y.health -= (x.inventory["Main Weapon"].attack + random.randint(-x.inventory["Main "
                                                                                             "Weapon"].attack_range, x.inventory["Main Weapon"].attack_range))
            else:
                if x == player:
                    print('You missed.')
                else:
                    print(f'{x.name} missed.')
            t += x.inventory["Main Weapon"].recharge

    if x is player:
        print(f'You attack {y.name}!')
        attack_amount()
        if y.health > 0:
            print(f'{y.name}\'s health is now {y.health}.')
        else:
            y.health = 0
            print(f'{y.name}\'s health is now 0.')
    else:
        print(f'{x.name} attacks you!')
        attack_amount()
        if y.health > 0:
            print(f'Your health is now {y.health}.')
        else:
            y.health = 0
            print(f'Your health is now 0.')


def shop_event():
    shop_inventory = {x.name: x for x in Weapon.weapons}
    print('The shopkeeper says "Hello there traveller, and welcome to my humble shop!"\n\n')
    while True:
        print("Here are the available items:\n")
        for item_name, item in shop_inventory.items():
            print(item_name + ': ' + str(item.price))
        else:
            print('Your cash is ' + str(player.cash) + '.\n\n')
        choice = input('What would you like to buy?: ')
        if choice in shop_inventory:
            x = shop_inventory[choice]
            if x.price <= player.cash:
                player.inventory["Main Weapon"] = x
                player.cash -= x.price
                print("You bought a {0}. \n\nYou're cash is now {1}.\n\n\n".format(choice, player.cash))
                leave = input("Press ENTER to leave the shop. To stay, press any character(s): ")
                if leave == "":
                    break
                else:
                    print("\n")
                    continue
            else:
                print("You don't have enough cash for a {0}.".format(choice) + "\n")
                leave = input("Press ENTER to leave the shop. To stay, press any character(s): ")
                if leave == "":
                    break
                else:
                    print("\n")
                    continue
        else:
            print("The shop doesn't have a {0}.".format(choice) + "\n")
            leave = input("Press ENTER to leave the shop. To stay, press any character(s): ")
            if leave == "":
                break
            else:
                print("\n")
                continue


victory_message = f'\nYou have defeated {villain.name}. You return to the kingdom where you are greeted by the king. ' \
                  f'"Thank you {player.name}" the king says, "tales will be written about this day and your heroic acts ' \
                  f'for centuries".'

losing_message = f'\n{villain.name} has defeated you.\n\nG a m e   O v e r!'


def battle_event(hero, foe):
    while True:
        input('\nPress enter to attack: ')
        coin_flip = random.randint(0, 1)
        if coin_flip == 0:
            attack(hero, foe)
            if foe.health == 0:
                print(victory_message)
                break
            attack(foe, hero)
            if hero.health == 0:
                print(losing_message)
                break
        else:
            attack(foe, hero)
            if hero.health == 0:
                print(losing_message)
                break
            attack(hero, foe)
            if foe.health == 0:
                print(victory_message)
                break
