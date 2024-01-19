import unittest
from world import create_organism, generate_position


class GeneratePositionTest(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        pass
    #
    # @staticmethod
    # def test__given_no_parent__when_generate_position__then_return_valid_position():
    #     # Arrange
    #     existing_organism_initial_position_x = 0
    #     existing_organism_initial_position_y = 0
    #
    #     wolf = get_animal("Wolf", existing_organism_initial_position_x, existing_organism_initial_position_y)
    #     organisms = [wolf]
    #     location_search_policy = "random"
    #
    #     # Act
    #     x, y = generate_position(location_search_policy, organisms)
    #
    #     # Assert
    #     assert x is not existing_organism_initial_position_x
    #     assert y is not existing_organism_initial_position_y
    #
    #     print(f"x: {x}, y: {y}")

    @staticmethod
    def test__given_parent__when_generate_position__then_return_valid_position():
        # Arrange
        existing_organism_initial_position_x = 5
        existing_organism_initial_position_y = 5
        parent_initial_position_x = 6
        parent_initial_position_y = 5

        wolf1 = create_organism("Wolf", existing_organism_initial_position_x, existing_organism_initial_position_y)
        wolf2 = create_organism("Wolf", parent_initial_position_x, parent_initial_position_y)
        organisms = [wolf1, wolf2]
        location_search_policy = "adjacent"

        # Act
        x, y = generate_position(location_search_policy, organisms, wolf2)

        # Assert
        assert x is not existing_organism_initial_position_x
        assert y is not existing_organism_initial_position_y

        print(f"x: {x}, y: {y}")


if __name__ == "__main__":
    unittest.main()
