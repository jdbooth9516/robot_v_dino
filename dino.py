class Dinosaur:
    def __init__(self,type):
        self.type = type
        self.energy = 100
        self.attack_power = 5
        self.health = 20

    def attack(self, target):
        damage = self.attack_power
        
        