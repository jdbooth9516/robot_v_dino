from weapon import Weapon
import random

class Robot:
    def __init__(self, name):
        self.name = name
        self.power_level = 100
        self.health = 30
        self.weapon_name = ''
        self.weapon_att = 0
        self.weapon = Weapon(self.weapon_name, self.weapon_att)

    def attack(self, target):
        rand_num = random.randint(0 , 5)
        total_attack = rand_num + self.weapon_att
        damage = target.health - total_attack
        target.health = damage
        self.power_level -= 10

        print(f"{self.name} attacks {target.type} with {self.weapon_name} dealing {total_attack} damage. {target.type} now has {target.health} health. ")
        print()
        print(f"{self.name} lost 10 energy {self.power_level} left")


    def choose_weapon(self):
  
        weapon_name = random.randint(1,3)

        if weapon_name == 1:
            self.weapon_name = "Hand Cannon"
            self.weapon_att = 6
            print(f'{self.name} picked the {self.weapon_name}')
         
        elif weapon_name == 2:
            self.weapon_name = "Laser Rifle"
            self.weapon_att = 7
            print(f'{self.name} picked the {self.weapon_name}')
           
        elif weapon_name == 3:
            self.weapon_name = "Micro Rockets"
            self.weapon_att = 8
            print(f'{self.name} picked the {self.weapon_name}')
            
            

