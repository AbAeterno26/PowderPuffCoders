import plotly
import plotly.graph_objs as go
from plotly.offline import plot
import plotly.express as px

class Visualize():
    def __init__(self, grid):
        self.grid = grid

    def fold_amino_scatter(self, x_values_amino, y_values_amino, text, color):
        fold_text = go.Scatter(
            x=x_values_amino,
            y=y_values_amino,
            name=text,
            mode="markers",
            marker=dict(
                size=14,
                color=color,
            ),
            showlegend=True,
        )
        return fold_text

    def visualize_2D(self):
        amino_acids = list(self.grid.amino_acids.values())

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

        fold_H = self.fold_amino_scatter(x_values_H, y_values_H, 'H', 'red')
        fold_P = self.fold_amino_scatter(x_values_P, y_values_P, 'P', 'blue')
        fold_C = self.fold_amino_scatter(x_values_C, y_values_C, 'C', 'green')

        fold_lines = []

        # Draw covalent bonds
        for i in range(len(amino_acids)-1):
            fold_lines.append(go.Scatter(x=[amino_acids[i]._location[0], amino_acids[i+1]._location[0]], 
                                          y=[amino_acids[i]._location[1], amino_acids[i+1]._location[1]], 
                                          mode='lines', 
                                          line=dict(color='black', width=1), 
                                          showlegend=False))

        # Draw hydrogen bonds
        for i in range(len(amino_acids)):
            for j in range(i+2, len(amino_acids)):
                if self.grid.check_location(amino_acids[i]._location, amino_acids[j]._location):
                    if self.grid.is_hydrogen_bond(amino_acids[i], amino_acids[j]):
                        fold_lines.append(go.Scatter(x=[amino_acids[i]._location[0], amino_acids[j]._location[0]], 
                                                     y=[amino_acids[i]._location[1], amino_acids[j]._location[1]], 
                                                     mode='lines', 
                                                     line=dict(color='blue', dash='dot', width=2), 
                                                     showlegend=False))

        layout = dict(
            title=f'Protein fold with a score of {self.grid.score}',
            xaxis=dict(
                showgrid=True,
                zeroline=True,
                showline=True,
                mirror='all',
                ticks='',
                showticklabels=False,
            ),
            yaxis=dict(
                showgrid=True,
                zeroline=True,
                showline=True,
                mirror='all',
                ticks='',
                showticklabels=False,
            ),
            showlegend=True,
        )

        fig = go.Figure(data=fold_lines+[fold_H, fold_P, fold_C], layout=layout)
        fig.update_xaxes(dtick=1)
        fig.update_yaxes(dtick=1)
        fig.update_layout(
            autosize=False,
            width = 800,
            height = 800,
            xaxis=dict(
                scaleanchor="y",
            )
        )

        fig.show()
        # plotly.io.write_image(fig, 'data/output/random/graphs/amino_plotly.pdf', format='pdf')
