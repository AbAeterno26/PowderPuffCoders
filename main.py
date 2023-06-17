from code.classes import grid

from code.algorithms import randomise
from code.visualizations import visualize
from sys import argv
import tkinter as tk
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
import csv


def run(protein_file, iterations=100, algorithm=randomise, rules=False, show_vis=False):
    # The score of each folding of a protein
    scores = []

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
        scores.append(grid_obj.score)

        # Save output to a CSV file
        input_file = protein_file.split('/')[2].strip('.txt')
        filename = f"data/output/{input_file}_{i}.csv"
        grid_obj.output_to_csv(filename)

    # Plot histogram of the scores for a specified protein
    plot_hist(scores)

    # Display rules if requested
    if rules:
        grid_obj.display_rules()

if __name__ == "__main__":
    # Check for the correct command line input
    if len(argv) == 1:
        print("Usage: python main.py [protein]")
        exit(1)
    
    filename = argv[1]
    protein_file = f"data/input/{filename}.txt"

def plot_development(output):
    """
    This function plots a histogram of all all the achieved scores (x-axis)
    for a specified algorithm that is applied and their occurences (y-axis).
    """
    # Open each output file and extract the score
    scores = []
    for csv_file in output:
        with open(csv_file, "r", encoding="utf-8", errors="ignore") as f:
            final_line = f.readlines()[-1]
            score = float(final_line.split(',')[1].strip())
            scores.append(score)

    # Plot histogram
    sns.histplot(scores)
    plt.show()
    
def plot_hist(scores):
    """
    This function plots a histogram of all all the achieved scores (x-axis)
    for a specified algorithm that is applied and their occurences (y-axis).
    """
    sns.histplot(scores)
    plt.show()

run(protein_file, iterations=100)
