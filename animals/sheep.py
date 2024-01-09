from constants import *
from organism import Animal


class Sheep(Animal):
    def __init__(self, force, initiative, x, y):
        self.color = (255, 255, 255)
        super().__init__(force, initiative, x, y, self.color)

