from robot import Robot


class Fleet:
    def __init__(self, ):
        self.robots = []
        self.r = Robot('C1' )
        self.r2 = Robot('C2')
        self.r3 = Robot('C3')
        self.r.choose_weapon()
        self.r2.choose_weapon()
        self.r2.choose_weapon()

    def create_fleet(self):
        self.robots.append(self.r)
        self.robots.append(self.r2)
        self.robots.append(self.r3)

