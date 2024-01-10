from organism import Animal


class Turtle(Animal):
    def __init__(self, x, y):
        self.color = (199, 198, 31)
        self.force = 2
        self.initiative = 1
        super().__init__(x, y, self.force, self.initiative, self.color)

    def __str__(self):
        return "Turtle"
