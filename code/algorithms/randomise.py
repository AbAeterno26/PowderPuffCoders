import random


def fold_protein(amino_acids: dict):
    """ Folds an entire protein by generating random directions """
    # Right, left, down, up
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    max_grid_size = len(amino_acids)
    used_pos = set()
    last_pos = (0, 0)
    
    # Keep connecting amino acids until the whole protein is folded
    for amino in amino_acids:
        # Check that the location of the amino acid is not already in use
        while True:
            direction = random.choice(directions)
            next_pos = last_pos[0] + direction[0], last_pos[1] + direction[1]

            # Check if the location falls outside the grid size (AKA length of the protein)
            # IN FUNCTIE ZETTEN!! check if valid protein fold
            if (0 <= next_pos[0] < max_grid_size) and (0 <= next_pos[1] < max_grid_size) and next_pos not in used_pos:
                break
        
        # Update the location of the amino acid
        # IN FUNCTIE!!
        amino.update_loc(next_pos)

        # Update the last position for the next amino acid and add to in use locations
        last_pos = next_pos
        used_pos.add(last_pos)
