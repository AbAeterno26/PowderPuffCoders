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
        
        self.score = 0

        for location, amino_acid in self.amino_locations.items():
            for x_way, y_way in self.directions:
                location_amino = (location[0] + x_way, location[1] + y_way)
                next_amino = self.amino_locations.get(location_amino)

                
    


    # def compute_score(self) -> int:
    #     """ 
    #     Computes the total stability score for the entire protein 
    #     by looping over the amino acids their bonds
    #     """
    #     self.score = 0
    #     aminos_list = list(self.amino_acids.keys())
    #     amino_loc_list = list(self.amino_locations.keys()
    #                           )
    #     for i, (location, amino) in enumerate(self.amino_locations.items()):
    #         # Check if the current amino is Hydrofoob
    #         if amino.text == "H":
    #             location_above = (location[0], location[1] + 1)
    #             location_below = (location[0], location[1] - 1)
    #             location_right = (location[0] + 1, location[1])
    #             location_left = (location[0] - 1, location[1])
                
    #             # Add the bond to history of moves starting from the second amino acid
    #             next_amino = aminos_list[i + 1]
    #             next_amino_location = amino_loc_list[i + 1]
                
    #             if next_amino != None and i > 0:
    #                 location_next_amino = self.amino_locations[i + 1]
    #                 if location_next_amino == location_above:
    #                     self.history.append("2")
    #                 elif location_next_amino == location_below:
    #                     self.history.append("-2")
    #                 elif location_next_amino == location_right:
    #                     self.history.append("1")
    #                 elif location_next_amino == location_left:
    #                     self.history.append("-1")

    #             # Check if the amino acid has four neighbours
    #             if location_above in self.amino_locations and location_below in self.amino_locations \
    #             and location_right in self.amino_locations and location_left in self.amino_locations:
                    
    #                 # Add -1 to the total score if one of the neighbours is also H
    #                 if self.amino_locations[location_above].text == "H":
    #                     self.score -= 1
    #                 elif self.amino_locations[location_below].text == "H":
    #                     self.score -= 1
    #                 elif self.amino_locations[location_right].text == "H":
    #                     self.score -= 1
    #                 elif self.amino_locations[location_left].text == "H":
    #                     self.score -= 1

    #     return self.score
    
    def is_valid(self, position):
        """This function checks if the position of the amino acid is not already occupied and does not fall outside of the grid."""
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
                        pass

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