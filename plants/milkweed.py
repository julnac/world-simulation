from enums.species import Species
from organism import Plant


class Milkweed(Plant):
    def __init__(self, x, y, age):
        self.color = (255, 215, 0)
        self.force = 0
        self.initiative = 0
        self.species = Species.Milkweed
        super().__init__(x, y, age, self.force, self.initiative, self.color, self.species)

    def __str__(self):
        return "Milkweed"