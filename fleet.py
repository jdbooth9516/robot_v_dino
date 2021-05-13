from robot import Robot


class Fleet:
    def __init__(self, ):
        self.robots = []
        self.r = Robot('C1', 'gun')
        self.r2 = Robot('C2', 'cannon')
        self.r3 = Robot('C3', 'laser')

    def create_fleet(self):
        self.robots.append(self.r)
        self.robots.append(self.r2)
        self.robots.append(self.r3)

