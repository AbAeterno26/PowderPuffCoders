from code.classes import grid
from code.algorithms import randomise
from code.algorithms import sa
# from code.visualizations import visualize_2D
from sys import argv
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objs as go
from plotly.offline import plot


def run(protein_file, iterations=100, algorithm="random", rules=False, show_vis=True):
    # The score of each folding of a protein
    scores = []
    input_file = protein_file.split('/')[2].strip('.txt')

    for i in range(iterations):
        # Create grid object
        grid_obj = grid.Grid()

        # Load in the nodes (AKA aminoacids)
        grid_obj.load_input(protein_file)
    
        # Call an algorithm to solve the protein folding
        # algorithm_obj = algorithm.Random(grid_obj)
        
        algorithm = algorithm.lower()
        if algorithm == "random":
            algorithm_obj = randomise.Random(grid_obj)
        elif algorithm == "sa":
            algorithm_obj = sa.SA(grid_obj)

        algorithm_obj.fold_protein()
        # Print the grid of the entire protein
        # Fold the protein
        algorithm_obj.fold_protein()

        # Visualize the protein folding
        if show_vis:
            grid_obj.visualize_2D()

        # Compute the score for the folding of the protein
        grid_obj.compute_score()
        # Compute the score for the folding of the protein
        grid_obj.compute_score()
        scores.append(grid_obj.score)

        # Save output to a CSV file
        filename = f"data/output/{algorithm}/scores/{input_file}_{i}.csv"
        grid_obj.output_to_csv(filename)

    # Plot histogram of the scores for a specified protein
    path_to_file = f"data/output/{algorithm}/graphs/{input_file}"
    title = f"{algorithm} - {iterations} iterations"
    plot_hist(scores, path_to_file, title, grid_obj.protein)

    # Display rules if requested
    if rules:
        grid_obj.display_rules()

if __name__ == "__main__":
    # Check for the correct command line input
    if len(argv) == 1:
        print("Usage: python main.py [protein]")
        exit(1)
    
    filename = argv[1]
    protein_file = f"data/input/{filename}.txt"
    
def plot_hist(scores, filename, title, protein):
    """
    This function plots a histogram of all all the achieved scores (x-axis)
    for a specified algorithm that is applied and their occurences (y-axis).
    """
    histplot = sns.histplot(scores, kde=True)
    plt.title(protein)
    fig = histplot.get_figure()
    fig.suptitle(title, fontsize=20, weight='bold')
    fig.savefig(f"{filename}.png", bbox_inches='tight')
    plt.show()

run(protein_file, iterations=1)
