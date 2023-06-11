class Grid():
    # width equals the length of the protein string 
    def __init__(self, aminoacids: list):
        self.aminoacids = aminoacids
        self.bonds = []

    def compute_score(self) -> float:
        """ Computes the total stability score for the entire protein """
        # Loop over self.bonds and sum all the scores
        pass

    def add_bond(self, amino):
        """ Checks what the optimal location is for the amino acid to be placed and returns a row and column index """
        self.bonds.append(amino)

    def check_grid(self):
        # self.board = [['_' for i in range(self.width)] for j in range(self.width)]
        pass

    def print_grid(self):
        """ Prints the grid for one protein """
        # self.check_grid()
        # print(self.board)
        pass
