from organism import Animal


class Wolf(Animal):
    def __init__(self, x, y):
        self.color = (128, 128, 128)
        self.force = 9
        self.initiative = 5
        super().__init__(x, y, self.force, self.initiative, self.color)

    def __str__(self):
        return "Wolf"
