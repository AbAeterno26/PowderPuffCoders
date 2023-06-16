from code.classes import grid

from code.algorithms import randomise
from code.visualizations import visualize
from sys import argv
import tkinter as tk
import pandas as pd
import seaborn as sns
from collections import Counter


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

    # Create grid object
    grid_obj = grid.Grid()

    # Load in the nodes (AKA aminoacids)
    grid_obj.load_input(protein_file)

    # Call an algorithm to solve the protein folding
    randomise.fold_protein(grid_obj)

    # Print the grid of the entire protein
    visualize.plot_grid(grid_obj.amino_acids)

    # Compute the score for the folding of the protein
    grid_obj.compute_score()

    grid_obj.output_to_csv(protein_file)

    grid_obj.display_rules()


def plot_development():
    """This function creates a histogram to plot all the achieved scores (x-axis) for a specified algorithm that is 
    applied and their occurences."""

    scores = []

    # Loop over alle csv files in de output map
    for csv in data/output:
        # amino_csv = sns.load_dataset(csv)
        amino_csv = pd.read_csv(csv)
        score = amino_csv[amino][-1] 
        scores.append(score)
    
    # occurences = Counter(scores)
    # df = pd.DataFrame({'counts':occurences})
    # x-axis - all achieved scores
    # y-axis - how many times was this score achieved

    sns.histplot(data=scores, x="scores", kde=True)
    
run(protein_file, iterations=10)
