from enums.species import Species
from organism import Animal


class Sheep(Animal):
    def __init__(self, x, y, age):
        self.color = (255, 255, 255)
        self.image = 'sheep.png'
        self.force = 4
        self.initiative = 4
        self.species = Species.Sheep
        super().__init__(x, y, age, self.force, self.initiative, self.color, self.species, self.image)

    def __str__(self):
        return "Sheep"
