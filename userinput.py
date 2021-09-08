Python 3.9.7 (v3.9.7:1016ef3790, Aug 30 2021, 16:39:15) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print("Upasana Purohit")
## drawing a dog in python:
print('o----')
print('||||')
# here we are getting multiple star, when we are drawing it.
print('*' * 10) # here we are drawing a start, inside quotation we have a string here.
#VARIABLE: we use variable to temporarily store data in a memory.
price = 10
price = 20
print(price)
SyntaxError: invalid syntax
>>> ## how to get input from user in python
x = input("Enter 1st number")
# here we are asking the user for the desired input
a = int(x) # as it is string here we have applied the type casting rule
y = input("Enter 2nd number")
b = int(y)
z = a+b
print(z)
## here we are using input function which always gives us string type in output,
# but we need an integer
Enter 1st numberx = int(input("Enter 1st number")) # here we are applying type casting directly
y = int(input("Enter 2nd number"))
z = x+y
print (z)
###################
# let's write a code where i want to take input from user in 'char' form i  python
ch = input('enter a char')
print(ch)
# in this example i can even print more than one character like pqr, but I still want 1st character
ch = input('enter a char')[0] # here we apply the indexing, for accesimg the 1st character pnly
print(ch)
####################################
# there is a function called 'eval' which we will use here to evaluate a full expression
result = eval(input('enter an expr'))
print(result)
#####################################
# agrn means argument values, which means we can pass any number of input, it depends on the user
import sys
x = int(sys.argv[1])
y = int(sys.argv[1])
z = x+y
print(z)
# we import sys as it belongs to 1a module called sys
## doubt with sys module
# write a code to find cube of the number,take the input from the user using input() and also using command line.
