from battlefield import Battlefield
from fleet import Fleet
from herd import Herd


class Main:
    def __init__(self):
        self.fleet = Fleet(1)
        self.herd = Herd(1)

        self.fleet.create_fleet()
        self.herd.create_herd()
        game = Battlefield(self.fleet, self.herd)
        game.run_game()


Main()
