import random

class Dinosaur:
    def __init__(self, name_type):
        self.type = name_type
        self.energy = 100
        self.attack_power = 5
        self.health = 20

    def attack(self, target):
        rand_num = random.randint(-2 , 5)
        total_attack = rand_num + self.weapon.attack_power
        damage = target.health - total_attack
        print(f"{self.type} attack {target.name} for {self.attack_power}. {target.name} now has {target.health} health")
