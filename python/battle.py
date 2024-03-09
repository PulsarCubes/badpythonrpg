import random as rand

def battle(player,enemy):
    playerdamage = player.heldweapon.dmg+player.str
    playerspeed = player.heldweapon.attackspeed+player.spd
    playerdodgechance=0
    enemydamage = enemy.heldweapon.dmg+enemy.str
    enemyspeed = enemy.heldweapon.attackspeed+enemy.spd
    enemydodgechance=0
    playerfirst= False
    
    critdmg=1
    if playerspeed>=enemyspeed:
        print('You hit first!')
        damage=damagecalc(5,playerdamage,enemy)
        enemy.hp-=damage
        print(f'You hit for {damage}')
        enemydodgechance+=20
        playerfirst=True
    else:
        print('Enemy hit first!')
        damage=damagecalc(5,enemydamage,player)
        player.hp-=damage
        print(f'You were hit for {damage}')
        playerdodgechance+=20
    while player.hp>0 and enemy.hp>0:
        if playerfirst:
            dodge=rand.randint(1,100/enemydodgechance)
            if dodge!=1:
                damage=damagecalc(5,playerdamage,enemy)
                enemy.hp-=damage
                print(f'You hit for {damage}')
                enemydodgechance+=20
            else:
                print('You missed')
            playerfirst=False
        dodge=rand.randint(1,100/playerdodgechance)
        if dodge!=1:
            damage=damagecalc(5,enemydamage,player)
            player.hp-=damage
            print(f'You were hit for {damage}')
            playerdodgechance+=20
        else:
            print('Enemy missed')
        playerfirst=True
    else:
        if player.hp<=0:
            print('You died!')
            #TODO add logic here for recovering
        else:
            print('You won!')
            #TODO add logic here for enemy drops
        
def damagecalc(cc,damage,defender):
    critdmg=1
    crit=rand.randint(1,(100/cc))
    if crit==20:
        critdmg=1.5
    finaldmg=damage*critdmg-defender.dfn
    return finaldmg
            