import random
import time 

class Dinosaur:
    def __init__(self, name_type):
        self.type = name_type
        self.energy = 100
        self.attack_power = 1
        self.health = 35
        self.tail = ('tail', 3)
        self.claw = ('claw', 4)
        self.bite = ('bite', 5)

    def attack(self, target):
        if self.energy > 0:
            attack_list = [self.tail, self.claw, self.bite]
            rand_num = random.randint(-2 , 5)
            rand_choice =random.choice(attack_list)
            total_attack = rand_num + self.attack_power + rand_choice[1]
            damage = target.health - total_attack
            target.health = damage
            self.energy -= 10 
            print()
            print()
            print()
            print(f"{self.type} attacks {target.name} with {rand_choice[0]} for {total_attack} in damage. {target.name} now has {target.health} health")
            time.sleep(1.5)
            print()
            print(f"{self.type} lost 10 energy {self.energy} left")
            print()
            print()
            print('-----------------------------------------------')
            time.sleep(1.5)
        else: 
            print()
            print(f'{self.type} enegry is to low can not attack')
            print()
            print()
            print('-----------------------------------------------')
            time.sleep(1.5)
            