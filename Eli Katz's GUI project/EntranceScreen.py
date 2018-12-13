import tkinter as tk


root = tk.Tk()

#Labels
labWELCOME = tk.Label(root, text = "Hello, welcome to the slope calculator and equation form modifier!")

labWELCOME.grid(row = 0, column = 0)

#Button
btnEnt = tk.Button(root, text = "Go!")
btnEnt.grid(row = 1, column = 0, rowspan = 1)

root.mainloop()


