# we will draw some patterns by applying all the things whatever we have learned.
for j in range(4):
    print("#",end =" ")
print()
# from the above section of code we will get the first row and in the same way we could get other row
# but instead of repeating the same code we could also use another for loop
# here the main logic is the number of row, is equal to the number of # value.
for i in range(4): # for a new row
    for j in range(4): # for a new column
        print("#", end=" ") # for printing the '#' in each row
    print()  # for getting the output of row in new line.
# in total we are printing it 16 times.
# we can see in the output when the value of i = 0, it not printing any #, when i = 1 , it printing 1 #.
##############################################################
# let's built a triangle hash pattern
#as the above range function is contain 4 by 4 for rows and column
# we can modify that here as the value of i starts from 0.
# here we will keep same the number of row, and we will modify the number of column.
for i in range(4):
    for j in range(i+1):
        print("# ", end = " ")
    print()
###############################################################
# here we will print a reverse triangle
# In reverse pattern as the row value increases, the # value decreases.
for i in range(4):
    for j in range(4-i):
        print("# ", end = " ")
    print()

