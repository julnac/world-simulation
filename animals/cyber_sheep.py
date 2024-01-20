from enums.species import Species
from organism import Animal
import math
from Direction import Direction


def check_distance(x, y, target):
    distance_x = math.fabs(target.x - x)
    distance_y = math.fabs(target.y - y)
    return distance_x + distance_y


class CyberSheep(Animal):
    def __init__(self, x, y, age):
        self.color = (175, 238, 238)
        self.image = 'cyber_sheep.png'
        self.force = 11
        self.initiative = 4
        self.species = Species.CyberSheep
        super().__init__(x, y, age, self.force, self.initiative, self.color, self.species, self.image)

    def __str__(self):
        return "CyberSheep"

    def go_to(self, target, initial_distance):
        # distance_x = target.x - self.x
        # distance_y = target.y - self.y

        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        for direction in directions:
            x, y = direction[0] + self.x, direction[1] + self.y
            distance = check_distance(x, y, target)
            if distance < initial_distance:
                self.x = x
                self.y = y
                break

    def action(self, next_position, existing_organisms=None):
        self.previous_position = (self.x, self.y)
        nearest_distance = 1000000
        nearest_organism = None
        for o in existing_organisms:
            if o.species == Species.Hogweed:
                distance = check_distance(self.x, self.y, o)
                if distance < nearest_distance:
                    nearest_distance = distance
                    nearest_organism = o

        if nearest_organism is not None:
            self.go_to(nearest_organism, nearest_distance)
            return "none"
        else:
            super().move(next_position)



