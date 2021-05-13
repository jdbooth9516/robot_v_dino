class Robot: 
    def __init__(self, name, weapon):
        self.name = name
        self.power_level = 100
        self.health = 10
        self.weapon = weapon

    def attack(self, target):
        damage = self.weapon.attack_power
        

