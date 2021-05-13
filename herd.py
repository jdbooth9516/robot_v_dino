from dino import Dinosaur


class Herd:
    def __init__(self, ):
        self.dinosaurs = []
        
        self.d = Dinosaur('t-rex')
        self.d2 = Dinosaur('r-rex')
        self.d3 = Dinosaur('z-rex')

    def create_herd(self):
        self.dinosaurs.append(self.d)
        self.dinosaurs.append(self.d2)
        self.dinosaurs.append(self.d3)


