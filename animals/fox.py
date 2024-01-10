from enums.species import Species
from organism import Animal


class Fox(Animal):
    def __init__(self, x, y):
        self.color = (254, 127, 0)
        self.force = 3
        self.initiative = 7
        self.species = Species.Fox
        super().__init__(x, y, self.force, self.initiative, self.color, self.species)

    def __str__(self):
        return "Fox"

    def action(self, vector):
        super().action(vector)
        # Good smell
