Python 3.9.7 (v3.9.7:1016ef3790, Aug 30 2021, 16:39:15) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> Type "help", "copyright", "credits" or "license" for more information.
>>> ################################################
# mathmetical functiom
# in built function
# calling function
#import in python
#floor function
#ceil function
#printing pi value
#finding square root by sqrt function
#changing name of built-in functom
# importing only some part from math
>>> # import math function in python
>>> # let's find the square root of function, in python we have a built in function for square.
>>> x = sqrt(24)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sqrt' is not defined
>>> ## here we get an error because in python, we must need to import certain module here math module to use math
>>> # a math built-in function
>>> import math ## here we get permission to use all the function
>>> x = math.sqrt(25)
>>> x
5.0
>>> x = math.sqrt(15)
>>> x
3.872983346207417
>>> ## we have some other math built-n function as weel
>>> print(math.floor
... 
... ## here we get an error because in python, we must need to import certain module here math module to use math
... print(math.floor(2.9))
  File "<stdin>", line 4
    print(math.floor(2.9))
    ^
SyntaxError: invalid syntax
>>> print(math.floor(2.9))
2
>>> print(math.ceil(2.2))
3
>>> # as we can see floor give lowest value whre as ceil give higet value
>>> ## like wise we can do factorial, sinx,cosx,
>>> ## we can also do power by using pow function
>>> print(math.poe(4,2))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'poe'
>>> print(math.pow(3,2))
9.0
>>> ## here we have two choices we could also use double star(**)
>>> ##,it's always better to use function
>>> print(math.pi)
3.141592653589793
>>> print(math.e)
2.718281828459045
>>> ## so from aboe two staement we could find the value of 'pi' and 'abselon'
>>> ## if we do not want to write math always we could use the concept of allies
>>> import math as m
>>> math.sqrt(25)
5.0
>>> m.sqrt(25)
5.0
>>> # as we can see now 'm' is working
>>> ## when we want to use only one function,insted of importing math function what else we can do
>>> from math import sqrt,pow
>>> pow(4,2)
16.0
>>> ## as we can see here we do not have to specify the math function every time
>>> ## read documentation about math function







