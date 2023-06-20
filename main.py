from code.classes import grid
from code.algorithms import randomise
from code.algorithms import sa
from code.visualizations import visualize
from sys import argv
import seaborn as sns
import matplotlib.pyplot as plt


def run(protein_file, iterations=100, algorithm="random", rules=True, show_vis=False):
    # The score of each folding of a protein
    scores = []
    input_file = protein_file.split('/')[2].strip('.txt')

    for i in range(iterations):
        # Create grid object
        grid_obj = grid.Grid()

        # Load in the nodes (AKA aminoacids)
        grid_obj.load_input(protein_file)
        
        algorithm = algorithm.lower()
        if algorithm == "random":
            algorithm_obj = randomise.Random(grid_obj)
        elif algorithm == "sa":
            algorithm_obj = sa.SA(grid_obj)

        algorithm_obj.fold_protein()
        # Print the grid of the entire protein
        if show_vis:
            visualize.plot_grid(grid_obj.amino_acids)

        # Compute the score for the folding of the protein
        grid_obj.compute_score()
        scores.append(grid_obj.score)

        # Save output to a CSV file
        filename = f"data/output/{algorithm}/scores/{input_file}_{i}.csv"
        grid_obj.output_to_csv(filename)

    # Plot histogram of the scores for a specified protein
    # path_to_file = f"data/output/{algorithm}/graphs/{input_file}"
    # title = f"{algorithm} - {iterations} iterations"
    # plot_hist(scores, path_to_file, title, grid_obj.protein)

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
