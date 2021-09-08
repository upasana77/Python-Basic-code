# loop means we could always repeat the code
print("Teluskmo")
## if I want to print the same code thousand time, instead of writing them manually we can always apply the loop.
# we can use two loop one is called while loop and the other is called for loop
i = 1 # we need a certain number of counter to repeat our value, 5 times,initilization
while i<=5:   # conditions
    print("Telusko")
    i = i+1 # incrementing the value, or decrement
    # the two statement belongs to the same block
    # by applying debugging, and stepover we can always check our output

# so while loop consit of three steps 1) initilization, 2) condition 3) increment/decrement
i = 1 # we need a certain number of counter to repeat our value, 5 times,initilization
while i<=5:   # conditions
    print("Telusko",i)
    i = i+1 # incrementing the value, or decrement
    # the two statement belongs to the same block
    # by applying debugging, and stepover we can always check our output
# can I use more than one  while
i = 1
j = 1
while i<=5:
    print("Telusko",i)
    while j<=4:
        print("Rocks")
        j = j+1
    i = i+1
# as i want to print telusko same line
i = 1

while i<=5:
    print("Telusko", end="") # end means staying in the same line
    j=1
    while j<=4:
        print("Rocks", end="")
        j = j + 1
    i = i+1
    print() # we write one print here because we just want to use one new line.
