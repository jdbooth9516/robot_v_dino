from weapon import Weapon
import random

class Robot:
    def __init__(self, name, weapon_name):
        self.name = name
        self.power_level = 100
        self.health = 10
        self.weapon = Weapon(weapon_name, 5)

    def attack(self, target):
        rand_num = random.randint(-2 , 5)
        total_attack = rand_num + self.weapon.attack_power
        damage = target.health - total_attack
        target.health = damage
        print(f"{self.name} attack {target.type} with{self.weapon} dealing {total_attack}. {target.type} now has {target.health} health")



