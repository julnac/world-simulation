from organism import Animal
from Direction import Direction
from constants import *
from enums.species import Species


class Human(Animal):
    def __init__(self, x, y, age):
        self.color = (255, 0, 128)
        self.image = 'human.png'
        self.force = 5
        self.initiative = 4
        self.elixir_counter = 0
        super().__init__(x, y, age, self.force, self.initiative, color=self.color, image=self.image)

    def __str__(self):
        return "HUMAN"

    def magic_elixir(self):
        if self.elixir_counter == 0:
            self.elixir_counter = 10
            self.force += 10

    def reduce_force(self):
        if self.elixir_counter > 0:
            self.elixir_counter -= 1
            self.force -= 1

    def action(self, next_position, existing_organisms=None):
        self.x = max(0, min(self.x, CELL_NUMBER - 1))
        self.y = max(0, min(self.y, CELL_NUMBER - 1))
        self.reduce_force()


