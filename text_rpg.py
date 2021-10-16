import random
from events_ import *
from objects_ import *

def villain_choice():
    n=random.choice((spear,sword,stick))
    villain.inventory.setdefault(n.name,n)

print(f'\nYou are in your house when a messenger knocks at the door. You answer and he hands you a letter and says '
      f'"this is from the king". It says:\n"The evil lord {villain.name} is wreaking havoc and must be stopped. Go to '
      f'the shop and buy what you need and then go to his lair and face him".\n\nYou go to the shop.')
shop_event()
villain_choice()
print('\nYou go and face {0}. You see that he has a {1}.'.format(villain.name,villain.inventory["Main Weapon"])) #don't
# think this right
victory_message=f'\nYou have defeated {villain.name}. You return to the kingdom where you are greeted by the king. ' \
                f'"Thank you {player.name}" the king says, "tales will be written about this day and your heroic acts ' \
                f'for centuries".'
losory_message=f'\n{villain.name} has defeated you.'
while True: #todo: put this into function called "battle"
    input('\nPress enter to attack: ')
    coin_flip=random.randint(0,1)
    if coin_flip == 0:
        attack(player,villain)
        if villain.health == 0:
            print(victory_message)
            break
        attack(villain,player)
        if player.health == 0:
            print(losory_message)
            break
    else:
        attack(villain,player)
        if player.health == 0:
            print(losory_message)
            break
        attack(player,villain)
        if villain.health == 0:
            print(victory_message)
            break