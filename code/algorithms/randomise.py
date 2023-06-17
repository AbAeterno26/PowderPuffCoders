import random


def fold_protein(grid):
    """ Folds an entire protein by generating random directions """
    # Right, left, down, up
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    used_pos = set()
    
    # Keep connecting amino acids until the whole protein is folded
    for amino_id, amino in grid.amino_acids.items():
        location = amino._location

        # Check that the location of the amino acid is not already in use
        while True:
            direction = random.choice(directions)
            next_pos = location[0] + direction[0], location[1] + direction[1]
            
            # Check if the location falls outside the grid size (AKA length of the protein)
            if grid.is_valid(next_pos, used_pos):
                # Update the location of the amino acid
                amino.update_loc(next_pos)
                
                # Add position to used locations
                used_pos.add(next_pos)
                break
            
            location = next_pos

        # Check what the move was and add it to the history of moves
        if direction[0] != 0:
            grid.history.append(direction[0])
        elif direction[1] == 1:
            grid.history.append("2")
        elif direction[1] == -1:
            grid.history.append("-2")