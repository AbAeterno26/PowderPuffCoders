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
