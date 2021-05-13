from robot import Robot

class Fleet:
    def __init__(self, num):
        self.robots = []
        self.num = num
        

    def create_fleet(self):
        for i in range(self.num):
            self.robots.append(Robot())

