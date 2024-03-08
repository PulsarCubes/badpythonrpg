class item:
    def __init__(self,name,equipable=False):
        self.equipable=equipable
class character:
    def __init__(self,name,str,spd,dfn,hp,heldweapon):
        self.name = name
        self.str = str
        self.spd = spd
        self.dfn = dfn
        self.hp = hp
    def attack(self,attacker):
        damage = self.myweapon.dmg+self.str
        attackspeed=self.spd+self.myweapon.atkspd
        if attackspeed>attacker.attackspeed:
            pass
        else:
            pass
class weapon(item):
    def __init__(self,name,dmg,atkspd) -> None:
        super().__init__(name,equipable=True)
        self.name=name
        self.dmg = dmg
        self.atkspd = atkspd
class enemy:
    def __init__(self,heldweapon,spd,dfn,str) -> None:
        self.str = str
        self.spd = spd
        self.dfn = dfn
        self.heldweapon = heldweapon
    