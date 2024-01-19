from enums.species import Species
from organism import Plant


class Grass(Plant):
    def __init__(self, x, y, age):
        self.color = (0, 128, 0)
        self.force = 0
        self.initiative = 0
        self.species = Species.Grass
        super().__init__(x, y, age, self.force, self.initiative, self.color, self.species)

    def __str__(self):
        return "Grass"
