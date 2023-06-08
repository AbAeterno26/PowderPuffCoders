from code.classes import grid
from sys import argv


if __name__ == "__main__":

    if len(argv) == 1:
        print("Usage: python main.py [protein]")
        exit(1)
    
    # Loading the protein
    protein_file = argv[1]
    with open(protein_file) as f:
        for protein in f:
            print(f"The loaded protein is: {protein}")
    
        # Loading and printing the grid
        grid_obj = grid.Grid(len(protein))
        grid_obj.print_grid()