import random

def gen_location(self, amino, protein: int, occupied_pos, last_pos=(0,0)):
    """Generates a valid random location for the amino acid to be placed."""

    # Directions the next amino acid can go, up, down, left, or right.
    directions = [(0,1), (0,-1), (-1,0), (1,0)]
    random.shuffle(directions)

    for direction in directions:
        new_pos = (last_pos[0] + direction[0], last_pos[1] + direction[1])

        if 0 <= new_pos[0] < protein and 0 <= new_pos[1] < protein and new_pos not in occupied_pos:
            return new_pos

    # If no valid positions were found, return None
    return None

def test_gen_location():
    """Test the gen_location function."""
    
    protein = 5
    occ_pos = [(0, 0), (0, 1), (1, 1)]
    last_position = (1, 1)

    # Testing gen_location function
    new_position = gen_location(None, protein, occ_pos, last_position)

    print(f"New position generated: {new_position}")

# Now call the test function
test_gen_location()
