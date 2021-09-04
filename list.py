Python 3.9.7 (v3.9.7:1016ef3790, Aug 30 2021, 16:39:15) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> >>> ######################
>>> ## list =  a group of data value
## working with list
## what is list
## how to use list
## Assign multiple value to variables
## printing value of list
## print value of list by index number
## string list
## list of different type of data type
## creating list with list:nested list
## append function
## insert function
## remove function
## pop function
## delete function
## extend function
##inbuilt function of list: min,max,sum
## sort function
>>>  nums = [25,12,36,95,14]
  File "<stdin>", line 1
    nums = [25,12,36,95,14]
IndentationError: unexpected indent
>>> nums
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'nums' is not defined
>>> nums = [24,36,18]
>>> nums
[24, 36, 18]
>>> nums[0]
24
>>> 
>>> nums[2:3]
[18]
>>> nums[-1]
18
>>> # we could also use negative number here, we can slice them too.
>>> ## example of list of string, see the following
>>> names = ['navin','kiran','john']
>>> names
['navin', 'kiran', 'john']
>>> ## can I create a list of different type?yes, but in array we must have to be same type( in java,c,c++)
>>> values = [9.5,'navin',25]
>>> values
[9.5, 'navin', 25]
>>> ## can we have two list working together? yes
>>> mil = [nums, names]
>>> mil
[[24, 36, 18], ['navin', 'kiran', 'john']]
>>> #different method operation on list:
>>> # list is mutable , which means we can change the list value.
>>> ## use appends() method
>>> nums.append(45)
>>> nums
[24, 36, 18, 45]
>>> ## the insert() method, the difference betwween append and insert method is in append we could only append  at the end, but in case of insert we can insert inbetween.
>>> nums.insert(2,77)
>>> nums
[24, 36, 77, 18, 45]
>>> nums.remove(14)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>> nums.remove(24)
>>> nums
[36, 77, 18, 45]
>>> # if I want to deleat based on the index number, I could use pop()
>>> nums.pop(1)
77
>>> nums
[36, 18, 45]
>>> ## if we do not specify thr value we could always deleat the last value
>>> nums.pop()
45
>>> nums
[36, 18]
>>> ## lets us method
>>> nums = [25,12,77,36,95,45]
>>> del nums[2:]
>>> nums
[25, 12]
>>> num.extend([29,12,14,36])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'num' is not defined
>>> nums.extend([29,12,14,35])
>>> nums
[25, 12, 29, 12, 14, 35]
>>> ## in list we can also use some in-built function
>>> min(nums)
12
>>> max(nums)
35
>>> sum(nums)
127
>>> ## one more method in python is called
>>> nums.sort()
>>> nums
[12, 12, 14, 25, 29, 35]
>>> ## list is very intresting, we can always mutate, by using different built-in and methods, if we want to use any particular value we can always use, index.
>>> name = "Telusko"
>>> print(name[-3])
s
