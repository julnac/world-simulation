from enums.species import Species
from organism import Plant
import random


class Milkweed(Plant):
    def __init__(self, x, y, age):
        self.color = (255, 215, 0)
        self.image = 'milkweed.png'
        self.force = 0
        self.initiative = 0
        self.species = Species.Milkweed
        super().__init__(x, y, age, self.force, self.initiative, self.color, self.species, self.image)

    def __str__(self):
        return "Milkweed"

    def action(self, next_position, existing_organisms=None):
        if random.random() < 0.3:
            return "grow"
        else:
            return "none"


