import random

def gen_location(protein_length):
    grid_size = protein_length

    # Generate a random row and column
    row = random.randint(0, grid_size - 1)
    column = random.randint(0, grid_size - 1)
    return row, column


print(gen_location(5))


