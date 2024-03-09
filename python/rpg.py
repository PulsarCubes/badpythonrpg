#text based rpg so if i complain about not having a python project i have this
#woaj its some imports
import random
import os
import rpgclasses as rpg
import battle

#TODO make a new file full of weapons and enemy types

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
    for key, value in player.inventory.items():
        print(f'{key}: {value}')
        
hands=rpg.weapon('fists',1,1)

namechoice = input('Welcome, what would you like your name to be? ')
player = rpg.character(namechoice,random.randint(1,10),random.randint(1,10),random.randint(1,10),10,hands)

#clear()

testenemy=rpg.enemy(hands,1,1,1,10,'testenemy')
battle.battle(player,testenemy)


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
        tutorialfinished=True
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
        if len(player.inventory)==0:
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

