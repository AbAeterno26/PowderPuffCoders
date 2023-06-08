from code.classes import grid
from sys import argv


if __name__ == "__main__":

    if len(argv) == 1:
        print("Usage: python main.py [aminoacid]")
        exit(1)
    
    # loading the amino acid
    aminoacid = argv[1]
    with open(aminoacid) as f:
        for line in f:
            print(f"The loaded amino acid is: {line}")
    
        # Loading and printing the grid
        grid_obj = grid.Grid(len(line))
        grid_obj.print_grid()