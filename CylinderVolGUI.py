import tkinter as tk
import math

def submit():
	
	print("Submit Pressed")
	r = float(entr.get())
	h = float(enth.get())

	v = math.pi*r*r*h
	v = round(v,3)

	outputValue = "Given\nradies:"+str(r)="units\nheight:"+str(h)"units\nThe Volume is"+str(v)+"units\n\n"

	output.confic(state="normal")
	output.insert(tk.INSERT,v)
	output.config(state="disabled")

root = tk.Tk()#is a special method called a constuctor that builds a basic window
root.title('Volume of a Cylinder')

labr = tk.Label(root, text="radius")#this is creating a label
labr.pack()

entr = tk.Entry(root) #this is creatinga slot for entry
entr.pack()

labh = tk.Label(root, text="height")#this is creating a label
labh.pack()


enth = tk.Entry(root)
enth.pack()

btn = tk.Button(root, text="Submit", command=submit)
btn.pack()

output = tk.Text(root, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
output.config(state="disabled")
output.pack()




root.mainloop()