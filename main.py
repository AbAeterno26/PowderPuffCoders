from code.classes import grid

from code.algorithms import randomise
from code.visualizations import visualize
from sys import argv
import tkinter as tk


if __name__ == "__main__":
    # Check for the correct command line input
    if len(argv) == 1:
        print("Usage: python main.py [data/input/protein.txt]")
        exit(1)
    
    protein_file = argv[1]

    # Create grid object
    grid_obj = grid.Grid()

    # Load in the nodes (AKA aminoacids)
    grid_obj.load_input(protein_file)

    # Call an algorithm to solve the protein folding
    randomise.fold_protein(grid_obj.amino_acids)

    # Print the grid of the entire protein
    visualize.plot_grid(grid_obj.amino_acids)

    # Compute the score for the folding of the protein
    grid_obj.compute_score()

    grid_obj.output_to_csv(protein_file)

    grid_obj.display_rules()
       
