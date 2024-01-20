from enums.species import Species
from organism import Animal


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

    def action(self, next_position, existing_organisms=None):
        # for o in existing_organisms:
            # if o.species == Species.Hogweed:
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