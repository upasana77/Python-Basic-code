Python 3.9.7 (v3.9.7:1016ef3790, Aug 30 2021, 16:39:15) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> >>> ################################################################
# operator in Python
# arithmetic operator: addition,subtraction,multiplication and divison
# assignment operator
## Relational operator- equals to, greater then, less than, not equals, greater than equals to
# logical operator-AND,OR,NOT,TRUTH TABLE OF LOGICAL OPERATOS
#Unary operators-negation
# 
>>> operators in python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'operators' is not defined
>>> ## operators in python
>>> ## so we will talk about 1) Arithmetic operator,2) assigment operators, 3) relational operator, 4) logical operator 4) Unary operator
>>> ## arithmetic operator:
>>> x = 2
>>> y = 3
>>> x+y
5
>>> x-y
-1
>>> x*y
6
>>> x/y
0.6666666666666666
>>> ## equal to symbol means assignment operator
>>> x =8
>>> x = x+2
>>> x
10
>>> ## we can do the same operation we can do on shotcut way
>>> x +=2
>>> x
12
>>> ## the same thing we can do substraction, multiplication and divison.
>>> x*=3
>>> x
36
>>> x/=4
>>> x
9.0
>>> x-=5
>>> x
4.0
>>> aa,b = 5,6 ## we can do assignment in one itself
>>> a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
>>> a,b = 5,6
>>> a
5
>>> b
6
>>> ## unary operator: unary operator means one
>>> n = 7
>>> n
7
>>> -n
-7
>>> n = -n
>>> n
-7
>>> ## logical and relational operator
>>> ## relational operator( compairing two stuff)
>>> a<b
True
>>> a>b
False
>>> a ==b ## here we are compairing not assigning
False
>>> a =6
>>> a ==b
True
>>> a<=b
True
>>> a>=b
True
>>> ## not equal
>>> a!=b
False
>>> b =7
>>> a!b
  File "<stdin>", line 1
    a!b
     ^
SyntaxError: invalid syntax
>>> a!=b
True
>>> ## logical operator(concept of true and false) and,or,not
>>> a = 5
>>> b =4
>>> a<8 and b<5
True
>>> a<8 and b<2
False
>>> ## in Truth table we can represent Truth = 1 false = 0
>>> ## and means multiplication
>>> ##or table is like if we have atleast one is true the result is always true
>>> a<8 or b<2
True
>>> x = True
>>> x
True
>>> notx
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'notx' is not defined
>>> not x ## reversing a operation or negate an operation
False
>>>  x = not x
  File "<stdin>", line 1
    x = not x
IndentationError: unexpected indent
>>> x = not x
>>> x
False
>>> 
