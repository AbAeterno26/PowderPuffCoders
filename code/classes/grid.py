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
        """ Adds the amino acid to the list of amino acids """
        self.bonds.append(amino)

    def check_grid(self):
        pass

    def print_grid(self):
        """ Prints the grid for one protein """
        pass
