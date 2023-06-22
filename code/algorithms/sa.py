import math
from code.algorithms import randomise
import random 


class SA(randomise.Random):
    # eventueel alpha ook nog meegeven als parameter
    # ook variabelen initial temp and final temp mogelijk meegeven om meer dynamiek te creeeren 
    def __init__(self, grid_obj):
        self.grid_obj = grid_obj 
        # self.cooling = cooling 
   
   
    def fold_protein(self):
        initial_temp = 90
        final_temp = 0.1
        """This function folds the protein according to the Simulated Annealing algorithm."""

        # Setting the current temperature equal to the initialized temperature 
        current_temp = initial_temp

        # Creating an initial state using the randomise algorithm 
        solution = super().fold_protein()
        # print(f'intial_state is {initial_state}')
        
        # Computing the score of the initial state 
        best_score = super().compute_score()
        # print(f'score is {score}')

        while current_temp > final_temp:
            print(f'current_temp {current_temp}')

            # Create a new protein configuration 
            new_protein_fold = super().fold_protein()
            # print(f'new_protein_fold is {new_protein_fold}')

            # Computing the score of the new state 
            new_score = super().compute_score()
            # print(f'new_score is {new_score}')

            #Calculate the score difference 
            score_diff = abs(abs(best_score) - abs(new_score))

            # Computing the current temperature 
            current_temp = initial_temp / float(i + 1)

            # If this new configuration has a better stability, accept it:
            if new_score < best_score: ###checken of dit klopt!!###
                acceptance_probability = 1
            # If this new configuration is not better, accept it with a probability related to the cooling schedule of choice
            else:
                acceptance_probability = math.exp((score_diff)/current_temp)
                
            if acceptance_probability > random.random(): 
                solution = new_protein_fold
                best_score = new_score

            print(f'solution{solution}, best score{best_score}')

             # Updating the initial temperature 

### NOTES ###
# calculate metropolis acceptance criterion
# metropolis = exp(-diff / t)
# deepcopy?? 
# different cooling schedules???
        


            # temperature is acceptance probability: linear / hyperbolic cooling schedule
            # if the cooling schedule is linear
            # if COOL is "linear":
            #     # temperature decreases linear
            #     temp = float(ITER - i)
            # # if cooling schedule is hyperbolic
            # elif COOL is "hyperbolic":
            #     # temperature decreases hyperbolic
            #     temp = ITER / i






    # def get_new_protein(self):
    #     super().fold_protein()
        
    # def compute_score_SA(self):
    #     super().compute_score()


