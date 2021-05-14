from battlefield import Battlefield
from fleet import Fleet
from herd import Herd
from robot import Robot
import time


class Main:
    def __init__(self):
        print()
        print()
        print("Welcome to Robots Vs Dinosaurs.")
        print()
        time.sleep(2)

        print("Here you will be given a fleet of robots.")
        print()
        time.sleep(2)

        print("Your robots will pick a random weapon and you will choose which robot attacks that turn.")
        print()
        time.sleep(2)

        print("Each attack consumes energy if your robot runs out of energy they won't be able to attack.")
        print()
        time.sleep(2)

        print("If you robots run out of health they die.")
        print()
        time.sleep(2)

        print("Eliminate all the dinosaurs to win.")
        print()
        time.sleep(2)

        print("Standy by initializing robots")
        print("10%")
        print()
        time.sleep(1)

        print("Standy by initializing robots")
        print("30%")
        print()
        time.sleep(1)

        print("Standy by initializing robots")
        print("60%")
        print()
        time.sleep(1)

        print("Complete")
        

        self.fleet = Fleet()
        self.herd = Herd()
        self.fleet.create_fleet()
        self.herd.create_herd()

        game = Battlefield(self.fleet, self.herd)
        game.display_welcome()


Main()