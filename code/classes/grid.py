import csv
import tkinter as tk
from code.classes import amino_cat


class Grid():
    # width equals the length of the protein string 
    def __init__(self):
        self.amino_acids = {}
        self.amino_locations = {}
        self.history = []
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def compute_score(self) -> int:
        """ 
        Computes the total stability score for the entire protein 
        by looping over the amino acids their bonds
        """        
        self.score = 0

        for location, amino_acid in self.amino_locations.items():
            # Reset the number of neighbours to 0 for each amino acid
            neighbours = 0
            for x_way, y_way in self.directions:
                # Check if the current amino acid has four neighbours
                location_amino = (location[0] + x_way, location[1] + y_way)
                # print(location_amino)
                next_amino = self.amino_locations.get(location_amino)

                if next_amino != None:
                    neighbours += 1
            if neighbours == 4:
                self.score += self.calculate_bond_score(amino_acid, next_amino)
                print(f"THE SCORE IS: {self.score}")

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
    
    def is_valid(self, position, used_pos):
        if (0 <= position[0] < self.max_grid_size) and (0 <= position[1] < self.max_grid_size) and position not in used_pos:
            return True

    def load_input(self, protein_file):
        """ This function loads in a file with a protein and returns it as a string """
        with open(protein_file, 'r') as f:
            for protein in f:
                # Save protein name
                self.protein = protein
                
                self.max_grid_size = len(protein)
                # Create interface object to visualize in Tkinter
                interface = tk.Tk()
                amino_label = set()
                for aminoacid in protein:
                    # Create class object from amino acid, which is the key in the dict
                    if aminoacid == 'P':
                        amino = amino_cat.Amino("P", "blue")
                        print("YY")
                        amino_label = 'P'
                    elif aminoacid == 'H':
                        amino = amino_cat.Amino("H", "red")
                        amino_label = 'H'
                    else:
                        amino = amino_cat.Amino("C", "green")
                        amino_label = 'C'

                    # Create widget for amino acid visualisation as value in dict
                    amino_acid_label = tk.Label(interface, text=amino.text, bg=amino.color, width=3, height=3)
                self.amino_acids[amino] = amino_label
                print(self.amino_acids)
                self.max_grid_size = len(protein)

                    # Fill dictionary with amino acid location as key and the amino acid itself as value
                self.amino_locations[amino._location] = amino
        
    def output_to_csv(self, filename):
        """Creates a csv file with each amino acid with its corresponding folding score."""
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['amino', 'fold'])

            # Write which amino acid was moved in the left column and the actual move in the right column                
            for i, amino in enumerate(self.amino_acids):
                if i > 0:
                    amino_text = amino.text
                    move = self.history[i - 1]
                    writer.writerows([[amino_text, move]])
            writer.writerows([["score", self.score]])

    def display_rules(self):
        print("1 betekent een positieve stap in de eerste dimensie (X-as richting).")
        print("-1 betekent een negatieve stap in de eerste dimensie (X-as richting).")
        print("2 betekent een positieve stap in de tweede dimensie (Y-as richting).")
        print("-2 betekent een negatieve stap in de tweede dimensie (Y-as richting).")
