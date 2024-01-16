from enums.species import Species
from organism import Plant


class Hogweed(Plant):
    def __init__(self, x, y, age):
        self.color = (194, 218, 184)
        self.force = 10
        self.initiative = 0
        self.species = Species.Hogweed
        super().__init__(x, y, age, self.force, self.initiative, self.color, self.species)

    def __str__(self):
        return "Hogweed"