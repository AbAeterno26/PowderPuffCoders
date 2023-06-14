import csv
import tkinter as tk
from code.classes import amino_cat


class Grid():
    # width equals the length of the protein string 
    def __init__(self):
        self.amino_acids = {}
        self.amino_locations = {}
        self.history = []

    def compute_score(self) -> int:
        """ 
        Computes the total stability score for the entire protein 
        by looping over the amino acids their bonds
        """
        

    def output_to_csv(self, protein_file):
        """Creates a csv file with each amino acid with its corresponding folding score."""
        # data/input/protein.txt
        filename = (protein_file.split('/')[2] + "_output").strip(".txt")
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['amino', 'fold'])

            # Write which amino acid was moved in the left column and the actual move in the right column                
            for i in range(1, len(self.amino_acids)):
                amino_text = self.amino_acids[i].text
                move = self.history[i - 1]
                writer.writerows([[amino_text, move]])

    def display_rules(self):
        print("1 betekent een positieve stap in de eerste dimensie (X-as richting).")
        print("-1 betekent een negatieve stap in de eerste dimensie (X-as richting).")
        print("2 betekent een positieve stap in de tweede dimensie (Y-as richting).")
        print("-2 betekent een negatieve stap in de tweede dimensie (Y-as richting).")