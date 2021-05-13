
from dino import Dinosaur
from robot import Robot


class Battlefield:
    def __init__(self, fleet, herd):
        self.fleet = fleet
        self.herd = herd
        self.turn = "robot"
        self.run = False
        self.winner = ''
        herd = self.herd.dinosaurs
        fleet = self.fleet.robots
    

    def display_welcome(self):
        start = input("Welcome your fleet is ready do you want to start the battle? (y/n): ")
        if start == 'y':
            self.run = True
            self.run_game()

    def show_dino_options(self):
        selection = int(input("Select which dinosaur is going to attack: (1, 2, or 3)")) - 1
        selected_attacker = self.herd.dinosaurs[selection]
        return selected_attacker

    def show_robo_options(self):
        selection = int(input("Select which Robot is going to attack: (1, 2, or 3)")) - 1
        selected_attacker = self.fleet.robots[selection]
        return selected_attacker

    def dino_turn(self):
        if self.turn == "dino":
            self.show_dino_options()

    def robo_turn(self):
        if self.turn == "robot":
            self.show_robo_options()

    def display_winners(self):
        if self.winner == "robot":
            print("The dinosaurs have been defeated. Robots win!!!")
        else:
            print("The dinosaurs have been defeated. Robots win!!!")


    def battle(self):
        if self.turn == 'robot':
            attacker = self.show_robo_options()
            attacker.attack(self.herd.dinosaurs[0])
            self.turn = "dino"
            print()
        else:     
            attacker= self.show_dino_options()
            attacker.attack(self.fleet.robots[0])
            self.turn = "robot"
            print()


    def check_for_death(self):
        if self.herd.dinosaurs[0].health <= 0:
            print(self.herd.dinosaurs[0].type + " Was defeated")
            del self.herd.dinosaurs[0]

        elif self.fleet.robots[0].health <= 0: 
            print(self.fleet.robots[0].name + " Was defeated")
            del self.fleet.robots[0]   


    def check_for_win(self):
        if len(self.herd.dinosaurs) == 0:
            self.winner = 'robot'
            self.run = False
            
        elif len(self.fleet.robots) == 0:
            self.winner = 'dino'
            self.run = False

    def run_game(self):
        while self.run == True:
            self.battle()
            self.check_for_death()
            self.check_for_win()
            if self.winner != "":
                self.display_winners()




