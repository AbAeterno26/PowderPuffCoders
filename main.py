from code.classes import grid
from code.algorithms import randomise
from code.algorithms import sa
from code.algorithms import depth_first
from code.visualizations import visualize
import matplotlib.pyplot as plt
from sys import argv
import seaborn as sns


def run(protein_file, iterations=100, algorithm="random", rules=False, show_vis=False):
    # The score of each folding of a protein
    scores = []
    input_file = protein_file.split('/')[2].strip('.txt')

    for i in range(iterations):
        # Create grid object
        grid_obj = grid.Grid()

        # Load in the nodes (AKA aminoacids)
        grid_obj.load_input(protein_file)
    
        # Call an algorithm to solve the protein folding        
        algorithm = algorithm.lower()
        if algorithm == "random":
            algorithm_obj = randomise.Random(grid_obj)
        elif algorithm == "sa":
            algorithm_obj = sa.SA(grid_obj)
        elif algorithm == "depth":
            algorithm_obj = depth_first.DepthFirstSearch(grid_obj)

        algorithm_obj.execute()

        # Get the modified grid object from simulated annealing
        if algorithm == "sa":
            grid_obj = algorithm_obj.get_best_configuration()

        # Compute the score for the folding of the protein
        grid_obj.compute_score()
        scores.append(grid_obj.score)
        
        # Visualize the protein folding
        if show_vis:
            vis = visualize.Visualize(grid_obj)
            vis.visualize_2D()

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

run(protein_file, iterations=1, algorithm='depth')
