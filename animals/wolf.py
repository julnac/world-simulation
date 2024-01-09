from constants import *
from organism import Animal


class Wolf(Animal):
    def __init__(self, force, initiative, x, y):
        self.color = (128, 128, 128)
        super().__init__(force, initiative, x, y, self.color)
