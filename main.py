from battlefield import Battlefield
from fleet import Fleet
from herd import Herd
from robot import Robot


class Main:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        self.fleet.create_fleet()
        self.herd.create_herd()
        game = Battlefield(self.fleet, self.herd)
        game.display_welcome()


Main()
