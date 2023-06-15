import csv
import tkinter as tk
from code.classes import amino_cat


class Grid():
    # width equals the length of the protein string 
    def __init__(self):
        self.amino_acids = {}
        self.max_grid_size = len(self.amino_acids)
        self.amino_locations = {}
        self.history = []
        self.directions[(0, 1), (0, -1), (1, 0), (-1, 0)]

    def compute_score(self) -> int:
        """ 
        Computes the total stability score for the entire protein 
        by looping over the amino acids their bonds
        """


    def calculate_bond_score(self, amino1, amino2) -> int:
        """
        Calculates the bond score between two amino acids based on their types.
        """
        if amino1.text == "H" and amino2.text == "H":
            return -1
        elif amino1.text == "H" and amino2.text == "C":
            return -1
        elif amino1.text == "C" and amino2.text == "H":
            return -1
        elif amino1.text == "C" and amino2.text == "C":
            return -5
        else:
            return 0
    
    def is_valid(self, position):
        if (0 <= position[0] < self.max_grid_size) and (0 <= position[1] < self.max_grid_size) and position not in used_pos:
            return True

    def load_input(self, protein_file):
        """ This function loads in a file with a protein and returns it as a string """
        with open(protein_file, 'r') as f:
            for protein in f:
                # Create interface object to visualize in Tkinter
                interface = tk.Tk()
                for aminoacid in protein:
                    # Create class object from amino acid, which is the key in the dict
                    if aminoacid == 'P':
                        amino = amino_cat.Amino("P", "blue")
                    elif aminoacid == 'H':
                        amino = amino_cat.Amino("H", "red")
                    else:
                        amino = amino_cat.Amino("C", "green")

                    # Create widget for amino acid visualisation as value in dict
                    amino_acid_label = tk.Label(interface, text=amino.text, bg=amino.color, width=3, height=3)
                    self.amino_acids[amino] = amino_acid_label

                    # Fill dictionary with amino acid location as key and the amino acid itself as value
                    self.amino_locations[(amino.row, amino.column)] = amino
        
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