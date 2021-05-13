from robot import Robot


class Fleet:
    def __init__(self, num):
        self.robots = []
        self.num = num
        self.r = Robot('C1', 'gun')

    def create_fleet(self):
        for i in range(self.num):
            self.robots.append(self.r)

