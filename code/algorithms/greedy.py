import random

class Greedy:
    def __init__(self, grid):
        self.grid = grid
        self.flag = True
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def execute(self):
        """"Folds an entire protein by making local decisions to optimize the score"""
        location = (0, 0)
        self.grid.amino_acids[0].update_loc(location)
        self.grid.locations.add(location)

        for amino_id, amino in list(self.grid.amino_acids.items())[1:]:
            # Initialize variables
            min_score = 0
            best_direction = None

            # Generating a randomized list of directions
            random_directions = self.directions[:]
            random.shuffle(random_directions)

            for direction in random_directions:
                next_pos = (location[0] + direction[0], location[1] + direction[1])
                
                if self.grid.is_valid(next_pos):
                    # Temporarily place the amino acid in the grid and calculate the score
                    amino.update_loc(next_pos)
                    self.grid.locations.add(next_pos)
                    score = self.grid.compute_score()

                    # Update score
                    if score < min_score:
                        min_score = score
                        best_direction = direction

                    # Remove the amino acid from the temporary location
                    amino.update_loc(None)
                    self.grid.locations.remove(next_pos)

            # If no direction was found that improves the score, take a random direction
            if best_direction is None:
                best_direction = random.choice(random_directions)

            # Look for next position and update postion
            next_pos = (location[0] + best_direction[0], location[1] + best_direction[1])
            amino.update_loc(next_pos)
            self.grid.locations.add(next_pos)
            location = next_pos

            # Add new best move
            self.grid.add_move(best_direction, amino_id)