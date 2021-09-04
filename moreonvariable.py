Python 3.9.7 (v3.9.7:1016ef3790, Aug 30 2021, 16:39:15) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> >>> ###### learn about "sublime" text editore for writing python.
>>> ## more on variables in Python
##more about variables in python
## what happen when we declare variable
## id of variable
## Assigning or tagging value of one variable to another
## Variables having same value
## id of an object
## Tags in Python
## Garbage collection Python
## cONSTANTS
### Typeof variables
>>> num = 5
>>> num
5
>>> ## how do you what is the adress of a variable in Python? we have a function called "id" which will help us to get address.
>>> ##id(num)
>>> id(num)
140545422977456
>>> name = 'upasana'
>>> id(name)
140544886199792
>>> ## so for both  num and name we have two diffrent adress.
>>> a = 10
>>> b=a # here I have assigned the value a to b.
>>> id(a)
140545422977616
>>> id(b)
140545422977616
>>> ##IN PYTHON WHEN WE HAVE MULTIPLE DATA, THEY BOTH GET POINT TO THE SAME BOX, OR SAME VALUE WILL HAVE SAME ADRESS.
>>> ##THAT IS WHY PYTHON IS MORE MEMORY EFFICIENT BECAUSE WE ARE NOT GETTING MULTIPLE DATA HERE.
>>> id(10)
140545422977616
>>> ## if we assign our 10 to k, or we can say tag(inplace of assign), still we get the same adress in Python
>>> id(k)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'k' is not defined
>>> K= 10
>>> id(k)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'k' is not defined
>>> k = 10
>>> id(k)
140545422977616
>>> ## once I change the value of a, it will give a different adress, because different value means diffrent box.
>>> a = 9
>>> id(a)
140545422977584
>>> id(b)
140545422977616
>>>  k= a
  File "<stdin>", line 1
    k= a
IndentationError: unexpected indent
>>> id(b)
140545422977616
>>> k = a
>>> id(k)
140545422977584
>>> ## now we have two boxex, one for value 10 and other for value 9, where both have unique adresses.
>>>  b = 8
  File "<stdin>", line 1
    b = 8
IndentationError: unexpected indent
>>> b=8
>>> ## now no one is using 10, so in python that is why we have a concept of garbage collection.
>>> ## when your datavalue is not tag for any variable it used for garbage collector.
>>> ## what is constant in Python, we cannot make a variable to a constant, but we can always write constant in capital letter
>>> PI = 3.14
>>> P
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'P' is not defined
>>> PI
3.14
>>> ## but in Python, we could change the value of the constant..
>>> ## so In python we canot make constant, but we can show our intention by writing everything in capital letter.
>>> ## type of the variable
>>> type(PI)
<class 'float'>
>>> ## normally this type are called as data type.

