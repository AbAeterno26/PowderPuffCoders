class Grid():
    def __init__(self, width):
        self.bonds = []
        self.width = width

    def compute_score(self):
        pass

    def add_bond(self, amino):
        self.bonds.append(amino)

    def check_grid(self):
        self.board = [['_' for i in range(self.width)] for j in range(self.width)]

    def print_grid(self):
        self.check_grid()
        print(self.board)
