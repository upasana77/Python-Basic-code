Python 3.9.7 (v3.9.7:1016ef3790, Aug 30 2021, 16:39:15) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> upasanapurohit@UPASANAs-iMac-Pro ~ % python3
Python 3.9.7 (v3.9.7:1016ef3790, Aug 30 2021, 16:39:15) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> Tuple and set in Python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Tuple' is not defined
>>> ## tuple and set in python
>>> # the difference between list and tuple is in list we can change the value but tuple is unmutable
## Difference between tuple and list
## create tuple
## count
##Where to use tuple
## what is set
## define set
## hashing in set
## set functions

>>> tup = (21,36,14,25) ## we specify tuple with round bracket
>>> tup(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object is not callable
>>> tup
(21, 36, 14, 25)
>>> ## in tuple we cannot change the value
>>> tup[1]
36
>>> tup[1] = 22
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> ## we cannot use ceratin method in tuples
>>> tup.index[0] =4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'builtin_function_or_method' object does not support item assignment
>>> ## since we do not change value in tuples, iteration is faster than list.
>>> ## thats why we need to use tuple if you want to enhance the speed of execution
>>> ######SET= A set is a collection of unique elements
>>> ## as square brackets for list, round brackets for tuple and curley bracket is for set.
>>> s = { 22,25,14,21,5}
>>> ## set does not follow a sequence.
>>> s
{5, 21, 22, 25, 14}
>>> ## we can see from the output
>>> s = { 25,14,98,63,75,98}
>>> s
{98, 25, 75, 14, 63}
>>> ## actually set outpu is not sorted, it used the concept of "hash" for improving the performance.
>>> ## as in set we do not have proper sequence, indexing is not working here.
>>> s[1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object is not subscriptable
>>> ## but we can applycertain method with set without indexing
>>> s.append(65)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'set' object has no attribute 'append'
>>> s.pop()
98
>>> s.append(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'set' object has no attribute 'append'
>>> s.appand(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'set' object has no attribute 'appand'
>>> 







