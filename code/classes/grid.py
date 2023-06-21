import csv
import tkinter as tk
from code.classes import amino_cat
import plotly.graph_objs as go
from plotly.offline import plot

class Grid():
    # width equals the length of the protein string 
    def __init__(self):
        self.amino_acids = {}
        self.locations = []
        self.history = []
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def compute_score(self) -> float:
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
                    if amino != next_amino and amino != prev_amino and self.check_location(current_amino._location, amino._location):
                        self.score += self.calculate_bond_score(current_amino, amino)

        self.score /= 2

    def check_location(self, amino1: tuple, amino2: tuple) -> bool:
        """ This function returns true if the amino acids are adjacent """
        distance = abs(amino2[0] - amino1[0]) + abs(amino2[1] - amino1[1])

        return distance == 1
    
    def calculate_bond_score(self, amino1, amino2) -> int:
        """ Calculates the bond score between two amino acids based on their types. """
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
        """ This function checks if the position is blocked by an amino acid """
        if position not in used_pos:
            return True
        return False

    def add_move(self, direction, index):
        """ This function checks what direction an amino acid was folded """
        # Check if it's the last amino acid in the protein
        key_list = list(self.amino_acids.keys())
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

                    # Add amino acid to dictionary
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
                print(i)
                print(self.history)
                move = self.history[i]
                writer.writerows([[amino_text, move]])
            writer.writerows([["score", self.score]])

    def display_rules(self):
        # print("1 betekent een positieve stap in de eerste dimensie (X-as richting).")
        # print("-1 betekent een negatieve stap in de eerste dimensie (X-as richting).")
        # print("2 betekent een positieve stap in de tweede dimensie (Y-as richting).")
        # print("-2 betekent een negatieve stap in de tweede dimensie (Y-as richting).")
        pass

    def visualize_2D(self):
        x_values = []
        y_values = []
        color_array = []
        type_array = []

        color_dict = {
            "P": "blue",
            "H": "red",
            "C": "green"
        }

        for index, amino_acid in self.amino_acids.items():
            x, y = amino_acid._location
            x_values.append(x)
            y_values.append(y)
            type_array.append(amino_acid.text)
            color_array.append(color_dict[amino_acid.text])

        trace = go.Scatter(
            x=x_values,
            y=y_values,
            mode="lines+markers+text",
            text=type_array,
            marker=dict(
                size=8,
                color=color_array,
            ),
            line=dict(
                color='black',
                width=1,
            ),
            textfont=dict(
                family='sans serif',
                size=18,
                color='black'
            ),
            showlegend=False,
        )

        layout = dict(
            title='Algorithmic Protein Folding',
            xaxis=dict(
                gridcolor='rgb(255, 255, 255)',
                zerolinecolor='rgb(255, 255, 255)',
                showgrid=True,
                zeroline=False,
                ticks="",
                showticklabels=False,
                # backgroundcolor='rgb(230, 230,230)'
            ),
            yaxis=dict(
                gridcolor='rgb(255, 255, 255)',
                zerolinecolor='rgb(255, 255, 255)',
                showgrid=True,
                zeroline=False,
                ticks="",
                showticklabels=False,
                # backgroundcolor='rgb(230, 230,230)'
            ),
            plot_bgcolor='rgb(230, 230,230)',
        )

        fig = go.Figure(data=trace, layout=layout)
        plot(fig, filename="output.html")

    # Add this method to the Grid class, and call it when you want to visualize your protein
# grid.visualize_2D = visualize_2D
