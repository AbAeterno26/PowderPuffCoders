import csv
import tkinter as tk
from code.classes import amino_cat


class Grid():
    # width equals the length of the protein string 
    def __init__(self):
        self.amino_acids = {}
        self.history = []
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.locations = []

    def compute_score(self) -> int:
        """ 
        Computes the total stability score for the entire protein 
        by looping over the amino acids their bonds
        """
        # Set score to 0 to start count properly
        self.score = 0

        # Looping over each amino_acid
        for i in range(len(self.locations)):
            # De indexen van deze lijst komen overeen met de keys van de amino_acids dictionary
            # Voor elk aminozuur kijken naar alle aminozuren, is het een previous of next
            for i in range(len(self.locations)):
                # First check: is this an H
                if self.amino_acids[i].text == 'H':
                    if i < (len(self.amino_acids) - 1): 
                        next_amino = self.amino_acids[i + 1]
                    if > 0:
                        previous_amino = next_amino = self.amino_acids[i - 1]

            # Find location of previous amino_acid


            print(f"object: {self.amino_acids[i].text}")
            
        

        # Loop over dictionary with id as key and amino object as value
        # for amino_id, amino in self.amino_acids.items():
        #     print(f"id: {amino_id}")
        #     print(f"object: {amino}")

        #     # Get location of the current amino acid
        #     location = amino._location
        #     print(f"location: {location}")

        #     # Check if the current amino acid is an H or C
        #     if amino.text == 'H' or amino.text == 'C':
        #         # Check 

        # for location, amino_acid in self.amino_locations.items():
        #     print(f"Checking amino acid at {location} with type {amino_acid.text}")
        #     for dx, dy in self.directions:
        #         neighbour_location = (location[0] + dx, location[1] + dy)
        #         neighbour_amino = self.amino_locations.get(neighbour_location)
        #         if neighbour_amino and neighbour_amino.text != "P" and amino_acid.text != "P":
        #             bond_score = self.calculate_bond_score(amino_acid, neighbour_amino)
        #             print(f"Bond score with neighbour at {neighbour_location} is {bond_score}")
        #             self.score += bond_score

        # print(f"THE SCORE IS: {self.score}")
    
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
        if position not in used_pos:
            return True
        return False

    def load_input(self, protein_file):
        """ This function loads in a file with a protein and returns it as a string """
        with open(protein_file, 'r') as f:
            for protein in f:
                # Save protein name
                self.protein = protein
                self.max_grid_size = len(protein)
                
                # Create interface object to visualize in Tkinter
                # interface = tk.Tk()

                for i, aminoacid in enumerate(protein):
                    # Create class object from amino acid, which is the key in the dict
                    if aminoacid == 'P':
                        amino = amino_cat.Amino("P", "blue", i)
                    elif aminoacid == 'H':
                        amino = amino_cat.Amino("H", "red", i)
                    else:
                        amino = amino_cat.Amino("C", "green", i)

                    # Create widget for amino acid visualisation as value in dict
                    # amino_acid_label = tk.Label(interface, text=amino.text, bg=amino.color, width=3, height=3)
                    self.amino_acids[amino.amino_id] = amino
                    

    def output_to_csv(self, filename):
        """Creates a csv file with each amino acid with its corresponding folding score."""
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['amino', 'fold'])

            # Write which amino acid was moved in the left column and the actual move in the right column                
            for i, amino in enumerate(self.amino_acids.values()):
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
