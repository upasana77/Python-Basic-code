
# we will write here a simple code in python just to mimic the vending machine.
x = int(input("How many Candies you want?")) # I will ask the number of candy required to the user.
i = 1
while i <= x:
     print('Candy')
     i+=1 # the number of candy value will get incremented
##############################################################
# we write the program for getting the number of candy, now what if the required amount of candy is not available
# at the vending machine
av = 10  # av is the available candies
x = int(input("How many candies you want?"))
i = 1
while i<= x:
     if i>av:
          break
     print("Candy")
     i+=1
print("Bye")
#################################################################
av = 5  # av is the available candies
x = int(input("How many candies you want?"))
i = 1
while i<= x:
     if i>av:
          break
     print("Candy")
     i+=1
print("Bye")
# this is how we could use the break statement to come out of the loop.
# if we want to print a message we can do that too, so if we want to jump out of a certain step we can always do that
# by using the break statement
av = 5  # av is the available candies
x = int(input("How many candies you want?"))
i = 1
while i<= x:
     if i>av:
          print("Out of stock")
          break
     print("Candy")
     i+=1
print("Bye")
##############################################################
# suppose i want to print 1 to 100, but I do not want to print those number which is divisible by 3.
# here we will see the application of continue statement
# it will not jump out of the loop, it will just skip the given condition. and again continue
for i in range(1,101):
     if i%3 == 0:
          continue
     print(i)
print('Bye')
# we use both for 3 and 5
for i in range(1, 101):
     if i % 3 == 0 or i%5==0:
          continue
     print(i)
print('Bye')
# now we are skipping both diviible by 5 and 3
#############################################################
# now we will use the value pass
# so we will write a program, which will not print the odd number
for i in range(1, 101):
     if(i%2!=0): # we are saying if the given value is odd then we need to pass
          pass  # we just write pass if we won't have any block of code,we simply pass it
     else:
          print(i)
# so as we pass with odd number condition we are getting only even number
