#this imports the tkinter "toolbox" this contains
#all the support material to make GUI elements.
#by including "as tk" we are giving a short name to use.
import tkinter as tk


#Main Window
root = tk.Tk() #creates the standard main window.


#************** Widget 1 **************
#Three stages to build elements/objects
#1. Construct the Object: We build and cofigure it
#2. COnfigure the Object: We specify behaviours and setting (OPTIONAL)
#3. Pack the Object: Put it in the window
output = tk.Text(root,height = 10, width = 30) #Parameters are what we send to the function.
#there are ordered parameters: The order we send them matters. (COMMON)
#there are named paremeters: JavaScript and Python specific
output.config(state = "disable", background = "hot pink")
output.grid(row = 0, column = 0, rowspan = 5)


#************** Widget 2,3,4 (labels) **************
labInput1 = tk.Label(root, text = "Input 1")
labInput1.grid(row = 5, column = 0)

labInput2 = tk.Label(root, text = "Input 2")
labInput2.grid(row = 6, column = 0)

labInput3 = tk.Label(root, text = "Input 3")
labInput3.grid(row = 7, column = 0)

#************** Widget 5,6 (Checkboxes) **************
#How do I track the checkbox state.
var1 = tk.IntVar()
var2 = tk.IntVar()

#What the named parameter variable does is binds the IntVar to the
#checkbox. If there is a change in the box, there is a change in the
#variable. This is called BINDING
cHC = tk.Checkbutton(root, text = "High Contrast", variable = var1)
cHC.grid(row = 0, column = 1)

cLF = tk.Checkbutton(root, text = "Larger Font Size", variable=var2)
cLF.grid(row = 1, column = 1)


#we are writing an EVENT DRIVE PROGRAM
#Build the GUI
#Start it running
#Wait for "EVENT"
root.mainloop() #Starts the program.