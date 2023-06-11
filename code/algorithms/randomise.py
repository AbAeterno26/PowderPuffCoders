import random

def gen_location(self, amino, protein: int, protein_length, occupied_pos, last_pos=(0,0)):
    """ Generates a random location for the amino acid to be placed """

    # Ways the next amino can go, up, down, left or right.
    amino_move = [(0,1), (0,-1), (-1,0), (1,0)]
    random.shuffle(amino_move)

    for move in amino_move:
        new_pos = (last_pos[0] + move[0], last_pos[1] + move[1])        

    # Generate random location for the amino acid to be placed
    row = random.randint([0, protein])
    column = random.randint([0, protein])

    return row, column

