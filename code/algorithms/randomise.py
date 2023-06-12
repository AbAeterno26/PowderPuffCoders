import random

def gen_location(protein_length):
    max_grid_size = protein_length

    # Generate a random row and column
    row = random.randint(0, max_grid_size - 1)
    column = random.randint(0, max_grid_size - 1)
    return row, column


