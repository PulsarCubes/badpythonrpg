import random as rand
import os
from time import sleep
#drop tables are in form item:dropchance in form 1/x
def parse_drop_tables(file_name, enemy):
    file_path = os.path.join(os.getcwd(), file_name)
    drop_table = {}

    if not os.path.exists(file_path):
        print(f"Error: File '{file_name}' not found at '{os.getcwd()}'")
        return drop_table

    with open(file_path, 'r') as file:
        current_enemy = None
        for line in file:
            if line := line.strip():
                if line.startswith("#"):  # Line indicates a new enemy
                    current_enemy = line[1:].strip()
                    if current_enemy == enemy:
                        drop_table = {}  # Initialize drop_table for the specified enemy
                elif current_enemy == enemy:  # Check if we are processing the correct enemy
                    item, drop_chance = line.split(':')
                    drop_table[item.strip()] = drop_chance  # Add item and drop chance to drop_table

    return drop_table
def rng(character, droptable):
    global dropped
    rarities = list(droptable.values())
    key_list = list(droptable.keys())
    val_list = list(droptable.values())

    dropped = False
    
    for i in rarities:
        rngsim = rand.randint(1, int(i))
        position = val_list.index(i)
        if rngsim == 1:
            print(f'You dropped {key_list[position]}')
            character.add_to_inventory(key_list[position])
            dropped = True
    if not dropped:
        print('You dropped nothing')
        
def damagecalc(cc,damage,defender):
    critdmg=1
    crit=rand.randint(1,(100/cc))
    if crit==20:
        critdmg=1.5 
        print('Crit!')
    return damage*critdmg-defender.dfn

def battle(player, enemy):
    playerdamage = player.heldweapon.dmg + player.str
    playerspeed = player.heldweapon.attackspeed + player.spd
    playerdodgechance = 0
    enemydamage = enemy.heldweapon.dmg + enemy.str
    enemyspeed = enemy.heldweapon.attackspeed + enemy.spd
    enemydodgechance = 0

    while player.hp > 0 and enemy.hp > 0:
        # Determine who attacks first based on speed

        if playerspeed >= enemyspeed:
            # Player's turn
            damage = damagecalc(5, playerdamage, enemy)
            if enemydodgechance > 0:
                dodge = rand.randint(1, int(100 / enemydodgechance))
                if dodge == 1:
                    print('Enemy dodged your attack!')
                    enemydodgechance=0
                elif damage>0:
                    enemy.hp -= damage
                    if enemy.hp <= 0:
                        print('You defeated the enemy!')
                        enemydefeated(player,enemy)
                        break

                    print(f'You hit for {damage} damage, enemy has {enemy.hp} health remaining!')
                    enemydodgechance += 20
                else:
                    print('Enemy blocked your attack!')
            else:
                if damage>0:
                    enemy.hp -= damage
                    if enemy.hp <= 0:
                        print('You defeated the enemy!')
                        enemydefeated(player,enemy)
                        break
                    print(f'You hit for {damage} damage, enemy has {enemy.hp} health remaining!')
                    enemydodgechance += 20
                else:
                    print('Enemy blocked your attack!')
            sleep(1)
            # Enemy's turn
            damage = damagecalc(5, enemydamage, player)
            if playerdodgechance > 0:
                dodge = rand.randint(1, int(100 / playerdodgechance))
                if dodge == 1:
                    print('Your dodge was successful!')
                    playerdodgechance=0
                elif damage>0:
                    player.hp -= damage
                    if player.hp <= 0:
                        print('You were defeated by the enemy!')
                        break
                    print(f'You were hit for {damage} damage, you have {player.hp} health remaining!')
                    playerdodgechance += 20
                else:
                    print('You blocked enemy\'s attack!')
            else:
                if damage>0:
                    player.hp -= damage
                    if player.hp <= 0:
                        print('You were defeated by the enemy!')
                        break
                    print(f'You were hit for {damage} damage, you have {player.hp} health remaining!')
                    playerdodgechance += 20
                else:
                    print('You blocked enemy\'s attack!')
            sleep(1)
        else:
            # Enemy's turn
            damage = damagecalc(5, enemydamage, player)
            if playerdodgechance > 0:
                dodge = rand.randint(1, int(100 / playerdodgechance))
                if dodge == 1:
                    print('Your dodge was successful!')
                    playerdodgechance=0
                elif damage>0:
                    player.hp -= damage
                    if player.hp <= 0:
                        print('You were defeated by the enemy!')
                        break
                    print(f'You were hit for {damage} damage, you have {player.hp} health remaining!')
                    playerdodgechance += 20
                else:
                    print('You blocked enemy\'s attack!')
            else:
                if damage>0:
                    player.hp -= damage
                    if player.hp <= 0:
                        print('You were defeated by the enemy!')
                        break
                    print(f'You were hit for {damage} damage, you have {player.hp} health remaining!')
                    playerdodgechance += 20
                else:
                    print('You blocked enemy\'s attack!')
            sleep(1)
            # Player's turn
            damage = damagecalc(5, playerdamage, enemy)
            if enemydodgechance > 0:
                dodge = rand.randint(1, int(100 / enemydodgechance))
                if dodge == 1:
                    print('Enemy dodged your attack!')
                    enemydodgechance=0
                elif damage>0:
                    enemy.hp -= damage
                    if enemy.hp <= 0:
                        print('You defeated the enemy!')
                        enemydefeated(player,enemy)
                        break
                    print(f'You hit for {damage} damage, enemy has {enemy.hp} health remaining!')
                    enemydodgechance += 20
                else:
                    print('Enemy blocked your attack!')
            else:
                if damage > 0:
                    enemy.hp -= damage
                    if enemy.hp <= 0:
                        print('You defeated the enemy!')
                        enemydefeated(player,enemy)
                        break
                    print(f'You hit for {damage} damage, enemy has {enemy.hp} health remaining!')
                    enemydodgechance += 20
                else:
                    print('Enemy blocked your attack!')
            sleep(1)
def enemydefeated(player,enemy):
    dt=parse_drop_tables('drop_tables.txt',enemy.name)
    rng(player,dt)
           
        

            