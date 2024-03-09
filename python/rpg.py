#text based rpg so if i complain about not having a python project i have this
#woaj its some imports
import random
import os
import rpgclasses as rpg
import battle

dropped = False
inventory = {}
#simplest class in existence because i need to learn
tutorialfinished=False

#functions
#this is for cleaning shit ykyk
def clear(): os.system('cls')
def invadd():
    pass
def printinv():
    print('in your inventory you have ')
    for key, value in inventory.items():
        print(f'{key}: {value}')
def rng(droptable):
    global dropped
    global inventory
    rarities=list(droptable.values())
    # list out keys and values separately
    key_list = list(droptable.keys())
    val_list = list(droptable.values())
    
    # print key with val 100
    
    
    for i in rarities:
        rngsim = random.randint(1,i)
        position = val_list.index(i)
        if rngsim == 1:
            print(f'you dropped {key_list[position]}')
            inventory[key_list[position]] = inventory.get(key_list[position], 0) + 1
            dropped = True
    if not dropped:
        print('you dropped nothing')
namechoice = input('Welcome, what would you like your name to be? ')
player = rpg.character(namechoice,random.randint(1,10),random.randint(1,10),random.randint(1,10),0)

clear()
print(f'Welcome to the world of Generic Text RPG Name Here, {namechoice}!')
while True:
    dialogtut = input('''To start, try using these keys to use the menu!
                      1 not this one
                      2 type this one
                      3 also not this one
                ''')
    if dialogtut == '1':
        print('nope')
    elif dialogtut == '2':
        print('Great job!')
        break
    elif dialogtut == '3':
        print('nope')


while tutorialfinished:
     
    action = input('''What would you like to do?
                      1 to view inventory
                      2 to view stats
                      3 to exit
                ''')
    if action == '1':
        if len(inventory<0):
            print('you have nothing')
        else:
            printinv()
    elif action == '2':
        print('your stats are: Strength: '+str(player.str) + ' Speed: ' + str(player.spd)+ ' Intelligence: ' + str(player.int)+ ' Defense: ' + str(player.dfn))
    elif action == '3':
        break
    else:
        print('invalid input')
input('enter to exit')

