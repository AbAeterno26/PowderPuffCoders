import math
from code.algorithms import randomise
import random 
import copy 


class SA(randomise.Random):
    # eventueel alpha ook nog meegeven als parameter
    # ook variabelen initial temp and final temp mogelijk meegeven om meer dynamiek te creeeren 
    def __init__(self, grid, cooling='linear', alpha=0.4, rate_of_decrease=0.95, initial_temp=90, final_temp=.1):
        self.grid = grid
        self.initial_temp = initial_temp
        self.cooling = cooling
        self.final_temper = final_temp
        self.alpha = alpha
        self.rate_of_decrease = rate_of_decrease
        self.x = 0

   
    def execute(self): ## rename to execute 
        """NOTE: ER IS NOG GEEN CHECK AANWEZIG DAT DE EERSTE EN/OF LAATSTE NIET VERWISSELD MOGEN WORDEN.
        WEET NIET OF DAT NODIG IS, MAAR ANDERS NOG AANPASSEN. OOK NOG CHECKEN OF HET GOED GAAT ZO MET CURRENT
        CONFIGURATION EN HET UPDATEN DAARVAN. The function returns the updated grid object, where the protein folding
        configuration is saved within the amino_acids dictionary."""
        
        current_temp = self.initial_temp
        k = 0
        
        # Creating an initial state using the randomise algorithm 
        super().execute()
        
        # The protein configuration is stored in de amino_acids dictionary in the grid object
        current_configuration = self.grid
        current_score = self.grid.compute_score()

        # Setting the best values equal to the current ones 
        self.best_configuration = current_configuration
        self.best_score = current_score
        
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
                acceptance_probability = math.exp((-score_diff) / current_temperature)
                acceptance_probability = round(acceptance_probability, 2)

                # Also giving worse configuration a chance of acceptance 
                if random.random() > acceptance_probability:
                    current_configuration = self.new_protein_obj
                    current_score = new_score

                    # If the new configuration has a higher score, update the best configuration
                    if current_score < self.best_score:
                        self.best_score = current_score
                        self.best_configuration = current_configuration

            # Updating the temperature according to the cooling schedule 
            if self.cooling == 'exponential':
                current_temperature = self.initial_temperature * self.alpha**k
            if self.cooling == 'logarithmic':
                current_temperature = self.initial_temperature / math.log(k+1)
            if self.cooling == 'linear':
                current_temperature *= self.rate_of_decrease
            if self.cooling == 'adaptive':
                pass 

            print(f'best configuration is {self.best_configuration}')
            print(f'best score is {self.best_score}')
        
    def get_best_configuration(self):
        return self.best_configuration
    
    def pullMove(self, new_protein_dict):
        """Updates the dictionary location values of the new_protein (grid)object.
        In protein folding, pull moves involve moving an amino acid to a nearby unoccupied 
        diagonal position."""

        amino = random.choice(new_protein_dict)
        current_co = amino._location 
        coordinates = self.new_protein_obj.getDiagonals(amino)

        while not coordinates:
            amino = random.choice(new_protein_dict)
            diagonals = self.new_protein_obj.get_valid_diagonals(amino)
            new_location = random.choice(diagonals)
            amino._location = new_location         

        return new_protein_dict






        



   


