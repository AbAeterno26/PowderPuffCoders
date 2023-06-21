class DepthFirstSearch:
    def __init__(self, grid):
        self.grid = grid
        self.solution_found = False
        self.solution = None
        
    def fold_protein(self):
        """ Executes the depth-first search algorithm to fold the protein. """
        self.solution_found = False
        self.solution = None
        self.depth_first_search()

    def depth_first_search(self):
        """
        Recursive function that performs the depth-first search by exploring
        possible moves and backtracking when necessary.
        """
        if self.is_goal_state():
            self.solution_found = True
            self.solution = self.grid.copy()
            return

        next_move = self.get_next_move()
        for move in next_move:
            if self.is_valid_move(move):
                self.apply_move(move)
                self.depth_first_search()
                if self.solution_found:
                    return
                self.undo_move(move)

    def is_valid_move(self, move):
        """ Checks whether a given move is valid within the current state of the protein. """
        location = self.grid.get_last_amino_acid_location()
        next_pos = location[0] + move[0], location[1] + move[1]
        return self.grid.is_valid(next_pos)

    def is_goal_state(self):
        """ Checks whether the folding process has reached the goal state. """
        return len(self.grid.amino_acids) == self.grid.max_grid_size

    def get_next_move(self):
        """ Determines the next move to be made in the folding process. """
        return [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def apply_move(self, move):
        """ Applies the given move to the current state of the protein. """
        last_amino_acid = self.grid.get_last_amino_acid()
        location = last_amino_acid._location
        next_pos = location[0] + move[0], location[1] + move[1]
        amino = self.grid.add_amino_acid(next_pos)
        self.grid.add_move(move, amino)

    def undo_move(self, move):
        """ Undoes the effects of the previous move, reverting the protein to its previous state. """
        self.grid.remove_last_amino_acid()
        self.grid.remove_last_move()
