from organism import Animal
from Direction import Direction
from constants import *


class Human(Animal):
    def __init__(self, x, y, age):
        self.color = (255, 0, 128)
        self.force = 5
        self.initiative = 4
        super().__init__(x, y, age, self.force, self.initiative, self.color)

    def __str__(self):
        return "HUMAN"

    def action(self, next_position, existing_organisms=None):
        self.x = max(0, min(self.x, CELL_NUMBER - 1))
        self.y = max(0, min(self.y, CELL_NUMBER - 1))
