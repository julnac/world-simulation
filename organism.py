from abc import ABC, abstractmethod
from constants import *
import pygame
import random
from enums.species import Species


class Organism(ABC):
    id_counter = 1

    def __init__(self, x, y, age, force=None, initiative=None, color=None, species=None, image=None):
        self.x = x
        self.y = y
        self.force = force
        self.initiative = initiative
        self.color = color
        self.image = image
        self.species = species
        self.age = age
        self.id = Organism.id_counter
        Organism.id_counter += 1

    @abstractmethod
    def action(self, next_position, existing_organisms=None):
        pass

    def collision(self, other_organism):
        pass

    def draw(self, screen):
        # pygame.draw.rect(screen, self.color, (self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        image = pygame.image.load(f'assets/{self.image}')
        screen.blit(image, (self.x * CELL_SIZE, self.y * CELL_SIZE))

        if self.initiative != 0:
            font = pygame.font.SysFont('arial', 15)
            text_surface = font.render(str(self.id), True, (30, 30, 30))
            text_rect = text_surface.get_rect(center=(self.x * CELL_SIZE + CELL_SIZE // 2 + 8,
                                                      self.y * CELL_SIZE + CELL_SIZE // 2 - 8))
            screen.blit(text_surface, text_rect)


class Animal(Organism):
    def __init__(self, x, y, age, force=None, initiative=None, color=None, species=None, image=None):
        super().__init__(x, y, age, force, initiative, color, species, image)
        self.previous_position = (0, 0)

    def action(self, next_position, existing_organisms=None):
        self.move(next_position)

    def move(self, next_position):
        self.previous_position = (self.x, self.y)

        x, y = next_position
        self.x = x
        self.y = y

        return "none"

    def step_back(self):
        self.move(self.previous_position)


class Plant(Organism):
    def __init__(self, x, y, age, force=None, initiative=None, color=None, species=None, image=None):
        super().__init__(x, y, age, force, initiative, color, species, image)

    def action(self, next_position, existing_organisms=None):
        if random.random() < 0.1:
            return "grow"
        else:
            return "none"

