from organism import Animal


class Sheep(Animal):
    def __init__(self, x, y):
        self.color = (255, 255, 255)
        self.force = 4
        self.initiative = 4
        super().__init__(x, y, self.force, self.initiative, self.color)

