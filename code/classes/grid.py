import csv
from code.classes import amino_cat
import random

class Grid():
    # width equals the length of the protein string 
    def __init__(self):
        self.amino_acids = {}
        self.locations = set()
        self.history = []
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def compute_score(self):
        """ 
        Computes the total stability score for the entire protein 
        by looping over the amino acids their bonds
        """
        # Set score to 0 to start count properly
        self.score = 0

        # Loop over each amino acid
        for i in range(len(self.amino_acids)):
    
            # The index of this location is the key in the dictionary with amino acids
            current_amino = self.amino_acids[i]

            # Check if there is a chance for a hydrogen bond
            if current_amino.text == 'H' or current_amino.text == 'C':
              
                # Find the next and previous amino acid object
                if i == len(self.amino_acids) - 1:
                    
                    # Skip assigning a value to next_amino for the last amino acid
                    continue
                next_amino = self.amino_acids[i + 1]

                # Initialize prev_amino as None
                prev_amino = None
                if i > 0:
                    # Skip assiging a value to prev_amino for the first amino acid
                    prev_amino = self.amino_acids[i - 1]

                # Check if it is not a covalent bond and if the amino acids are apart 1 step
                for amino in self.amino_acids.values():

                    # Check if there is a next amino or previous amino
                    if prev_amino and next_amino:
                        if amino.amino_id != next_amino.amino_id and amino.amino_id != prev_amino.amino_id and self.check_location(current_amino._location, amino._location):
                            self.score += self.calculate_bond_score(current_amino, amino)

        self.score = self.score
        return self.score

    def check_location(self, amino1: tuple, amino2: tuple) -> bool:
        """ This function returns true if the amino acids are adjacent """
        distance = abs(amino2[0] - amino1[0]) + abs(amino2[1] - amino1[1])

        return distance == 1    
    
    def calculate_bond_score(self, amino1, amino2) -> int:
        """ Calculates the bond score between two amino acids based on their types. """
        if amino1.text == "H" and amino2.text == "H":
            return -1
        elif (amino1.text == "H" and amino2.text == "C") or (amino1.text == "C" and amino2.text == "H"):
            return -1
        elif amino1.text == "C" and amino2.text == "C":
            return -5

        else:
            return 0

        
    def is_hydrogen_bond(self, amino1, amino2) -> bool:
        """ Checks if there is a hydrogen bond between two given amino acids """
        if self.calculate_bond_score(amino1, amino2) < 0:
            return True
        return False

    def is_valid(self, position):
        """ This function checks if the position is blocked by an amino acid """
        if position not in self.locations:
            return True
        return False

    def add_move(self, direction, index):
        """ This function checks what direction an amino acid was folded """
        # Check if it's the last amino acid in the protein
        if direction[0] != 0:
            self.history[index] = (direction[0])
        elif direction[1] == 1:
            self.history[index] = 2
        elif direction[1] == -1:
            self.history[index] = -2
        
    def load_input(self, protein_file):
        """ This function loads in a file with a protein and saves it as a string """
        with open(protein_file, 'r') as f:
            
            for protein in f:
                # Save protein name
                self.protein = protein
                self.max_grid_size = len(protein)

                for i, aminoacid in enumerate(protein):
                    # Create class object from amino acid, which is the key in the dict
                    if aminoacid == 'P':
                        amino = amino_cat.Amino("P", "blue", i)
                    elif aminoacid == 'H':
                        amino = amino_cat.Amino("H", "red", i)
                    else:
                        amino = amino_cat.Amino("C", "green", i)

                    # Create widget for amino acid visualisation as value in dict
                    self.amino_acids[amino.amino_id] = amino
                    self.history.append(0)

    def output_to_csv(self, filename):
        """ Creates a csv file with the folding score and all the moves made """
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['amino', 'fold'])

            # Write which amino acid was moved in the left column and the actual move in the right column                
            for i, amino in enumerate(self.amino_acids.values()):
                amino_text = amino.text
                move = self.history[i]
                writer.writerows([[amino_text, move]])
            writer.writerows([["score", self.score]])

    def display_rules(self):
        print("1 betekent een positieve stap in de eerste dimensie (X-as richting).")
        print("-1 betekent een negatieve stap in de eerste dimensie (X-as richting).")
        print("2 betekent een positieve stap in de tweede dimensie (Y-as richting).")
        print("-2 betekent een negatieve stap in de tweede dimensie (Y-as richting).")



    def getDiagional(self, amino):
        
        current_co = amino._location
        index = amino.amino_id

        # Searching for its neighbouring coordinates

        # Check if amino is the last 
        if (index + 1) == len(self.amino_acids):
            prev_amino = self.amino_acids[index - 1]
            coo_other = prev_amino._location
        # Check if amino is the first
        elif index == 0:
            next_amino = self.amino_acids[index + 1]
            coo_other = next_amino._location
        else:
            # Neither first or last amino
            next_or_prev = [index + 1, index - 1]
            # Random shuffle so that later on the pull move can be performed in either direction
            random.shuffle(next_or_prev)

            # Retrieving the neighbouring amino's
            next_amino = self.amino_acids[next_or_prev[0]]
            coo_other = next_amino._location

            prev_amino = self.amino_acids[next_or_prev[1]]
            coo_prev = prev_amino._location

            # Getting the diagonals if the amino_acid is in the chain

            # for previous amino 
            







    def is_diagonal(self, coord1, coord2):
        x1, y1 = coord1
        x2, y2 = coord2

        dx = abs(x1 - x2)
        dy = abs(y1 - y2)

        return dx == 1 and dy == 1 

