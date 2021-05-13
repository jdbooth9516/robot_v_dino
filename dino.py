class Dinosaur:
    def __init__(self, name_type):
        self.type = name_type
        self.energy = 100
        self.attack_power = 5
        self.health = 20

    def attack(self, target):
        damage = self.attack_power
        target.health = damage
        print(f"{self.name} attack {target.type} for {self.weapon.attack_power}. {target.type} now has {target.health} health")
