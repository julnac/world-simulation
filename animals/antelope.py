from enums.species import Species
from organism import Animal


class Antelope(Animal):
    def __init__(self, x, y, age):
        self.color = (202, 160, 142)
        self.force = 4
        self.initiative = 4
        self.species = Species.Antelope
        super().__init__(x, y, age, self.force, self.initiative, self.color, self.species)

    def __str__(self):
        return "Antelope"

    def action(self, next_position, existing_organisms=None):
        super().action(next_position, existing_organisms)
        pass
