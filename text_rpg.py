import random
from events_ import *
from objects_ import *

def villain_choice():
    n=random.choice((spear,sword,stick))
    villain.inventory.setdefault(n.name,n)

print(f'\nYou are in your house when a messenger knocks at the door. You answer and he hands you a letter and says '
      f''"this is from the king. It says:\nThe evil lord {villain.name} is wreaking havoc and must be stopped. Go to "
      "the shop and buy what you need and then go to his lair and face him.\n\nYou go to the shop.")
shop_event()
villain_choice()
print('\nYou go and face {0}. You see that he has a {1}.'.format(villain.name,villain.inventory["Main Weapon"].name))
#don't
# think this right

battle_event(player, villain)
