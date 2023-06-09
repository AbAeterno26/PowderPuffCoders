import random

def add_bond(self, amino, protein: int):
    """ Generates a random location for the amino acid to be placed """
    # self.bonds.append(amino)

    # Generate random location for the amino acid to be placed
    row = random.randint([0, protein])
    col = random.randint([0, protein])

    return row, col

