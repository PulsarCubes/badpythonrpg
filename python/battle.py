import random as rand
import os
#move rng/drops to here, add seperate file for drop tables
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
            line = line.strip()
            if line:  # Check if the line is not empty
                if line.startswith("#"):  # Line indicates a new enemy
                    current_enemy = line[1:].strip()
                    if current_enemy == enemy:
                        drop_table = {}  # Initialize drop_table for the specified enemy
                else:
                    if current_enemy == enemy:  # Check if we are processing the correct enemy
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
    finaldmg=damage*critdmg-defender.dfn
    return finaldmg

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
                if dodge != 1:
                    if damage>0:
                        enemy.hp -= damage
                        if enemy.hp <= 0:
                            print('You defeated the enemy!')
                            enemydefeated(player,enemy)
                            break
                        
                        print(f'You hit for {damage}, enemy has {enemy.hp} remaining!')
                        enemydodgechance += 20
                    else:
                        print('Enemy blocked attack')
                else:
                    print('Enemy dodged your attack!')
                    enemydodgechance=0
            else:
                if damage>0:
                    enemy.hp -= damage
                    if enemy.hp <= 0:
                        print('You defeated the enemy!')
                        enemydefeated(player,enemy)
                        break
                    print(f'You hit for {damage}, enemy has {enemy.hp} remaining!')
                    enemydodgechance += 20
                else:
                    print('Enemy blocked attack')
        
            # Enemy's turn
            damage = damagecalc(5, enemydamage, player)
            if playerdodgechance > 0:
                dodge = rand.randint(1, int(100 / playerdodgechance))
                if dodge != 1:
                    if damage>0:
                        player.hp -= damage
                        if player.hp <= 0:
                            print('You were defeated by the enemy!')
                            break
                        print(f'You were hit for {damage}, you have {player.hp} remaining!')
                        playerdodgechance += 20
                    else:
                        print('You blocked attack')
                else:
                    print('Your dodge was successful!')
                    playerdodgechance=0
            else:
                if damage>0:
                    player.hp -= damage
                    if player.hp <= 0:
                        print('You were defeated by the enemy!')
                        break
                    print(f'You were hit for {damage}, you have {player.hp} remaining!')
                    playerdodgechance += 20
                else:
                    print('You blocked attack')
        else:
            # Enemy's turn
            damage = damagecalc(5, enemydamage, player)
            if playerdodgechance > 0:
                dodge = rand.randint(1, int(100 / playerdodgechance))
                if dodge != 1:
                    if damage>0:
                        player.hp -= damage
                        if player.hp <= 0:
                            print('You were defeated by the enemy!')
                            break
                        print(f'You were hit for {damage}, you have {player.hp} remaining!')
                        playerdodgechance += 20
                    else:
                        print('you blocked attack')
                else:
                    print('Your dodge was successful!')
                    playerdodgechance=0
            else:
                if damage>0:
                    player.hp -= damage
                    if player.hp <= 0:
                        print('You were defeated by the enemy!')
                        break
                    print(f'You were hit for {damage}, you have {player.hp} remaining!')
                    playerdodgechance += 20
                else:
                    print('you blocked attack')
            
            # Player's turn
            damage = damagecalc(5, playerdamage, enemy)
            if enemydodgechance > 0:
                dodge = rand.randint(1, int(100 / enemydodgechance))
                if dodge != 1:
                    if damage>0:
                        enemy.hp -= damage
                        if enemy.hp <= 0:
                            print('You defeated the enemy!')
                            enemydefeated(player,enemy)
                            break
                        print(f'You hit for {damage}, enemy has {enemy.hp} remaining!')
                        enemydodgechance += 20
                    else:
                        print('Enemy blocked attack')
                else:
                    print('Enemy dodged your attack!')
                    enemydodgechance=0
            else:
                if damage > 0:
                    enemy.hp -= damage
                    if enemy.hp <= 0:
                        print('You defeated the enemy!')
                        enemydefeated(player,enemy)
                        break
                    print(f'You hit for {damage}, enemy has {enemy.hp} remaining!')
                    enemydodgechance += 20
                else:
                    print('enemy blocked your attack!')
def enemydefeated(player,enemy):
    dt=parse_drop_tables('drop_tables.txt',enemy.name)
    rng(player,dt)
           
        

            