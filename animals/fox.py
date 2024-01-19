from enums.species import Species
from organism import Animal


class Fox(Animal):
    def __init__(self, x, y, age):
        self.color = (254, 127, 0)
        self.force = 3
        self.initiative = 7
        self.species = Species.Fox
        super().__init__(x, y, age, self.force, self.initiative, self.color, self.species)

    def __str__(self):
        return "Fox"

    def action(self, next_position, existing_organisms):
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        possible_locations = []
        for direction in directions:
            x, y = direction[0] + self.x, direction[1] + self.y
            possible_locations.append((x, y))
        for location in possible_locations:
            for organism in existing_organisms:
                if location[0] == organism.x and location[1] == organism.y and organism.force > self.force:
                    possible_locations.remove(location)
                    print(f"Fox({self.id}) avoids {organism}({organism.id})")

        for pos in possible_locations:
            if pos == next_position:
                super().move(next_position)
            else:
                pass


