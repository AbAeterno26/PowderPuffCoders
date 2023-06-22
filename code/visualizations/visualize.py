import plotly
import plotly.graph_objs as go
from plotly.offline import plot
import plotly.express as px


class Visualize():
    def __init__(self, grid):
        self.grid = grid

    def fold_amino_scatter(self, x_values_amino, y_values_amino, text, color):
        fold_text = go.Scatter(
            x = x_values_amino,
            y = y_values_amino,
            name = text,
            mode = "markers",
            marker = dict(
                size=14,
                color=color,
            ),
            showlegend=True,
        )
        return fold_text

    def visualize_2D(self):
        x_values = []
        y_values = []
        x_values_H = []
        y_values_H = []
        x_values_P = []
        y_values_P = []
        x_values_C = []
        y_values_C = []
        
        for amino in self.grid.amino_acids.values():
            x, y = amino._location
            x_values.append(x)
            y_values.append(y)
            if amino.text == 'H':
                x_values_H.append(x)
                y_values_H.append(y)
            elif amino.text == 'P':
                x_values_P.append(x)
                y_values_P.append(y)
            elif amino.text == 'C':
                x_values_C.append(x)
                y_values_C.append(y)
        
        fold_line = go.Scatter(
            x=x_values,
            y=y_values,
            name="protein string line",
            mode="lines",
            line=dict(
                color='black',
                width=1,
            ),
            showlegend=False,
        )

        # Separate scatter plots for each type of amino acid
        fold_H = self.fold_amino_scatter(x_values_H, y_values_H, 'H', 'red')
        fold_P = self.fold_amino_scatter(x_values_P, y_values_P, 'P', 'blue')
        fold_C = self.fold_amino_scatter(x_values_C, y_values_C, 'C', 'green')

        layout = dict(
            title='Protein fold - folding a protein with H, P, and C aminoacids',
            xaxis=dict(
                showgrid=True,
                zeroline=True,
            ),
            yaxis=dict(
                showgrid=True,
                zeroline=True,
            ),
            legend=dict(
                x=1,
                y=1

            ),
            plot_bgcolor='rgb(240, 230, 240)',
        )

        fig = go.Figure(data=[fold_line, fold_H, fold_P, fold_C], layout=layout)
        fig.update_xaxes(dtick=1)
        fig.update_yaxes(dtick=1)

        fig.show()
        # plotly.io.write_image(fig, 'data/output/random/graphs/file1.pdf', format='pdf')

