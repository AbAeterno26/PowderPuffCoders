import math
from code.algorithms import randomise
import random 
import copy 


class SA(randomise.Random):
    def __init__(self, grid, cooling='linear', alpha=0.4, rate_of_decrease=0.95, initial_temp=90, final_temp=.1):
        self.grid = grid
        self.initial_temp = initial_temp
        self.cooling = cooling
        self.final_temp = final_temp
        self.alpha = alpha
        self.rate_of_decrease = rate_of_decrease
        self.x = 0

    def execute(self): 
        """Executes the Simulated Annealing algorithm for the given protein. Returns the updated grid object, where 
        the protein folding configuration is saved within the amino_acids dictionary."""

        k = 0
        current_temp = self.initial_temp
        
        # Creating an initial state using the randomise algorithm 
        super().execute()
        
        current_configuration = self.grid
        current_score = self.grid.compute_score()
        
        # Setting the best values equal to the current ones 
        self.best_grid = current_configuration
        best_score = current_score
        
        while current_temp > self.final_temp:
            # Keeping track of iterations
            k += 1

            # Making a copy of the grid object
            self.new_protein_obj = copy.deepcopy(current_configuration)

            # Extracting the dictionary with all protein information 
            new_protein_dict = self.new_protein_obj.amino_acids

            # Executing the pullmove to create a different configuration 
            self.pullMove(new_protein_dict)

            # Calculate the score of the new ordered dictionary (protein)
            new_score = self.new_protein_obj.compute_score()
            score_diff = abs(new_score - current_score)

            if score_diff > self.x:
                # Calculate the acceptance probability based on the difference in score and current temperature
                acceptance_probability = math.exp((-score_diff) / current_temp)
                acceptance_probability = round(acceptance_probability, 2)

                # Also giving worse configuration a chance of acceptance 
                if random.random() > acceptance_probability:
                    current_configuration = self.new_protein_obj
                    current_score = new_score

                    # If the new configuration has a higher score, update the best configuration
                    if current_score < best_score:
                        best_score = current_score
                        self.best_grid = current_configuration

            # Updating the temperature according to the cooling schedule 
            if self.cooling == 'exponential':
                current_temp = self.initial_temperature * self.alpha**k
            if self.cooling == 'logarithmic':
                current_temp = self.initial_temperature / math.log(k+1)
            if self.cooling == 'linear':
                current_temp *= self.rate_of_decrease 
        
    def get_best_configuration(self):
        return self.best_grid
    
    def pullMove(self, new_protein_dict):
        """Updates the dictionary location values of the new_protein (grid)object.
        In protein folding, pull moves involve moving an amino acid to a nearby unoccupied 
        diagonal position."""

        amino = random.choice(new_protein_dict)
        coordinates = self.new_protein_obj.get_valid_diagonals(amino)

        while not coordinates:
            amino = random.choice(new_protein_dict)
            diagonals = self.new_protein_obj.get_valid_diagonals(amino)
            new_location = tuple(random.choice(diagonals))
            amino._location = new_location         

        return new_protein_dict






        



   


