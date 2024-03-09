class item:
    def __init__(self,name,equipable=False):
        self.equipable=equipable
class weapon(item):
    def __init__(self,name,dmg,attackspeed) -> None:
        super().__init__(name,equipable=True)
        self.name=name
        self.dmg = dmg
        self.attackspeed = attackspeed
class character:
    def __init__(self,name,str,spd,dfn,hp,heldweapon):
        self.name = name
        self.str = str
        self.spd = spd
        self.dfn = dfn
        self.hp = hp
        self.heldweapon=heldweapon
        self.inventory = {}

    def add_to_inventory(self, item, quantity=1):
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity
    def equip_item(self, item):
        if item.equipable:
            self.heldweapon = item
            print(f"{self.name} has equipped {item.name}")
        else:
            print(f"{item.name} cannot be equipped.")

class enemy:
    def __init__(self,heldweapon,spd,dfn,str,hp,name) -> None:
        self.str = str
        self.spd = spd
        self.dfn = dfn
        self.hp = hp
        self.heldweapon = heldweapon
        self.name=name
    