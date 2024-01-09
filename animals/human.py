from organism import Animal


class Human(Animal):
    def __init__(self, x, y):
        self.color = (255, 0, 128)
        self.force = 5
        self.initiative = 4
        super().__init__(x, y, self.force, self.initiative, self.color)

