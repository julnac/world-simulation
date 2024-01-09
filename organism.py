from abc import ABC, abstractmethod
from constants import *
import pygame


class Organism(ABC):
    def __init__(self, force, initiative, x, y, color=None):
        self.force = force
        self.initiative = initiative
        self.x = x
        self.y = y
        self.color = color

    @abstractmethod
    def action(self):
        pass

    def collision(self):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))


class Animal(Organism):
    def __init__(self, force, initiative, x, y, color=None):
        super().__init__(force, initiative, x, y, color)

    def action(self):
        pass


class Plant(Organism):
    def __init__(self, force, initiative, x, y, world, color):
        super().__init__(force, initiative, x, y, world, color)
        initiative = 0

    def action(self):
        pass
