from enums.species import Species
from organism import Animal


class Turtle(Animal):
    def __init__(self, x, y, age):
        self.color = (199, 198, 31)
        self.force = 2
        self.initiative = 1
        self.species = Species.Turtle
        super().__init__(x, y, age, self.force, self.initiative, self.color, self.species)

    def __str__(self):
        return "Turtle"
