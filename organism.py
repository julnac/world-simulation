from abc import ABC, abstractmethod
from constants import *
import pygame
import random


class Organism(ABC):
    id_counter = 1

    def __init__(self, x, y, age, force=None, initiative=None, color=None, species=None):
        self.x = x
        self.y = y
        self.force = force
        self.initiative = initiative
        self.color = color
        self.species = species
        self.age = age
        self.id = Organism.id_counter
        Organism.id_counter += 1

    @abstractmethod
    def action(self, vector):
        pass

    def collision(self, other_organism):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        font = pygame.font.SysFont('arial', 36)
        text_surface = font.render(str(self.id), True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(self.x * CELL_SIZE + CELL_SIZE // 2,
                                                  self.y * CELL_SIZE + CELL_SIZE // 2))
        screen.blit(text_surface, text_rect)


class Animal(Organism):
    def __init__(self, x, y, age, force=None, initiative=None, color=None, species=None):
        super().__init__(x, y, age, force, initiative, color, species)

    def action(self, next_position):
        x, y = next_position
        self.x = x
        self.y = y
        return "none"


class Plant(Organism):
    def __init__(self, x, y, age, force=None, initiative=None, color=None, species=None):
        super().__init__(x, y, age, force, initiative, color, species)

    def action(self, next_position):
        if random.random() < 0.1:
            return "grow"
        else:
            return "none"

