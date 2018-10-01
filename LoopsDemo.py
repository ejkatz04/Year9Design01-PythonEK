#Looks are stritures used to repeat sections of code.
#They are useful if you have to do the same thing more than once
#or your can establish

#Example 1
print("0")
print("1")
print("3")
print("4")
print("**************")
#this is a counted loop. I want you to think about 
#count, check, change
#i = 0, 0 < 5, True - RUN LOOP
#i = 1, 1 < 5, True - RUN LOOP
#i = 2, 2 < 5, True - RUN LOOP
#i = 3, 3 < 5, True - RUN LOOP
#i = 4, 5 < 5, True - RUN LOOP
#i = 5, 0 < 5, FALSE - EXIT AND MOVE ON
for i in range (0,5,1):
	print(i)