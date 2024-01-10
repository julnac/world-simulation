from organism import Animal


class CyberSheep(Animal):
    def __init__(self, x, y):
        self.color = (175, 238, 238)
        self.force = 11
        self.initiative = 4
        super().__init__(x, y, self.force, self.initiative, self.color)

    def __str__(self):
        return "CyberSheep"