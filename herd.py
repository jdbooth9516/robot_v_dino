from dino import Dinosaur


class Herd:
    def __init__(self, num):
        self.dinosaurs = []
        self.num = num
        

    def create_herd(self ):
        for i in range(self.num):
            self.dinosaurs.append(Dinosaur())

