import tkinter as tk
import random 

grid = tk.Tk()

width = 3
height = 3

# loop over each amino-acid, make a label for each amino-acid and then generate the row and column 
# index to position it in the grid and display. 

# Label class is for text or images(widget)
# Controlling the width and height of a label with the width and height parameters

mylabel1 = tk.Label(grid, text='P', bg="blue", width=width, height=height)
mylabel2 = tk.Label(grid, text='H', bg="red", width=width, height=height)

# also possible to add the text to the window by using 
# mylabel1.pack()

# Generate random row and column in de range van de lengte van het eiwit (0 tm lengte eiwit)

mylabel1.grid(row=0, column=1)
mylabel2.grid(row=1, column=1)

grid.mainloop()



# import random

# class randomise:
#     def __init__(self, grid_size):
#         self.grid_size = grid_size
#         # Start with a fixed point
#         self.last_position = [grid_size // 2, grid_size // 2]
#         # Track all positions to avoid overlap
#         self.positions = [self.last_position.copy()]

#     def gen_location(self):
#         directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # Up, Down, Left, Right

#         while True:
#             if len(directions) == 0:
#                 raise Exception("No valid positions left to place an amino acid")

#             direction = random.choice(directions)
#             next_position = [self.last_position[0] + direction[0], self.last_position[1] + direction[1]]

#             # Check if next_position is in the grid and is not overlapping with existing ones
#             if (0 <= next_position[0] < self.grid_size) and \
#                (0 <= next_position[1] < self.grid_size) and \
#                next_position not in self.positions:
#                 break
#             else:
#                 # Remove invalid direction
#                 directions.remove(direction)

#         self.positions.append(next_position)
#         self.last_position = next_position

#         return tuple(self.last_position)



