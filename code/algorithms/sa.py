# import math
# from code.classes import grid 

# class SA(Random):
#     # eventueel alpha ook nog meegeven als parameter
#     # ook variabelen initial temp and final temp mogelijk meegeven om meer dynamiek te creeeren 
#     def __init__(self, grid_obj, cooling):
#         self.grid_obj = grid_obj # == grid object 
#         self.cooling = cooling 
#         initial_temp = 90
#         final_temp = .1
#         alpha = 0.01

#         # Setting the current temperature equal to the initialized temperature 
#         current_temp = initial_temp

#         current_state = new_protein
#         solution = current_state
    
        
#     def fold_protein(self):

#         ### Doorgeven van het grid_obj??? ###

        
#         # Creating an initial state (using randomise)
#         initial_state = self.grid_obj.get_new_protein()
#         # Computing the score of the initial state 
#         score = self.grid_obj.compute_score()

#         while current_temp > final_temp:

#             # Initialize a new grid object each iteration 
#             # it is a random fold of the same protein file each time 
#             new_grid_obj = grid.Grid()

#             # Create a new protein configuration 
#             new_protein_fold = get_new_protein(self.new_grid_obj)
#             new_score = compute_score_SA(self.new_grid_obj)

#             initial_state = new_protein_fold
#             score = new_score

#             # If this new configuration has a better stability, accept it:
#             if new_score < score:
#                 solution = new_protein_fold
#             # If this new configuration is not better, accept it with a probability related to the cooling schedule of choice
#             else:
#                 # if random.uniform(0, 1) < math.exp()



#     def get_new_protein(self):
#         super().fold_protein()
        

#     def compute_score_SA(self):
#         super().compute_score()
