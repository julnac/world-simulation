import random
from constants import *
from animals.wolf import Wolf
from animals.sheep import Sheep
from animals.fox import Fox
from animals.turtle import Turtle
from animals.antelope import Antelope
from animals.cyber_sheep import CyberSheep
from animals.human import Human
import pygame

animal_type_list = ["wolf", "sheep", "fox", "turtle", "antelope", "cyber_sheep"]


def choose_animal_type_randomly(animals, number):
    chosen_animal_types = []
    for animal in range(number):
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
    elif animal_type == "cyber_sheep":
        return CyberSheep(x, y)
    else:
        return None


def get_human():
    human = Human(int(CELL_NUMBER // 2), int(CELL_NUMBER // 2))
    return human


def check_collision(animal1, animal2):
    return animal1.x == animal2.x and animal1.y == animal2.y


class World:
    def __init__(self):
        self.existing_animals = []
        chosen_animal_types = choose_animal_type_randomly(animal_type_list, 7)
        for animal_type in chosen_animal_types:
            self.existing_animals.append(get_animal(animal_type))
        self.human = get_human()
        self.existing_animals.append(self.human)
        self.existing_animals.sort(key=lambda x: x.initiative, reverse=True)
        for a in self.existing_animals:
            print(f"{a}, pos: {a.x}, {a.y} | ", end="")

    def make_round(self):
        for o in self.existing_animals:
            o.action()
            for other_animal in self.existing_animals:
                if other_animal != o:
                    if check_collision(o, other_animal):
                        o.collision()
                        print(f"Collision: {o} invades {other_animal} !")
        # self.human.action()

    def draw_world(self, screen):
        for o in self.existing_animals:
            o.draw(screen)
        self.human.draw(screen)

        for i in range(CELL_NUMBER):
            pygame.draw.line(screen, (71, 71, 71), (0, i*CELL_SIZE), (CELL_NUMBER*CELL_SIZE, i*CELL_SIZE))
        for i in range(CELL_NUMBER):
            pygame.draw.line(screen, (71, 71, 71), (i * CELL_SIZE, 0), (i * CELL_SIZE, CELL_NUMBER * CELL_SIZE))


