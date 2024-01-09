from organism import Animal


class Antelope(Animal):
    def __init__(self, x, y):
        self.color = (202, 160, 142)
        self.force = 4
        self.initiative = 4
        super().__init__(x, y, self.force, self.initiative, self.color)