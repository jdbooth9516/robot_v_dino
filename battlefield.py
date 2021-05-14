from dino import Dinosaur
from robot import Robot
import time


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
            print("Good luck")
            print()


    def show_dino_options(self):
        print("Waiting for Dinosaur to attack")
        print()


    def show_robo_options(self):
        valid_for_show_robo = False
        while valid_for_show_robo == False:
            length = len(self.fleet.robots)
            if length == 3:
                print()
                selection = int(input("Select which Robot is going to attack: (1, 2, or 3) : ")) - 1

                if selection != 0 and selection != 1 and selection != 2:
                    print("Invalid input please try again")
                    print()
                else:
                    selected_attacker = self.fleet.robots[selection]
                    valid_for_show_robo = True
                    return selected_attacker

            elif length == 2:
                print()
                selection = int(input("Select which Robot is going to attack: (1 or 2 ) : ")) - 1
                print()

                if selection != 0 and selection != 1:
                    print("Invalid input please try again")
                    print()
                else:
                    selected_attacker = self.fleet.robots[selection]
                    valid_for_show_robo = True
                    return selected_attacker

            elif length == 1:
                time.sleep(2)
                selected_attacker = self.fleet.robots[0]
                valid_for_show_robo = True
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
            print("The Robots have been defeated. dinosaurs win!!!")


    def battle(self):
        if self.turn == 'robot':
            attacker = self.show_robo_options()
            attacker.attack(self.herd.dinosaurs[0])
            self.turn = "dino"
            print()
        else:     
            self.show_dino_options()
            self.herd.dinosaurs[0].attack(self.fleet.robots[0])
            self.turn = "robot"
            print()


    def check_for_death(self):
        if self.herd.dinosaurs[0].health <= 0:
            print(self.herd.dinosaurs[0].type + " Was defeated")
            print()
            del self.herd.dinosaurs[0]

        elif self.fleet.robots[0].health <= 0 : 
            print(self.fleet.robots[0].name + " Was defeated")
            print()
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




