import tkinter as tk
from tkinter import ttk
import random #import random

#Function written by Mr. Miskew. 
#return the greatest common factor of a and b
def findGCF(a,b):
	a = int(a)
	b = int(b)
	gcf = 1

	for i in range(1,min(a,b) + 1, 1):
		#MOD (%) gives the remainder when we divide two numbers
		#if m%n == 0 n is a factor of m
		if a % i == 0 and b % i == 0:
			gcf = i

	return gcf







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
	
	gcf = findGCF(a,b)
	a = a / gcf
	b = b / gcf


	ms = "-" + str(a) + "/" + str(b)
	if b == 1:
		ms = "-" + str(a)
	
	
	#ms = "-" + str(a/b)
	
	m = -1*a/b
	
	bis = str(c) + "/" + str(b)
	
	bi = c/b
	
	eqs = "y = " + ms + "x + " + bis
	
	eq = "y = " + str(m) + "x +" + str(bi)
	print(eq)
	
	labANS2.config(text = eqs)





root = tk.Tk()

tabControl = ttk.Notebook(root)



#********************
#Tab 1

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text="Equation Converter")
tabControl.grid()

#************** Widget 1 (entry boxes) **************
entrX = tk.Entry(tab1)
entrX.grid(row = 2, column = 0)

entrY = tk.Entry(tab1)
entrY.grid(row = 3, column = 0)

entrC = tk.Entry(tab1)
entrC.grid(row = 4, column = 0)


#************** Widget 2 (labels) **************
labX = tk.Label(tab1,text = "x")
labX.grid(row = 2, column = 1)

labY = tk.Label(tab1,text = "y")
labY.grid(row = 3, column = 1)

labC = tk.Label(tab1,text = "c")
labC.grid(row = 4, column = 1)

labANS = tk.Label(tab1,text = "Answer:")
labANS.grid(row = 5, column = 0)

labEQ = tk.Label(tab1,text = "Equation:")
labEQ.grid(row = 7, column = 0)

labANS2 = tk.Label(tab1,text = "answer = ")
labANS2.grid(row = 7, column = 1)

#************** Widget 3 (buttons) **************
btnR1 = tk.Button(tab1, text = "Random", command = random1)
btnR1.grid(row = 2, column = 2)

btnR2 = tk.Button(tab1, text = "Random", command = random2)
btnR2.grid(row = 3, column = 2)

btnR3 = tk.Button(tab1, text = "Random", command = random3)
btnR3.grid(row = 4, column = 2)

btnSHOW = tk.Button(tab1, text = "Show", command = showAnswer)
btnSHOW.grid(row = 5, column = 2)

#******************************************
#Tab 2


tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="Slope Calculator")
tabControl.grid()


#************** Widget 1 (entry boxes) **************
entrY1 = tk.Entry(tab2)
entrY1.grid(row = 0, column = 1)

entrY2 = tk.Entry(tab2)
entrY2.grid(row = 1, column = 1)

entrX1 = tk.Entry(tab2)
entrX1.grid(row = 2, column = 1)

entrX2 = tk.Entry(tab2)
entrX2.grid(row = 3, column = 1)

entrANS = tk.Entry(tab2)
entrANS.grid(row = 5, column = 1)

#************** Widget 2 (labels) **************
labY1 = tk.Label(tab2,text = "Y1")
labY1.grid(row = 0, column = 0)

labY2 = tk.Label(tab2,text = "Y2")
labY2.grid(row = 1, column = 0)

labX1 = tk.Label(tab2,text = "X1")
labX1.grid(row = 2, column = 0)

labX2 = tk.Label(tab2,text = "X2")
labX2.grid(row = 3, column = 0)

labANS = tk.Label(tab2,text = "Answer")
labANS.grid(row = 5, column = 0)

#************** Widget 3 (buttons) **************
btnCALC = tk.Button(tab2, text = "Calculate")
btnCALC.grid(row = 4, column = 1, columnspan = 1)

btnSHOW = tk.Button(tab2, text = "Show Answer")
btnSHOW.grid(row = 5, column = 2)




root.mainloop()




