from enums.species import Species
from organism import Plant


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

    # def action(self, next_position):
    #     super().action(next_position)
    #     for _ in range(0, 3):
    #         Milkweed.action(self, next_position)
