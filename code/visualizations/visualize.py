import plotly.graph_objs as go
from plotly.offline import plot

class Visualize():
    def __init__(self, grid):
        self.grid = grid

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
            mode="lines+markers",
            text=type_array,
            marker=dict(
                size=10,
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
            ),
            yaxis=dict(
                gridcolor='rgb(255, 255, 255)',
                zerolinecolor='rgb(255, 255, 255)',
                showgrid=True,
                zeroline=False,
            ),
            plot_bgcolor='rgb(230, 230,230)',
        )

        fig = go.Figure(data=trace, layout=layout)
        plot(fig, filename="output.html")


    #  grid.visualize_2D = visualize_2D