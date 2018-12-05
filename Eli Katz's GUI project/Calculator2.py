import tkinter as tk

root = tk.Tk()

#************** Widget 1 (entry boxes) **************
entrY1 = tk.Entry(root)
entrY1.grid(row = 0, column = 1)

entrY2 = tk.Entry(root)
entrY2.grid(row = 1, column = 1)

entrX1 = tk.Entry(root)
entrX1.grid(row = 2, column = 1)

entrX2 = tk.Entry(root)
entrX2.grid(row = 3, column = 1)

entrANS = tk.Entry(root)
entrANS.grid(row = 5, column = 1)

#************** Widget 2 (labels) **************
labY1 = tk.Label(text = "Y1")
labY1.grid(row = 0, column = 0)

labY2 = tk.Label(text = "Y2")
labY2.grid(row = 1, column = 0)

labX1 = tk.Label(text = "X1")
labX1.grid(row = 2, column = 0)

labX2 = tk.Label(text = "X2")
labX2.grid(row = 3, column = 0)

labANS = tk.Label(text = "Answer")
labANS.grid(row = 5, column = 0)

#************** Widget 3 (buttons) **************
btnCALC = tk.Button(root, text = "Calculate")
btnCALC.grid(row = 4, column = 1, columnspan = 1)

btnSHOW = tk.Button(root, text = "Show Answer")
btnSHOW.grid(row = 5, column = 2)




















root.mainloop()