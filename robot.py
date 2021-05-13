from weapon import Weapon

class Robot:
    def __init__(self, name, weapon_name):
        self.name = name
        self.power_level = 100
        self.health = 10
        self.weapon = Weapon(weapon_name, 5)

    def attack(self, target):
        damage = target.health - self.weapon.attack_power
        target.health = damage
        print(f"{self.name} attack {target.type} for {self.weapon.attack_power}. {target.type} now has {target.health} health")



