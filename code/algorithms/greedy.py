import random
from code.classes import grid

class Greedy:
    def __init__(self, grid):
        self.grid = grid
        self.flag = True
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.max_attempts = 10000

    def execute(self):
        """"Folds an entire protein by making local decisions to optimize the score"""
        
        while True:
            # Restart folding process
            location = (0, 0)
            self.grid.locations = set([(0,0)])

            # Keep connecting amino acids until the whole protein is folded
            for amino_id, amino in self.grid.amino_acids.items():
                attempts = 0
                min_score = float('inf')
                best_direction = None
                
                # Check that the location of the amino acid is not already in use
                while attempts < self.max_attempts:
                    direction = random.choice(self.directions)
                    next_pos = location[0] + direction[0], location[1] + direction[1]
                    
                    # Check if the location falls outside the grid size (AKA length of the protein)
                    if self.grid.is_valid(next_pos):
                        # Store the original location of the amino acid
                        original_location = amino._location

                        # Temporarily place the amino acid in the grid and calculate the score
                        amino.update_loc(next_pos)
                        self.grid.locations.add(next_pos)
                        score = self.grid.compute_score()

                        # Update score
                        if score < min_score:
                            min_score = score
                            best_direction = direction

                        # Remove the amino acid from the temporary location and put it back to its original location
                        amino.update_loc(original_location)
                        self.grid.locations.remove(next_pos)
                        break
                    
                    else:
                        attempts += 1
                        continue
                
                if attempts == self.max_attempts or best_direction is None:
                    # We are stuck, start over
                    break
                
                # Update the location of the amino acid to the best direction
                next_pos = location[0] + best_direction[0], location[1] + best_direction[1]
                amino.update_loc(next_pos)
                self.grid.locations.add(next_pos)
                location = next_pos

                # Check what the move was and add it to the history of moves
                if amino_id != self.grid.max_grid_size - 1:
                    self.grid.add_move(best_direction, amino_id)

            else:
                # If we completed the for loop (didn't "break" out of it), we are done
                self.flag = True
                return
