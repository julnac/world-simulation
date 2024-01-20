from enums.species import Species
from organism import Plant


class WolfBerries(Plant):
    def __init__(self, x, y, age):
        self.color = (0, 0, 128)
        self.image = 'wolf_berries.png'
        self.force = 99
        self.initiative = 0
        self.species = Species.WolfBerries
        super().__init__(x, y, age, self.force, self.initiative, self.color, self.species, self.image)

    def __str__(self):
        return "WolfBerries"
