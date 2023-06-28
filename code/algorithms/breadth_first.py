import copy


class BreadthFirstSearch:
    def __init__(self, grid):
        self.grid = grid
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        self.best_score = float('inf')
        self.best_grid = None
    
    def execute(self):
        """Folds an entire protein using breadth-first search"""

        # Initialize the grid with the first amino acid placed
        self.grid.add_move((0, 0), 0)
        self.grid.locations.add((0, 0))
        
        self.stack = [(1, copy.deepcopy(self.grid))]

        while self.stack:
            current_amino_id, grid = self.stack.pop(0)

            # Check if we are at the end of the protein
            if current_amino_id == len(grid.amino_acids):
                score = grid.compute_score()
                
                # Check if the current score is better than the current best
                if score < self.best_score:
                    self.best_score = score
                    self.best_grid = grid

                    print(f'Found a configuration with score: {score}')
            else:
                # Iterate over the possible directions
                self.get_children(grid, current_amino_id)
        

    def get_children(self, grid, current_amino_id):
        """
        This function iterates over the possible directions
        and generates all the possible child states for the current amino acid
        """
        for direction in self.directions:
            current_pos = grid.amino_acids[current_amino_id - 1]._location
            next_pos = current_pos[0] + direction[0], current_pos[1] + direction[1]

            grid_child = copy.deepcopy(grid)
            current_amino = grid_child.amino_acids[current_amino_id]

            # Check if the next position is valid and not visited
            if grid_child.is_valid(next_pos):
                # Update the location of the amino acid
                current_amino.update_loc(next_pos)

                # Add position to used locations and visited set
                grid_child.locations.add(next_pos)

                # Add the move to the history of moves
                grid_child.add_move(direction, current_amino_id)

                # Add the next position to the stack
                self.stack.append((current_amino_id + 1, grid_child))

    def get_best_configuration(self):
        return self.best_grid