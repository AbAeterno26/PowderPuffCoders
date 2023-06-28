from code.classes import grid
from code.algorithms import randomise, sa, depth_first, breadth_first, greedy
from code.visualizations import visualize
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from sys import argv
import seaborn as sns
import time


def run(protein_file, iterations=100, algorithm="random", rules=False, show_vis=False, save=False):
    # The score of each folding of a protein
    scores = []
    input_file = protein_file.split('/')[2].strip('.txt')

    print(f"{input_file} is running")

    # Algorithm starts running
    start = time.time()

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
        elif algorithm == "breadth":
            algorithm_obj = breadth_first.BreadthFirstSearch(grid_obj)
        elif algorithm == "greedy":
            algorithm_obj = greedy.Greedy(grid_obj)
        
        algorithm_obj.execute()

        if algorithm_obj.flag:
            if algorithm == "random" or algorithm == "greedy":
            # Compute the score for the folding of the protein
                grid_obj.compute_score()
                scores.append(grid_obj.score)
            elif algorithm_obj.best_grid:
                # Get the grid with the best score
                grid_obj = algorithm_obj.get_best_configuration()
                scores.append(grid_obj.score)
        
    # Visualize the protein folding
    if show_vis:
        vis = visualize.Visualize(grid_obj, save, algorithm)
        vis.visualize_2D()
    
        # Save output to a CSV file
        # filename = f"data/output/{algorithm}/scores/{input_file}_{i}.csv"
    #     # grid_obj.output_to_csv(filename)
    filename_exp = f"data/output/{algorithm}/scores/{input_file}.csv"
    grid_obj.output_scores_csv(filename_exp, input_file, scores)
    
    # Algorithm is done running
    end = time.time()
    duration = end - start
    print(f"Duration running {iterations} iterations:\t{duration} s")
    # Plot histogram of the scores for a specified protein
    # path_to_file = f"data/output/{algorithm}/graphs/{input_file}"
    # title = f"{algorithm} - {iterations} iterations"
    # plot_hist(scores, path_to_file, title)

    # Display rules if requested
    if rules:
        grid_obj.display_rules()
    

def plot_hist(scores, filename, title):
    """
    This function plots a histogram of all the achieved scores (x-axis)
    for a specified algorithm that is applied and their occurences (y-axis).
    """
    fig, ax = plt.subplots()
    sns.histplot(scores, ax=ax)
    ax.set_title(title, fontsize=20, weight='bold')
    ax.set_xlabel('Score')
    ax.set_ylabel('Iterations')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    fig.savefig(f"{filename}.png", bbox_inches='tight')
    # plt.show()


if __name__ == "__main__":
    # Check for the correct command line input
    if len(argv) == 1:
        print("Usage: python main.py [protein] (algorithm)")
        exit(1)
    
    filename = argv[1]
    protein_file = f"data/input/{filename}.txt"
    algorithm = argv[2]

    # Run experiment for specified algorithm
    run(protein_file, iterations=10, algorithm=algorithm)

# if __name__ == "__main__":
#     # List of protein files
#     protein_files = ['amino1', 'amino2', 'amino3', 'amino4', 'amino5', 'amino6', 'amino7', 'amino8', 'amino9']
    
    # Run experiment for specified algorithm
    run(protein_file, iterations=100000)