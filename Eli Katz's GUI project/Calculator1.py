import tkinter as tk
import random #import random

def random1():
	print("random1")
	x = random.randint(1,20)
	entrX.delete(0,tk.END)
	entrX.insert(0,x)


def random2():
	print("random2")
	y = random.randint(1,20)
	entrY.delete(0,tk.END)
	entrY.insert(0,y)

def random3():
	print("random3")
	c = random.randint(1,20)
	entrC.delete(0,tk.END)
	entrC.insert(0,c)

def showAnswer():
	print("show answer")
	a = float (entrX.get())
	print (a)
	b = float (entrY.get())
	print (b)
	c = float (entrC.get())
	print (c)
	
	ms = "-" + str(a) + "/" + str(b)
	
	m = -1*a/b
	
	bis = str(c) + "/" + str(b)
	
	bi = c/b
	
	eqs = "y = " + ms + "x + " + bis
	
	eq = "y = " + str(m) + "x +" + str(bi)
	print(eq)
	
	labANS2.config(text = eqs)





root = tk.Tk()





#************** Widget 1 (entry boxes) **************
entrX = tk.Entry(root)
entrX.grid(row = 2, column = 0)

entrY = tk.Entry(root)
entrY.grid(row = 3, column = 0)

entrC = tk.Entry(root)
entrC.grid(row = 4, column = 0)


#************** Widget 2 (labels) **************
labX = tk.Label(text = "x")
labX.grid(row = 2, column = 1)

labY = tk.Label(text = "y")
labY.grid(row = 3, column = 1)

labC = tk.Label(text = "c")
labC.grid(row = 4, column = 1)

labANS = tk.Label(text = "Answer:")
labANS.grid(row = 5, column = 0)

labEQ = tk.Label(text = "Equation:")
labEQ.grid(row = 7, column = 0)

labANS2 = tk.Label(text = "answer = ")
labANS2.grid(row = 7, column = 1)

#************** Widget 3 (buttons) **************
btnR1 = tk.Button(root, text = "Random", command = random1)
btnR1.grid(row = 2, column = 2)

btnR2 = tk.Button(root, text = "Random", command = random2)
btnR2.grid(row = 3, column = 2)

btnR3 = tk.Button(root, text = "Random", command = random3)
btnR3.grid(row = 4, column = 2)

btnSHOW = tk.Button(root, text = "Show", command = showAnswer)
btnSHOW.grid(row = 5, column = 2)

root.mainloop()