import copy


class DepthFirstSearch:
    def __init__(self, grid):
        self.grid = grid
        self.solutions = set()

    def fold_protein(self):
        """ Executes the depth-first search algorithm to fold the protein. """
        self.solutions = set()  # Reset the solutions
        self.depth_first_search()

    def depth_first_search(self):
        """
        Recursive function that performs the depth-first search by exploring
        possible moves and backtracking when necessary.
        """

        # Right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        location = (0, 0)

        while True:
            # Check if all amino acids have been placed
            if len(self.grid.amino_acids) == self.grid.max_grid_size:
                break
            
            # Try out all possible moves for all amino acids
            for amino_id, amino in self.grid.amino_acids.items():
                for direction in directions:
                    next_pos = location[0] + direction[0], location[1] + direction[1]

                    # Check if the location falls outside the grid size (AKA length of the protein)
                    if self.grid.is_valid(next_pos):
                        # Create a copy of the grid object
                        grid_copy = copy.deepcopy(self.grid)

                        # Update the location of the amino acid in the copied grid
                        amino_copy = grid_copy.amino_acids[amino_id]
                        amino_copy.update_loc(next_pos)

                        # Add the updated location to the set of locations of all amino acids and history
                        grid_copy.locations.add(amino_copy._location)

                        # Check what the move was and add it to the history of moves
                        if amino_id != grid_copy.max_grid_size - 1:
                            grid_copy.add_move(direction, amino_id)
                        
                    self.solutions.add(grid_copy)
                    self.depth_first_search()