# import tkinter as tk

# def plot_grid(amino_acids: dict):
#     """ Loops over the amino acids and plots the protein in a grid """
#     grid = tk.Tk()

#     for amino, label in amino_acids.items():
#         print(f"amino is {amino}")
#         print(f"label is {label}")
#         label.grid(row=amino._location[0], column=amino._location[1])

#     return grid.mainloop()

import plotly.graph_objs as go
from plotly import plot
from code.classes import grid

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
            showbackground=True,
            zeroline=False,
            ticks="",
            showticklabels=False,
            backgroundcolor='rgb(230, 230,230)'
        ),
        yaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            zeroline=False,
            ticks="",
            showticklabels=False,
            backgroundcolor='rgb(230, 230,230)'
        ),
        plot_bgcolor='rgb(230, 230,230)',
    )

    fig = go.Figure(data=trace, layout=layout)
    plot(fig, filename="output.html")

# Add this method to the Grid class, and call it when you want to visualize your protein
grid.visualize_2D = visualize_2D
