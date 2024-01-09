import random
from constants import *
from animals.wolf import Wolf
from animals.sheep import Sheep
from animals.fox import Fox
from animals.turtle import Turtle
from animals.antelope import Antelope
from animals.human import Human
import pygame

animal_type_list = ["wolf", "sheep", "fox", "turtle", "antelope"]


def choose_animal_type_randomly(animals, number):
    chosen_animal_types = []
    for animal in range(number):
        # dodaj żeby gatunki się nie powtarzały
        chosen_animal_types.append(random.choice(animals))
    return chosen_animal_types


def get_animal(animal_type):
    x = random.randint(0, CELL_NUMBER - 1)
    y = random.randint(0, CELL_NUMBER - 1)
    if animal_type == "wolf":
        return Wolf(x, y)
    elif animal_type == "sheep":
        return Sheep(x, y)
    elif animal_type == "fox":
        return Turtle(x, y)
    elif animal_type == "turtle":
        return Antelope(x, y)
    elif animal_type == "antelope":
        return Fox(x, y)
    else:
        return None


def get_human():
    human = Human(int(CELL_NUMBER / 2), int(CELL_NUMBER / 2))
    return human


class World:
    def __init__(self):
        self.existing_animals = []
        chosen_animal_types = choose_animal_type_randomly(animal_type_list, 5)
        for animal_type in chosen_animal_types:
            self.existing_animals.append(get_animal(animal_type))
        self.human = get_human()

    def make_round(self):
        for o in self.existing_animals:
            o.action()

    def draw_world(self, screen):
        for o in self.existing_animals:
            o.draw(screen)
        self.human.draw(screen)

        for i in range(CELL_NUMBER):
            pygame.draw.line(screen, (71, 71, 71), (0, i*CELL_SIZE), (CELL_NUMBER*CELL_SIZE, i*CELL_SIZE))
        for i in range(CELL_NUMBER):
            pygame.draw.line(screen, (71, 71, 71), (i * CELL_SIZE, 0), (i * CELL_SIZE, CELL_NUMBER * CELL_SIZE))


