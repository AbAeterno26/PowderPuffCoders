from code.classes import grid
from code.classes import p
from code.classes import h
from code.algorithms import randomise 
from sys import argv
import tkinter as tk 


def plot_grid():
    """ Loops over the amino acids and plots the protein in a grid """
    grid = tk.Tk()
    for amino_acid in amino_labels:
        amino_acid_label.grid(row=row, column=column)

        grid.mainloop()
    


if __name__ == "__main__":
    # Check for the correct command line input
    if len(argv) == 1:
        print("Usage: python main.py [protein]")
        exit(1)
    
    # Loading the protein
    protein_file = argv[1]
    with open(protein_file) as f:
        for protein in f:
<<<<<<< HEAD
            interface = tk.Tk()
            amino_labels = []
=======
>>>>>>> 555933fa1efef69ce943772a9197f6f5bbcb2b63
            print(f"The loaded protein is: {protein}")

            # Create grid object
<<<<<<< HEAD
            # grid_obj = grid.Grid(len(protein))
            grid_obj = grid.Grid()

=======
            grid_obj = grid.Grid(len(protein))
            
            amino_labels = []
>>>>>>> 555933fa1efef69ce943772a9197f6f5bbcb2b63
            for aminoacid in protein:
                # Call random algorithm to solve protein fold
                row, column = randomise.gen_location(len(protein))

                # Create class object from aminoacid
                if aminoacid == 'P':
                    amino = p.Polair(row, column)
                elif aminoacid == 'H':
                    amino = h.Hydrofoob(row, column)
                else:
                    #This is reserved for the C class
                    pass

                # Create widget for amino acid visualisation
                amino_acid_label = tk.Label(interface, text=amino.text, bg=amino.color, width=3, height=3)
                amino_labels.append(amino_acid_label)
                
                # Add amino acid to grid
                grid_obj.add_bond(amino)

        # Print the grid of the entire protein
<<<<<<< HEAD
        for label in amino_labels:
            label.interface(row=0, column=1)
        interface.mainloop()
=======
        plot_grid()
>>>>>>> 555933fa1efef69ce943772a9197f6f5bbcb2b63
