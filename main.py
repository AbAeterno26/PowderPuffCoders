from code.classes import grid

from code.algorithms import randomise
from code.visualizations import visualize
from sys import argv
import tkinter as tk


def run(protein_file, iterations=100, algorithm=randomise, rules=False, show_vis=False):
    for i in range(iterations):
        # Create grid object
        grid_obj = grid.Grid()

        # Load in the nodes (AKA aminoacids)
        grid_obj.load_input(protein_file)
    
        # Call an algorithm to solve the protein folding
        algorithm.fold_protein(grid_obj)

        # Print the grid of the entire protein
        if show_vis:
            visualize.plot_grid(grid_obj.amino_acids)

        # Compute the score for the folding of the protein
        grid_obj.compute_score()

        # Save output to a CSV file
        input_file = protein_file.split('/')[2].strip('.txt')
        filename = f"data/output/{input_file}_{i}.csv"
        grid_obj.output_to_csv(filename)

    # Display rules if requested
    if rules:
        grid_obj.display_rules()

if __name__ == "__main__":
    # Check for the correct command line input
    if len(argv) == 1:
        print("Usage: python main.py [data/input/protein.txt]")
        exit(1)
    
    protein_file = argv[1]

    run(protein_file, iterations=10)