import random

import numpy as np

from constants import *
from animals.wolf import Wolf
from animals.sheep import Sheep
from animals.fox import Fox
from animals.turtle import Turtle
from animals.antelope import Antelope
from animals.cyber_sheep import CyberSheep
from animals.human import Human
from plants.grass import Grass
from plants.wolf_berries import WolfBerries
from plants.guarana import Guarana
from plants.hogweed import Hogweed
from plants.milkweed import Milkweed
from organism import Organism
import pygame

from enums.species import Species

# animal_type_list = ["Wolf", "Sheep", "Fox", "Turtle", "Antelope", "CyberSheep"]
# plant_type_list = ["Grass", "Milkweed", "Guarana", "WolfBerries", "Hogweed"]
existing_animals = []


def choose_animal_type_randomly(number):
    species_list = list(Species)
    return [random.choice(species_list) for _ in range(number)]


def board_is_full(organisms):
    return len(organisms) == CELL_NUMBER**2


def generate_initial_position(board):
    generate_try_counter = 0
    while True:
        x = np.random.randint(low=0, high=CELL_NUMBER)
        y = np.random.randint(low=0, high=CELL_NUMBER)
        if x >= CELL_NUMBER or y >= CELL_NUMBER:
            raise Exception("TOO big")

        if not board[x][y]:
            return x, y
        else:
            generate_try_counter += 1
            if generate_try_counter > 10:
                print("Exceeded 10 tries.")


def find_adjacent_position(reference_organism):
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    while True:
        dx, dy = random.choice(directions)
        x, y = (reference_organism.x + dx), (reference_organism.y + dy)

        if x < 0 or x >= CELL_NUMBER or y < 0 or y >= CELL_NUMBER:
            continue

        return x, y


def find_empty_adjacent_position(board, reference_organism):
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    # find position further if everything is full?
    while True:
        dx, dy = random.choice(directions)
        x, y = (reference_organism.x + dx), (reference_organism.y + dy)

        if x < 0 or x >= CELL_NUMBER or y < 0 or y >= CELL_NUMBER:
            continue

        if not board[x][y]:
            return x, y


def generate_position(location_search_policy, existing_organisms, reference_organism=None):
    if board_is_full(existing_organisms):
        raise Exception("Board is full. Cannot find position for another organism.")

    board = np.full((CELL_NUMBER, CELL_NUMBER), False)
    for o in existing_organisms:
        board[o.x][o.y] = True

    if location_search_policy == "random":
        return generate_initial_position(board)

    elif location_search_policy == "adjacent":
        return find_adjacent_position(reference_organism)

    elif location_search_policy == "empty-adjacent":
        return find_empty_adjacent_position(board, reference_organism)

    return None, None


def create_organism(species: Species, x, y) -> Organism:
    if species == Species.Wolf:
        return Wolf(x, y, 0)
    elif species == Species.Sheep:
        return Sheep(x, y, 0)
    elif species == Species.Fox:
        return Fox(x, y, 0)
    elif species == Species.Turtle:
        return Turtle(x, y, 0)
    elif species == Species.Antelope:
        return Antelope(x, y, 0)
    elif species == Species.CyberSheep:
        return CyberSheep(x, y, 0)
    elif species == Species.WolfBerries:
        return WolfBerries(x, y, 0)
    elif species == Species.Grass:
        return Grass(x, y, 0)
    elif species == Species.Milkweed:
        return Milkweed(x, y, 0)
    elif species == Species.Guarana:
        return Guarana(x, y, 0)
    elif species == Species.Hogweed:
        return Hogweed(x, y, 0)


def get_human():
    human = Human(int(CELL_NUMBER // 2), int(CELL_NUMBER // 2), 0)
    return human


def check_collision(animal1, animal2, round_counter):
    if animal2 != animal1 and animal1.x == animal2.x and animal1.y == animal2.y:
        # TODO - nie rozpoznawaj gatunku po kolorze
        if animal1.color == animal2.color:
            if animal1.age > 5 and animal2.age > 5:
                collision_type = "procreation"
            elif (animal1.age > 5 > animal2.age) or (animal1.age < 5 < animal2.age):
                collision_type = "none"
            elif animal1.age < 5 < round_counter and animal2.age < 5:
                collision_type = "fight"
            else:
                collision_type = "none"
        else:
            collision_type = "fight"
        return collision_type
    return "none"


def update_ranking():
    existing_animals.sort(key=lambda x: (-x.initiative, -x.age))
    # for organism in existing_animals:
    # print(f"{organism}(id:{organism.id}), age: {organism.age} | ", end="")


class World:
    def __init__(self):
        Organism.id_counter = 1
        self.round_counter = 0
        existing_animals.clear()
        initial_organisms_count = 10
        chosen_animal_types = choose_animal_type_randomly(initial_organisms_count)
        for animal_type in chosen_animal_types:
            position = generate_position("random", existing_animals)
            animal = create_organism(animal_type, position[0], position[1])
            if animal is not None:
                existing_animals.append(animal)
        self.human = get_human()
        existing_animals.append(self.human)
        update_ranking()

    def make_round(self) -> str:
        state = "game"
        for organism in existing_animals:
            # TODO - niektórym organizmom czasem nie dolicza wieku
            organism.age += 1
            next_position = generate_position("adjacent", existing_animals, organism)
            organism.action(next_position)
            for other_organism in existing_animals:
                if other_organism != organism:
                    match check_collision(organism, other_organism, self.round_counter):
                        case "procreation":
                            position = generate_position("empty-adjacent", existing_animals, organism)
                            new_organism = create_organism(organism.species, position[0], position[1])
                            existing_animals.append(new_organism)
                            update_ranking()
                        case "fight":
                            organism.collision(other_organism)
                            if organism.force < other_organism.force:
                                print(f"{other_organism}({other_organism.id}) kills {organism}({organism.id})")
                                if organism.color == (255, 0, 128):
                                    print("GAME OVER")
                                    state = "game_over"
                                    break
                                existing_animals.remove(organism)
                            else:
                                print(f"{organism}({organism.id}) kills {other_organism}({other_organism.id})")
                                if other_organism.color == (255, 0, 128):
                                    print("GAME OVER")
                                    state = "game_over"
                                    break
                                existing_animals.remove(other_organism)
                            update_ranking()
                        case "none":
                            pass
                        case _:
                            print("Error")

            if state == "game_over":
                return "game_over"
        return state

    def draw_world(self, screen):
        self.round_counter += 1

        for o in existing_animals:
            o.draw(screen)
        self.human.draw(screen)

        for i in range(CELL_NUMBER):
            pygame.draw.line(screen, (71, 71, 71), (0, i*CELL_SIZE), (CELL_NUMBER*CELL_SIZE, i*CELL_SIZE))
        for i in range(CELL_NUMBER):
            pygame.draw.line(screen, (71, 71, 71), (i * CELL_SIZE, 0), (i * CELL_SIZE, CELL_NUMBER * CELL_SIZE))

        font = pygame.font.SysFont('arial', 15)

        pygame.draw.rect(screen, (225, 225, 225), pygame.Rect(GAME_WIDTH, 0, 200, GAME_HEIGHT))
        header_surface = font.render("Ranking", True, (71, 71, 71))
        screen.blit(header_surface, ((CELL_NUMBER * CELL_SIZE) + 5, 5))
        y_offset = 30
        animal_counter = 1

        for organism in existing_animals:
            text_surface = font.render(f"{animal_counter}. [ {organism.id} ] {organism}, age: {organism.age}", True, (71, 71, 71))
            screen.blit(text_surface, ((CELL_NUMBER * CELL_SIZE) + 5, 5 + y_offset))
            y_offset += 20
            animal_counter += 1

        turn_surface = font.render(f"Turn {self.round_counter}", True, (71, 71, 71))
        screen.blit(turn_surface, ((CELL_NUMBER * CELL_SIZE) + 5, 20 + y_offset))
