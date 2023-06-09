from code.classes import grid
from code.classes import p
from code.classes import h
from code.algorithms import randomise 
from sys import argv
import tkinter as tk 


def plot_grid():
    """ Loops over the amino acids and plots the protein in a grid """
    


if __name__ == "__main__":
    # Check for the correct command line input
    if len(argv) == 1:
        print("Usage: python main.py [protein]")
        exit(1)
    
    # Loading the protein
    protein_file = argv[1]
    with open(protein_file) as f:
        for protein in f:
            amino_labels = []
            print(f"The loaded protein is: {protein}")
            # Create grid object
            grid_obj = grid.Grid(len(protein))

            for aminoacid in protein:
                row, column = randomise.gen_location(len(protein))

                #Create class object from aminoacid
                if aminoacid == 'P':
                    amino = p.Polair(row, column)
                elif aminoacid == 'H':
                    amino = h.Hydrofoob(row, column)
                else:
                    #This is reserved for the C class
                    pass

                # Call random algorithm to solve protein fold
                # Create widget for amino acid visualisation
                amino_acid_label = tk.Label(grid, text=amino.text, bg=amino.color, width=1, height=1)
                amino_labels.append(amino_acid_label)
                # Add amino acid to grid
                grid_obj.add_bond(amino)

        # Print the grid of the entire protein
        amino_acid_label.grid(row=row, column=column)

        grid.mainloop()
