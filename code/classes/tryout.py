import tkinter as tk

grid = tk.Tk()

# Label class is for text or images(widget)
# Controlling the width and height of a label with the width and height parameters
mylabel1 = tk.Label(grid, text='P', bg="blue", width=1, height=1)
mylabel2 = tk.Label(grid, text='H', bg="red", width=1, height=1)

# also possible to add the text to the window by using 
# mylabel1.pack()

mylabel1.grid(row=0, column=1)
mylabel2.grid(row=1, column=1)

grid.mainloop()
