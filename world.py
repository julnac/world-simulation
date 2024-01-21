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
from totem import Totem

from enums.species import Species

existing_organisms = []
existing_totems = []
score = 0


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
    if reference_organism.species == Species.Antelope:
        directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]
    else:
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    while True:
        dx, dy = random.choice(directions)
        x, y = (reference_organism.x + dx), (reference_organism.y + dy)

        if x < 0 or x >= CELL_NUMBER or y < 0 or y >= CELL_NUMBER:
            continue

        return x, y


def find_empty_adjacent_position(board, reference_organism):
    generate_try_counter = 0
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    # find position further if everything is full?
    while True:
        dx, dy = random.choice(directions)
        x, y = (reference_organism.x + dx), (reference_organism.y + dy)

        if x < 0 or x >= CELL_NUMBER or y < 0 or y >= CELL_NUMBER:
            continue

        if not board[x][y]:
            return x, y
        else:
            generate_try_counter += 1
            if generate_try_counter > 10:
                # print("Exceeded 10 tries.")
                return None


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
        if animal1.species == animal2.species:
            if animal1.age > 5 and animal2.age > 5:
                collision_type = "procreation"
            elif (animal1.age > 5 > animal2.age) or (animal1.age < 5 < animal2.age):
                collision_type = "none"
            elif animal1.age < 5 < round_counter and animal2.age < 5:
                collision_type = "fight"
            else:
                collision_type = "none"
        else:
            if animal2.species == Species.Turtle and animal1.force < 5:
                collision_type = "special_turtle_defense"
            elif animal2.species == Species.Antelope:
                if random.random() < 0.5:
                    collision_type = "special_antelope_escape"
                else:
                    collision_type = "fight"
            else:
                collision_type = "fight"
        return collision_type
    return "none"


def check_collision_with_totem(human):
    global score
    for totem in existing_totems:
        if human.x == totem.x and human.y == totem.y and totem.visibility:
            totem.visibility = False
            score += 1
    if score == 3:
        return "victory"


def update_ranking():
    existing_organisms.sort(key=lambda x: (-x.initiative, -x.age))
    # for organism in existing_animals:
    # print(f"{organism}(id:{organism.id}), age: {organism.age} | ", end="")


def move(organism, existing_organisms):
    # TODO - niektórym organizmom czasem nie dolicza wieku
    organism.age += 1
    next_position = generate_position("adjacent", existing_organisms, organism)
    action_type = organism.action(next_position, existing_organisms)
    if action_type == "grow" and organism.age > 2:
        grow_position = generate_position("empty-adjacent", existing_organisms, organism)
        if grow_position is not None:
            new_plant = create_organism(organism.species, grow_position[0], grow_position[1])
            existing_organisms.append(new_plant)
            print(f'{organism}({organism.id}) grows')


def procreate(organism):
    position = generate_position("empty-adjacent", existing_organisms, organism)
    if position is not None:
        new_organism = create_organism(organism.species, position[0], position[1])
        existing_organisms.append(new_organism)
        update_ranking()


def fight(organism, other_organism):
    organism.collision(other_organism)

    if organism.force < other_organism.force:
        print(f"{other_organism}({other_organism.id}) kills {organism}({organism.id})")
        # TODO - do not recognise human by color xd
        if organism.color == (255, 0, 128):
            print("GAME OVER")
            return "game_over"
        # TODO - ValueError: list.remove(x): x not in list
        existing_organisms.remove(organism)
    else:
        print(f"{organism}({organism.id}) kills {other_organism}({other_organism.id})")
        if other_organism.species == Species.Guarana:
            organism.force += 3
            print(f"{organism}({organism.id}) gains +3 to force")
        if other_organism.color == (255, 0, 128):
            print("GAME OVER")
            return "game_over"
        existing_organisms.remove(other_organism)
    update_ranking()
    return "game"


def create_totems(number):
    for _ in range(0, number):
        position = generate_position("random", existing_organisms)
        totem = Totem(position[0], position[1], True)
        existing_totems.append(totem)


class World:
    def __init__(self):
        global score
        Organism.id_counter = 1
        self.round_counter = 0
        score = 0
        existing_organisms.clear()
        existing_totems.clear()
        initial_organisms_count = 30
        self.human = get_human()
        existing_organisms.append(self.human)
        chosen_animal_types = choose_animal_type_randomly(initial_organisms_count)
        for animal_type in chosen_animal_types:
            position = generate_position("random", existing_organisms)
            org = create_organism(animal_type, position[0], position[1])
            if org is not None:
                existing_organisms.append(org)
        create_totems(3)
        update_ranking()

    def make_round(self) -> str:
        self.round_counter += 1
        print(f'#---Round {self.round_counter}---#')
        state = "game"
        sub_state = " "
        for organism in existing_organisms:
            move(organism, existing_organisms)
            for other_organism in existing_organisms:
                if other_organism != organism:
                    match check_collision(organism, other_organism, self.round_counter):
                        case "procreation":
                            procreate(organism)
                        case "fight":
                            state = fight(organism, other_organism)
                            if state == "game_over":
                                break
                        case "none":
                            pass
                        case "special_turtle_defense":
                            organism.step_back()
                            print(f'{organism}({organism.id}) steps back from {other_organism}({other_organism.id})')
                        case "special_antelope_escape":
                            move(other_organism, existing_organisms)
                            print(f'{other_organism}({other_organism.id}) escapes from {organism}({organism.id})')
                        case _:
                            print("Error")
            if organism.color == (255, 0, 128):
                sub_state = check_collision_with_totem(organism)
            if sub_state == "victory":
                return "victory"
            if state == "game_over":
                return "game_over"
        return state

    def draw_world(self, screen):
        for o in existing_organisms:
            o.draw(screen)
        # self.human.draw(screen)
        for totem in existing_totems:
            if totem.visibility:
                image = pygame.image.load(f'assets/totem.png')
                screen.blit(image, (totem.x * CELL_SIZE, totem.y * CELL_SIZE))
                # pygame.draw.rect(screen, (255, 255, 0), (totem.x * CELL_SIZE, totem.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        for i in range(CELL_NUMBER):
            pygame.draw.line(screen, (89, 81, 68), (0, i*CELL_SIZE), (CELL_NUMBER*CELL_SIZE, i*CELL_SIZE))
        for i in range(CELL_NUMBER):
            pygame.draw.line(screen, (89, 81, 68), (i * CELL_SIZE, 0), (i * CELL_SIZE, CELL_NUMBER * CELL_SIZE))

        font = pygame.font.SysFont('arial', 15)
        font_bold = pygame.font.SysFont('arial', 15, pygame.font.Font.bold)

        pygame.draw.rect(screen, (218, 192, 154), pygame.Rect(GAME_WIDTH, 0, RANKING_WIDTH, GAME_HEIGHT))

        turn_surface = font_bold.render(f"Turn {self.round_counter}", True, (89, 81, 68))
        screen.blit(turn_surface, ((CELL_NUMBER * CELL_SIZE) + 5, 5))

        score_surface = font_bold.render(f"Score {score}", True, (89, 81, 68))
        screen.blit(score_surface, ((CELL_NUMBER * CELL_SIZE) + 5, 25))

        header_surface = font_bold.render("Ranking:", True, (89, 81, 68))
        screen.blit(header_surface, ((CELL_NUMBER * CELL_SIZE) + 5, 45))
        animal_counter = 1
        y_offset = 65

        for organism in existing_organisms:
            if organism.initiative != 0:
                text_surface = font.render(f"{animal_counter}. [ {organism.id} ] {organism}, age: {organism.age}, force:{organism.force}", True, (89, 81, 68))
                screen.blit(text_surface, ((CELL_NUMBER * CELL_SIZE) + 5, 5 + y_offset))
                y_offset += 20
                animal_counter += 1


