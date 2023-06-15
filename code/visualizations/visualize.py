import tkinter as tk

def plot_grid(amino_acids: dict):
    """ Loops over the amino acids and plots the protein in a grid """
    grid = tk.Tk()

    for amino, label in amino_acids.items():
        label.grid(row=amino._location[0], column=amino._location[1])

    return grid.mainloop()