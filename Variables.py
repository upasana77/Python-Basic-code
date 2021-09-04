Python 3.9.7 (v3.9.7:1016ef3790, Aug 30 2021, 16:39:15) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> >>> ##############################
## I learn:
# what is variable?
# why do we need them
# How to assign value to variable.
# Fetching value of previous operation
# string value to variable
# Fetching value of string variable by index number
# finding the length of string
>>> # variables:so variable is a container where we are putting certain value, we can give always certain name to the variable(variable name) and the value which we put inside the container.
>>> 2+3
5
>>> x = 2
>>> x+3
5
>>> y = 3
>>> x+y
5
>>> # as the name suggest we can always change the value of variable, that's why it is variable
>>> x = 9
>>> x+y
12
>>> # so in summary variable is just a box where we define certain values.
>>> # when we are using a variable we must need to define it, we cannot use any random variable name.
>>> if we want to use output of the previos line of code we can use '-' 
  File "<stdin>", line 1
    if we want to use output of the previos line of code we can use '-' 
          ^
SyntaxError: invalid syntax
>>> -+y
-3
>>> x+10
19
>>> - + y
-3
>>> _+y
0
>>> x+10
19
>>> _ + y
22
>>> # as we can see by using a underscore we can always use previous output, and perform our operation on that.
>>> ## can I use variable with string?
>>> ## can I use variable with string? yes
>>> name = 'youtube'
>>> name
'youtube'
>>> name+ 'rocks'
'youtuberocks'
>>>  name + ' rocks'
  File "<stdin>", line 1
    name + ' rocks'
IndentationError: unexpected indent
>>> name + ' rocks'
'youtube rocks'
>>> # we must use + plus to concatenate two strings.
>>> # we can also use string as error let's take youtube
>>> name[0]
'y'
>>> name[6]
'e'
>>> # as it starts from 0.zero.
>>> ## we cannot go outof range it will give an error for example
>>> name[8]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> so can I use minus(-) symbol for accesing array yes, it will start from right to left(-1 to so on)
  File "<stdin>", line 1
    so can I use minus(-) symbol for accesing array yes, it will start from right to left(-1 to so on)
       ^
SyntaxError: invalid syntax
>>> # so can I use minus(-) symbol for accesing array yes, it will start from right to left(-1 to so on)
>>> name[-1]
'e'
>>> name[-2]
'b'
>>> # if I want to print two character, i will start from 0 and it will end at 2(ending character)
>>> name[0:2]
'yo'
>>> name[1:4]  ## here we will print 1 to exclusive 4 means upto 3.
'out'
>>> ## if we don't specify the ending part it will go up to the end.
>>> name[1:]
'outube'
>>> ## here i will specify the ending part which start not the beginning
>>> name[:4]
'yout'
>>> # if specify the last range as wrong value it will not give us an error.
>>> name[3:10]
'tube'
>>> ## we can see it's printing upto the last value without giving a error.
>>> ## changing letter in an array
>>> name[0:3] = 'my'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> name[0] = 'R'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> ## we can see in the above lines of code we are getting an error which means string in python is unmutttable, we cannot change the value.
>>> ## but we can prit
>>> 'my ' + name[3:]
'my tube'
>>> ## there are some built-in function in python like 'len'
>>> myname = 'Navin Reddy'
>>> len(myname)
11
>>> ## here we can get the length of the string.
>>> print(r 'Telusko \n Rocks')
  File "<stdin>", line 1
    print(r 'Telusko \n Rocks')
            ^
SyntaxError: invalid syntax
>>> print(r'Telusko \n Rocks')
Telusko \n Rocks
>>> 
