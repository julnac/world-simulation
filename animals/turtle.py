import random

from enums.species import Species
from organism import Animal


class Turtle(Animal):
    def __init__(self, x, y, age):
        self.color = (199, 198, 31)
        self.image = 'turtle.png'
        self.force = 2
        self.initiative = 1
        self.species = Species.Turtle
        super().__init__(x, y, age, self.force, self.initiative, self.color, self.species, self.image)

    def __str__(self):
        return "Turtle"

    def action(self, next_position, existing_organisms=None):
        if random.random() < 0.75:
            pass
        else:
            super().move(next_position)
