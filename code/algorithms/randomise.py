import random

def gen_location(self, amino, protein: int):
    """ Generates a random location for the amino acid to be placed """

    # Generate random location for the amino acid to be placed
    row = random.randint([0, protein])
    column = random.randint([0, protein])

    return row, column

