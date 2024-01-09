from organism import Animal


class Fox(Animal):
    def __init__(self, x, y):
        self.color = (254, 127, 0)
        self.force = 3
        self.initiative = 7
        super().__init__(x, y, self.force, self.initiative, self.color)

    def action(self):
        super().action()
        # Good smell
