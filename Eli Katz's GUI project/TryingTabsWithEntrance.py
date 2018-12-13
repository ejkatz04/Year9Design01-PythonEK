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
	if b == 1:
		bis = "-" + str(c)
	

	
	bi = c/b
	
	eqs = "y = " + ms + "x + " + bis
	
	eq = "y = " + str(m) + "x +" + str(bi)
	print(eq)
	
	labANS2.config(text = eqs)

def randomS1():
	print("randomS1")
	y1 = random.randint(1,20)
	entrY1.delete(0,tk.END)
	entrY1.insert(0,y1)

def randomS2():
	print("randomS2")
	y2 = random.randint(1,20)
	entrY2.delete(0,tk.END)
	entrY2.insert(0,y2)

def randomS3():
	print("randomS3")
	x1 = random.randint(1,20)
	entrX1.delete(0,tk.END)
	entrX1.insert(0,x1)

def randomS4():
	print("randomS4")
	x2 = random.randint(1,20)
	entrX2.delete(0,tk.END)
	entrX2.insert(0,x2)

def showAnswerSlope():
	print("slope calculated")
	
	y1 = float (entrY1.get())
	print (y1)

	y2 = float (entrY2.get())
	print(y2)
	
	x1 = float (entrX1.get())
	print(x1)

	x2 = float (entrX2.get())
	print(x2)

	rise = y2-y1
	run = x2 - x1
	slope1 = "slope = " + str(rise) + "/" + str(run)
	

	#y2y1 = str(y2) - str(y1)

	#x2x1 = str(x2) - str(x1)

	#slope = y2y1 + "/" + x2x1
	#print(slope)

	labANSSLOPE.config(text = slope1)







root = tk.Tk()

tabControl = ttk.Notebook(root)

#********************
#tab1






tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text="Welcome!")
tabControl.grid()

#Labels
labWELCOME = tk.Label(tab1, text = "Hello, welcome to the slope calculator and equation form modifier!")
labWELCOME.grid(row = 0, column = 0)

#Button
btnEnt = tk.Button(tab1, text = "Go!")
btnEnt.grid(row = 1, column = 0, rowspan = 1)

#********************
#Tab 2

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="Equation Converter")
tabControl.grid()

#************** Widget 1 (entry boxes) **************
entrX = tk.Entry(tab2)
entrX.grid(row = 2, column = 0)

entrY = tk.Entry(tab2)
entrY.grid(row = 3, column = 0)

entrC = tk.Entry(tab2)
entrC.grid(row = 4, column = 0)


#************** Widget 2 (labels) **************
labX = tk.Label(tab2,text = "x")
labX.grid(row = 2, column = 1)

labY = tk.Label(tab2,text = "y")
labY.grid(row = 3, column = 1)

labC = tk.Label(tab2,text = "c")
labC.grid(row = 4, column = 1)

labANS = tk.Label(tab2,text = "Answer:")
labANS.grid(row = 5, column = 0)

labEQ = tk.Label(tab2,text = "Equation:")
labEQ.grid(row = 7, column = 0)

labANS2 = tk.Label(tab2,text = "answer = ")
labANS2.grid(row = 7, column = 1)

#************** Widget 3 (buttons) **************
btnR1 = tk.Button(tab2, text = "Random", command = random1)
btnR1.grid(row = 2, column = 2)

btnR2 = tk.Button(tab2, text = "Random", command = random2)
btnR2.grid(row = 3, column = 2)

btnR3 = tk.Button(tab2, text = "Random", command = random3)
btnR3.grid(row = 4, column = 2)

btnSHOW = tk.Button(tab2, text = "Show", command = showAnswer)
btnSHOW.grid(row = 5, column = 2)

#******************************************
#Tab 3


tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text="Slope Calculator")
tabControl.grid()


#************** Widget 1 (entry boxes) **************
entrY1 = tk.Entry(tab3)
entrY1.grid(row = 0, column = 1)

entrY2 = tk.Entry(tab3)
entrY2.grid(row = 1, column = 1)

entrX1 = tk.Entry(tab3)
entrX1.grid(row = 2, column = 1)

entrX2 = tk.Entry(tab3)
entrX2.grid(row = 3, column = 1)


#************** Widget 2 (labels) **************
labY1 = tk.Label(tab3,text = "Y1")
labY1.grid(row = 0, column = 0)

labY2 = tk.Label(tab3,text = "Y2")
labY2.grid(row = 1, column = 0)

labX1 = tk.Label(tab3,text = "X1")
labX1.grid(row = 2, column = 0)

labX2 = tk.Label(tab3,text = "X2")
labX2.grid(row = 3, column = 0)

labANSSLOPE = tk.Label(tab3,text = "answer = ")
labANSSLOPE.grid(row = 4, column = 2)

#************** Widget 3 (buttons) **************
btnSHOW = tk.Button(tab3, text = "Show Answer", command = showAnswerSlope)
btnSHOW.grid(row = 4, column = 1)

btnRS1 = tk.Button(tab3, text = "Random", command = randomS1)
btnRS1.grid(row = 0, column = 2)

btnRS2 = tk.Button(tab3, text = "Random", command = randomS2)
btnRS2.grid(row = 1, column = 2)

btnRS3 = tk.Button(tab3, text = "Random", command = randomS3)
btnRS3.grid(row = 2, column = 2)

btnRS4 = tk.Button(tab3, text = "Random", command = randomS4)
btnRS4.grid(row = 3, column = 2)



root.mainloop()