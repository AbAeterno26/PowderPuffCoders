class Grid():
    def __init__(self, width):
        self.bonds = []
        self.width = width

    def compute_score(self):
        pass

    def add_bond(self, amino):
        self.bonds.append(amino)

    def check_grid(self):
        for i in range(self.width):
            for j in range(self.width):
                self.board = ['_']

    def print_grid(self):
        pass
        # print(grid)