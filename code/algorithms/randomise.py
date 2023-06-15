import random

last_pos = [0, 0]
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up
used_pos = [last_pos]

def gen_location(amino_acids):

    max_grid_size = len(amino_acids)

    for amino in amino_acids:

    while True:
        direction = random.choice(directions)
        next_pos = [last_pos[0] + direction[0], last_pos[1] + direction[1]]

        if (0 <= next_pos[0] < max_grid_size) and \
           (0 <= next_pos[1] < max_grid_size) and \
           next_pos not in used_pos:
            break

    used_pos.append(next_pos)
    last_pos = next_pos
    row = last_pos[0]
    column = last_pos[1]

    return row, column
