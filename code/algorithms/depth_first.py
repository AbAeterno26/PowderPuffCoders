import random


class DepthFirstSearch:
    def __init__(self, grid):
        self.grid = grid

    def fold_protein(self):
        """Folds an entire protein using depth-first search"""

        # Initialize the stack with the starting position (0, 0)
        stack = [(0, 0)]
        visited = set([(0, 0)])

        while stack:
            current_pos = stack.pop()
            current_amino_id = len(visited) - 1
            current_amino = self.grid.amino_acids[current_amino_id]

            # Iterate over the possible directions in a random order
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            random.shuffle(directions)

            for direction in directions:
                next_pos = current_pos[0] + direction[0], current_pos[1] + direction[1]

                # Check if the next position is valid and not visited
                if self.grid.is_valid(next_pos) and next_pos not in visited:
                    # Update the location of the amino acid
                    current_amino.update_loc(next_pos)

                    # Add position to used locations and visited set
                    self.grid.locations.add(next_pos)
                    visited.add(next_pos)

                    # Add the move to the history of moves
                    self.grid.add_move(direction, current_amino_id)

                    # Add the next position to the stack
                    stack.append(next_pos)
                    break
