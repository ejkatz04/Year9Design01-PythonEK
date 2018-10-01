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
for i in range (4,12,2):
	print(i)

print("**************")

for i in range (2,6,1):
	print(i*2)

print("**************BACKWARDS**************")

for i in range(10,-1,-1):
	print(i)


print("**************Printing String Characters**************")	
str = ("Monkey")

for i in range(len(str)-1, -1, -1):
	print(str[i])

print("MOVING ON")


print("**************PRINT EVERY SECOND LETTER IN STR START AT INDEX 0**************)
	