from battlefield import Battlefield
from fleet import Fleet
from herd import Herd




class Main:
    def __init__(self):
        self.fleet = Fleet(3)
        self.herd = Herd(3)

        Battlefield(self.fleet, self.herd)


Main()
