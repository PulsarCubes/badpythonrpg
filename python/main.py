#text based rpg so if i complain about not having a python project i have this
#woaj its some imports
import random
import os
import rpgclasses as rpg
from battle import *
from itemsandenemies import *
dropped = False
inventory = {}
tutorialstarted=False
tutorialfinished=False
dotutorial=''
remainingpoints=15
#this is for cleaning shit ykyk
def clear(): os.system('cls')
def printinv():
    print('In your inventory you have ')
    for key, value in player.inventory.items():
        print(f'{key}: {value}')



namechoice = input('Welcome, what would you like your name to be? ')
player = rpg.character(namechoice,random.randint(4,10),random.randint(5,10),random.randint(6,10),10,hands)


print(f'Welcome to the world of Generic Text RPG Name Here, {namechoice}!\n')
while dotutorial not in ['y', 'n']:
    dotutorial=input('Do you need a tutorial? y/n \n')
if dotutorial == 'n':
    tutorialfinished=True
    tutorialstarted=True
elif dotutorial == 'y':
    while not tutorialstarted:
        dialogtut = input('''To start, try using these keys to use the menu!
                          
                        1 Not this one!
                        2 Type this one!
                        3 Also not this one!
                    ''')
        if dialogtut in ['1', '3']:
            print('Nope!')
        elif dialogtut == '2':
            print('Great job! :D')
            break
    statetutorial=input(f'''Your player has stats that determine how well they can fight
For instance, some example stats for your character are: Strength: {str(player.str)}, Speed: {str(player.spd)}, and Defense: {str(player.dfn)}\n

Hit enter to proceed to the battle tutorial section
    ''')
    clear()

    battleready=input('''Now you can see how a fight works,
every turn you and the enemy both have a chance to hit first based on your speed.
there is a chance to dodge every attack, and a chance for every attack to critically hit.
This proceeds sequentially with both sides getting turns affected by your defense and attack.
This fight will use your example stats from the last section

Hit enter to proceed to the fight''')
    clear()

    battle(player,tutenemy)
    endtut = input('''Congrats! Now you're ready to move on to the real world!
                
Hit enter whenever you're ready to move on!''')
    clear()
    tutorialfinished=True
player = rpg.character(namechoice,0,0,0,10,hands)
while remainingpoints != 0:
    clear()
    specpoints=input(f'''You have {remainingpoints} left to put into 
1: Strength
2: Speed
3: Defense
Type the number in front of the skill you want to spec your points into! \n''')
    if specpoints=='1' and player.str<10:
        player.str+=1
        remainingpoints-=1
    elif specpoints == '2' and player.spd<10:
        player.spd+=1
        remainingpoints-=1
    elif specpoints=='3' and player.dfn<10:
        player.dfn+=1
        remainingpoints-=1
    else:
        print('invalid input or stat can\'t go above 10\n')
        continue
inventory = {}
while tutorialfinished:

    action = input('''What would you like to do?
                   
                      1 to view inventory
                      2 to view stats
                      3 to exit
                ''')
    if action == '1':
        if len(player.inventory)==0:
            print('You have nothing in your inventory!')
        else:
            printinv()
    elif action == '2':
        print(f'Your stats are: Strength: {+str(player.str)} Speed: {+str(player.spd)} Defense: {+str(player.dfn)}')
    elif action == '3':
        break
    else:
        print('Invalid input')
input('Enter to exit')

