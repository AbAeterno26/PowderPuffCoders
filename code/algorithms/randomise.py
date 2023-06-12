import random

def gen_location(self, amino, protein: int, protein_length, occupied_pos, last_pos=(0,0)):
    """ Generates a random location for the amino acid to be placed """

    # Ways the next amino can go, up, down, left or right.
    amino_move = [(0,1), (0,-1), (-1,0), (1,0)]
    random.shuffle(amino_move)

    for move in amino_move:
        new_pos = (last_pos[0] + move[0], last_pos[1] + move[1])    

        if (0 <= new_pos[0] < protein_length and 0 <= new_pos[1] < protein_length
            and new_pos not in occupied_pos):
            return new_pos

def test_gen_location():
    """Test the gen_location function."""
    
    protein = 5
    protein_len = 5
    occ_pos = [(0, 0), (0, 1), (1, 1)]
    last_position = (1, 1)

    # Testing gen_location function
    new_position = gen_location(None, protein, protein_len, occ_pos, last_position)

    print(f"New position generated: {new_position}")

# Now call the test function
test_gen_location()

