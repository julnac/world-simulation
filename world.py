import random
from constants import *
from animals.wolf import Wolf
from animals.sheep import Sheep
from animals.fox import Fox

animal_type_list = ["wolf", "sheep", "fox"]


def choose_animal_type_randomly(animals, number):
    chosen_animal_types = []
    for animal in range(number):
        chosen_animal_types.append(random.choice(animals))
    return chosen_animal_types


def get_animal(animal_type):
    x = random.randint(0, CELL_NUMBER - 1)
    y = random.randint(0, CELL_NUMBER - 1)
    if animal_type == "wolf":
        return Wolf(9, 5, x, y)
    elif animal_type == "sheep":
        return Sheep(4, 4, x, y)
    elif animal_type == "fox":
        return Fox(3, 7, x, y)
    else:
        return None


class World:
    def __init__(self):
        self.existing_animals = []
        chosen_animal_types = choose_animal_type_randomly(animal_type_list, 2)
        for animal_type in chosen_animal_types:
            self.existing_animals.append(get_animal(animal_type))


    def make_round(self):
        pass
        # self.organism.action()

    def draw_world(self, screen):
        for o in self.existing_animals:
            o.draw(screen)
