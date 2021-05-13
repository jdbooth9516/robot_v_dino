
from robot import Robot


class Battlefield:
    def __init__(self, fleet, herd):
        self.fleet = fleet
        self.herd = herd
        self.turn = "robot"
        self.run = False
        herd = self.herd.dinosaurs
        fleet = self.fleet.robots
    
        print(herd)

    def display_welcome(self):
        start = input("Welcome your fleet is ready do you want to start the battle? (y/n): ")
        if start == 'y':
            self.run = True
            self.battle()

    def show_dino_options(self):
        selection = int(input("Select which enemy to attack: (1, 2, or 3)")) - 1
        selected_target = self.fleet.robots[selection]
        return selected_target

    def show_robo_options(self):
        selection = int(input("Select which enemy to attack: (1, 2, or 3)")) - 1
        selected_target = self.herd.dinosaurs[selection]
        return selected_target

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

        while self.run == True:

            if self.turn == 'robot':
                target = self.show_robo_options()
                print(target)
                self.fleet.robots[0].attack(target)
                self.turn = "dino"
            else:     
                target = self.show_dino_options()
                print(target)
                self.herd.dinosaurs[0].attack(target)
                self.turn = "robot"
                self.run = False

    def run_game(self):
        self.display_welcome()

