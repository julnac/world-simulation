from constants import *
from organism import Animal


class Fox(Animal):
    def __init__(self, force, initiative, x, y):
        self.color = (254, 127, 0)
        super().__init__(force, initiative, x, y, self.color)

    def action(self):
        super().action()
        # Good smell
