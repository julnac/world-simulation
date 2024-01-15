from enums.species import Species
from organism import Animal


class Wolf(Animal):
    def __init__(self, x, y, age):
        self.color = (128, 128, 128)
        self.force = 9
        self.initiative = 5
        self.species = Species.Wolf
        super().__init__(x, y, age, self.force, self.initiative, self.color, self.species)

    def __str__(self):
        return "Wolf"
