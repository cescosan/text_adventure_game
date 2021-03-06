#classes and objects for the game
from random import randint

class Character:

    characters = []

    def character_stats(stats_tup=tuple):#returns a dictionary containing stats for the character
        stats = {"Strength":stats_tup[0],"Speed":stats_tup[1],"Armour":stats_tup[2]}
        return stats

    def __init__(self,name,stats_tup,health = 100,inventory = {"Main Weapon":None,},class_list = characters,funcs = character_stats):
        self.name = name
        self.stats = funcs(stats_tup)
        self.health = health
        self.inventory = inventory
        class_list.append(self)


class Player(Character):
    cash = 100


class Weapon:
    
    weapons = []
    
    def __init__(self, name, price, attack, recharge, attack_range, miss, class_list=weapons):
        self.name = name
        self.price = price
        self.attack = attack
        self.recharge = recharge
        self.attack_range = attack_range
        self.miss = miss
        class_list.append(self)


class Armour:

    armours = []

    def __init__(self, name, protection, class_list=armours):
        self.name = name
        self.protection = protection
        class_list.append(self)

    # todo: need to add a method to update update armour stat of character when it receives armour




sword = Weapon('Sword', 25, 100, 2, 10, 5)

stick = Weapon('Stick', 15, 10, 1, 10, 3)

spear = Weapon('Spear', 50, 75, 2, 0, 2)

player=Player(input('Please enter a name: '), (randint(1, 5), randint(1, 5), 0))

villain=Character("Mortimus", (6, 3, 9))

