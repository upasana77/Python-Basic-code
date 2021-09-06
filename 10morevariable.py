Python 3.9.7 (v3.9.7:1016ef3790, Aug 30 2021, 16:39:15) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> Type "help", "copyright", "credits" or "license" for more information.
>>> #################################################################
>>> # datatypes in python, the first one is none, numeric,list, tuple,set,string,range,dictionary.
>>> # when we have a variable and that value is not assigned by any value is called 'none'
>>> ## we can compare none with null.
>>> ## the secod type of data type is numeric type.
>>> #so if we talk about numeric type we have multiple type type here, 1) int, 2) float, 3) complex4) bool
>>> num = 2.5
>>> type(num)
<class 'float'>
>>> num = 5
>>> type(num) 
<class 'int'>
>>> num = a+bj
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
>>> num = 6+9j
>>> type(num)
<class 'complex'>
>>> a = 5.6
>>> b = int(a)
>>> type(b)
<class 'int'>
>>> b
5
>>> k = float(b)
>>> type(k)
<class 'float'>
>>> ## so here as we are doing type casting, can I convert a normal number into complex variable.
>>> k = 6
>>> c = comples(b,k)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'comples' is not defined
>>> c
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'c' is not defined
>>>  k = 6
  File "<stdin>", line 1
    k = 6
IndentationError: unexpected indent
>>> c = complex(b,k)
>>> c
(5+6j)
>>> ##when we talk about booleans we talk about true or false
>>> ## it comes under Numeric value becase we take True as 1 and False as 0.
>>> b<k
True
>>> bool = b<k
>>> type(bool)
<class 'bool'>
>>> b>k
False
>>> int(True)
1
>>> int(False)
0
>>> ## The Next-type we have is (List, Tuple,set,string,Range) those thing comes under sequence.
>>> lst = [25,36,45,12]
>>> type(lst)
<class 'list'>
>>> s = {25,36,45,15,12,25}
>>> s
{36, 25, 12, 45, 15}
>>> type(s)
<class 'set'>
>>> t = (25,36,4,57,12)
>>> type(t)
<class 'tuple'>
>>> str = "navin"
>>> type(str)
<class 'str'>
>>> ## how about character in python, in python we have do not have a char data type. becase we consider string as a character data-type
>>> st = 'a'
>>> type(st)
<class 'str'>
>>> ## we can always use char as part of the string
>>> ## range : when we iterate between value we use range, like goiung from 1 to 100
>>> range(10)
range(0, 10)
>>> ## ## we can convert list into range so we can print it.
>>> list(range)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'type' object is not iterable
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> ## what if I want range of other sequence of list
>>> list(range(2,10,2))
[2, 4, 6, 8]
>>> type(range)
<class 'type'>
>>> ## all this things comes under sequence.
>>> ## now we have most exciting type called as mapping or we can say dictionary
>>> ## so In dictionary when we have to fetch large amount of data, we assign a key, for each value od data.
>>> ### key should be unique, value we can repeat.
>>> ## as we put key inside curly bracket, because key doesnot repeat here.
>>> d = { 'navin': 'samsung','rahul':'iphone','kiran':'oneplus'}
>>> d
{'navin': 'samsung', 'rahul': 'iphone', 'kiran': 'oneplus'}
>>> d.keys()
dict_keys(['navin', 'rahul', 'kiran'])
>>> d.values()
dict_values(['samsung', 'iphone', 'oneplus'])
>>> ## how do get a particular values?
>>> d['rahul']
'iphone'
>>> ## we have one more way to fetch value in dictionery
>>> d.get('kiran')
'oneplus'
>>> ### so accesiing value in dictioney we can use square bracket or we can use a get method.
>>> 
