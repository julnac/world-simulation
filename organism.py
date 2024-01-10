from abc import ABC, abstractmethod
from constants import *
import pygame
import random


class Organism(ABC):
    def __init__(self, x, y, force=None, initiative=None, color=None):
        self.x = x
        self.y = y
        self.force = force
        self.initiative = initiative
        self.color = color
        self.directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    @abstractmethod
    def action(self):
        pass

    def collision(self):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))


class Animal(Organism):
    def __init__(self, x, y, force=None, initiative=None, color=None):
        super().__init__(x, y, force, initiative, color)

    def action(self):
        super().action()
        dx, dy = random.choice(self.directions)
        self.x += dx
        self.y += dy

        self.x = max(0, min(self.x, CELL_NUMBER - 1))
        self.y = max(0, min(self.y, CELL_NUMBER - 1))

    # def collision(self):
    #     super().collision()
    #     print(f"Collision: {self} and {other_animal}")


class Plant(Organism):
    def __init__(self, x, y, force, color):
        self.initiative = 0
        super().__init__(x, y, force, self.initiative, color)

    def action(self):
        pass
