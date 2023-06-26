import math
from code.algorithms import randomise
import random 
import copy 


class SA(randomise.Random):
    # eventueel alpha ook nog meegeven als parameter
    # ook variabelen initial temp and final temp mogelijk meegeven om meer dynamiek te creeeren 
    def __init__(self, grid, cooling='linear', alpha=0.4, rate_of_decrease=0.95):
        self.grid = grid
        self.initial_temperature = 90
        self.cooling = cooling
        self.final_temperature = .1
        self.alpha = alpha
        self.rate_of_decrease = rate_of_decrease
        self.x = 0

   
    def execute(self): ## rename to execute 
        """NOTE: ER IS NOG GEEN CHECK AANWEZIG DAT DE EERSTE EN/OF LAATSTE NIET VERWISSELD MOGEN WORDEN.
        WEET NIET OF DAT NODIG IS, MAAR ANDERS NOG AANPASSEN. OOK NOG CHECKEN OF HET GOED GAAT ZO MET CURRENT
        CONFIGURATION EN HET UPDATEN DAARVAN. The function returns the updated grid object, where the protein folding
        configuration is saved within the amino_acids dictionary."""
        current_temperature = self.initial_temperature
        
        # Creating an initial state using the randomise algorithm 
        super().execute()
        
        # The protein configuration is stored in de amino_acids dictionary in the grid object
        current_configuration = self.grid
        self.best_configuration = current_configuration
        current_score = self.grid.compute_score()
        self.best_score = current_score

        # Keeping track of iterations
        k = 0

        while current_temperature > self.final_temperature:
            k += 1
    
            # Generating a new configuration by swapping two amino_acids
            new_protein_obj = copy.deepcopy(current_configuration)
            self.new_protein_dict = new_protein_obj.amino_acids
            # i, j = random.sample(range(len(self.grid.amino_acids)), 2)
            # self.new_protein_dict[i] , self.new_protein_dict[j] = self.new_protein_dict[j], self.new_protein_dict[i]
           
            self.pivot()

            # Calculate the score of the new ordered dictionary (protein)
            new_score = new_protein_obj.compute_score()
            # print(f'NEW SCORE IS {new_score}')
            score_diff = abs(new_score - current_score)
            # print(f'SCORE DIFFERENCE IS {score_diff}')

            if score_diff > self.x:
                # Calculate the acceptance probability based on the difference in score and current temperature
                acceptance_probability = math.exp((-score_diff) / current_temperature)
                acceptance_probability = round(acceptance_probability, 2)
                # Also giving worse configuration a chance of acceptance 
                if random.random() > acceptance_probability:
                    current_configuration = new_protein_obj
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
                # cooling_factor = (final_temperature / initial_temperature) ** (1 / num_iterations)
                # cooling_factor = math.exp(math.log(self.final_temperature / self.initial_temperature) / self.rate_of_decrease)
                current_temperature *= self.rate_of_decrease
            if self.cooling == 'adaptive':
                pass 

        print(f'best configuration is {self.best_configuration}')
        print(f'best score is {self.best_score}')
        
    def get_best_configuration(self):
        return self.best_configuration
    
    def pivot(self):
        """Updates the dictionary location values."""

        # Selecting a pivot point
        #MAG NIET DE LAATSTE ZIJN DUS VANDAAR - 2
        random_key = random.randint(0, len(self.new_protein_dict) - 2)
        pivot = self.new_protein_dict[random_key] #== amino object

        # Determining the section to be rotated, by making a list of all the objects 
        section = list(self.new_protein_dict.values())[random_key+1:] 
        k, l = pivot._location
        
        for amino_obj in section:
            # Updating these positions based on the pivot point
            i, j  = amino_obj._location
            new_location = (i+1, k)
            i, j = new_location
        
           #MISSCHIEN NOG NODIG OM OP TE SLAAN IN ORIGINAL DICT???!






# By monitoring the acceptance rate over multiple iterations, you can gain insights into the algorithm's behavior and adjust the temperature accordingly.


### NOTES ###
# calculate metropolis acceptance criterion
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




###ORIGINAL HILL CLIMBER###
    # def hill_climber(self): ## rename to execute 
    #     """NOTE: ER IS NOG GEEN CHECK AANWEZIG DAT DE EERSTE EN/OF LAATSTE NIET VERWISSELD MOGEN WORDEN.
    #     WEET NIET OF DAT NODIG IS, MAAR ANDERS NOG AANPASSEN."""

    #     # Creating an initial state using the randomise algorithm 
    #     super().execute()
        
    #     # The protein configuration is stored in de amino_acids dictionary 
    #     best_configuration = self.grid.amino_acids
    #     best_score = self.grid.compute_score()
    #     no_improvement = 0

    #     while True:
    #         # Generating a new configuration by swapping two amino_acids
    #         new_protein_obj = copy.deepcopy(self.grid)
    #         new_protein_dict= new_protein_obj.amino_acids
    #         i, j = random.sample(range(len(self.grid.amino_acids)), 2)
    #         new_protein_dict[i], new_protein_dict[j] = new_protein_dict[j], new_protein_dict[j]

    #         # Calculate the score of the new ordered dictionary (protein)
    #         new_score = new_protein_obj.compute_score()

    #         # If the new configuration has a higher score, update the best configuration
    #         if new_score < best_score:
    #             best_configuration = new_protein_obj
    #             best_score = new_score
    #             no_improvement = 0 
    #         else:
    #             no_improvement += 1

    #         # Eindig de loop wanneer er geen vooruitgang is gemaakt na 10 iteraties
    #         if no_improvement >= 10:
    #             break

    #     print(f'best configuration is {best_configuration}')
    #     print(f'best score is {best_score}')
    #     return best_configuration, best_score



        



   


