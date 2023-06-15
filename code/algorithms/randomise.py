import random
def fold_protein(grid):
    """ Folds an entire protein by generating random directions """
    # Right, left, down, up
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    used_pos = set()
    last_pos = (0, 0)
    
    # Keep connecting amino acids until the whole protein is folded
    for amino in grid.amino_acids:
        random.shuffle(directions) # shuffle the directions 
        for direction in directions:
            next_pos = (last_pos[0] + direction[0], last_pos[1] + direction[1])

            # Check if the location falls outside the grid size (AKA length of the protein)
            if grid.is_valid(next_pos, used_pos):
                # Update the location of the amino acid
                amino.update_loc(next_pos)

                # Update the last position for the next amino acid and add to in use locations
                last_pos = next_pos
                used_pos.add(last_pos)
                break
        else:
            raise ValueError("No valid moves for current amino acid.")
