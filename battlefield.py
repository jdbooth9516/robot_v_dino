from weapon import Weapon
from fleet import Fleet
from herd import Herd


class Battlefield:
    def __init__(self, fleet, herd):
        self.fleet = fleet
        self.herd = herd
        
        


    def display_welcome():
        start = print("Welcome your fleet is ready do you want to start the battle? (y/n): ")
        if start == 'y':
            return True
        
    def run_game(self):
        if display_welcome() == True:
            run = True 

    display_welcome()
