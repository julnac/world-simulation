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

animal_type_list = ["Wolf"]
# animal_type_list = ["wolf", "sheep", "fox", "turtle", "antelope", "cyber_sheep"]
plant_type_list = ["grass", "milkweed", "guarana", "wolf_berries", "hogweed"]


def choose_animal_type_randomly(animals, number):
    chosen_animal_types = []
    for animal in range(number):
        chosen_animal_types.append(random.choice(animals))
    return chosen_animal_types


def get_animal(animal_type):
    x = random.randint(0, CELL_NUMBER - 1)
    y = random.randint(0, CELL_NUMBER - 1)
    if animal_type == "Wolf":
        return Wolf(x, y)
    elif animal_type == "Sheep":
        return Sheep(x, y)
    elif animal_type == "Fox":
        return Fox(x, y)
    elif animal_type == "Turtle":
        return Turtle(x, y)
    elif animal_type == "Antelope":
        return Antelope(x, y)
    elif animal_type == "CyberSheep":
        return CyberSheep(x, y)
    else:
        return None


def get_human():
    human = Human(int(CELL_NUMBER // 2), int(CELL_NUMBER // 2))
    return human


def check_collision(animal1, animal2):
    if animal2 != animal1 and animal1.x ==  animal2.x and animal1.y ==  animal2.y:
        if animal1.color == animal2.color:
            collision_type = "procreation"
        else:
            collision_type = "fight"
        return collision_type
    return "none"

# def sexual_interaction(partner, existing_animal_list):


class World:
    def __init__(self):
        self.existing_animals = []
        chosen_animal_types = choose_animal_type_randomly(animal_type_list, 7)
        for animal_type in chosen_animal_types:
            animal = get_animal(animal_type)
            if animal is not None:
                self.existing_animals.append(animal)
        self.human = get_human()
        self.existing_animals.append(self.human)
        self.existing_animals.sort(key=lambda x: x.initiative, reverse=True)
        for a in self.existing_animals:
            print(f"{a}, pos: {a.x}, {a.y} | ", end="")

    def make_round(self):
        for organism in self.existing_animals:
            organism.action()
            for other_organism in self.existing_animals:
                match check_collision(organism, other_organism):
                    case "procreation":
                        organism_type = str(organism)
                        new_organism = get_animal(organism_type)
                        if new_organism is not None:
                            self.existing_animals.append(new_organism)
                        print(f"{organism} was born")
                        for a in self.existing_animals:
                            print(f"{a}, pos: {a.x}, {a.y} | ", end="")
                        # organism.collision(other_organism, procreation)
                    case "fight":
                        organism.collision(other_organism)
                    case "none":
                        pass
                    case _:
                        print("Error")

    def draw_world(self, screen):
        for o in self.existing_animals:
            o.draw(screen)
        self.human.draw(screen)

        for i in range(CELL_NUMBER):
            pygame.draw.line(screen, (71, 71, 71), (0, i*CELL_SIZE), (CELL_NUMBER*CELL_SIZE, i*CELL_SIZE))
        for i in range(CELL_NUMBER):
            pygame.draw.line(screen, (71, 71, 71), (i * CELL_SIZE, 0), (i * CELL_SIZE, CELL_NUMBER * CELL_SIZE))


