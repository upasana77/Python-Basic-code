#creating the error
# here 'i' is the type code in the array

from array import *
vals = array('i',[5,9,8,4,2])
print(vals)
##########################################
# we can use ceratain function with array
# we will take buffer_info method which will give the size of the array
from array import *
vals = array('i',[5,9,8,4,2])
print(vals.buffer_info())
# we can see from the output that the buffer info is giving both the Address and size of the array.
from array import *
vals = array('i',[5,9,8,4,2])
print(vals.typecode)
# the typecode method will print the type which is 'i' as int.
# in the same way we can append,remove, reverse and apply many more method to an array.
from array import *
vals = array('i',[5,9,8,4,2])
vals.reverse()
print(vals)
### so here we have applied the reverse function.
###################################################
# we can also print the values one by one, by using index number, as array is behave like list.
from array import *
vals = array('i',[5,9,8,4,2])
print(vals[1])
# we can pritnt all the values, by using 1 by 1, by using a for lopp.
from array import *
vals = array('i',[5,9,8,4,2])
for i in range (5):
      print(vals[i])
# what if we do not know the   length of the array
from array import *
vals = array('i',[5,9,8,4,2])
for i in range (len(vals)):
      print(vals[i])
# we can use 'e' , it even works
from array import *
vals = array('i',[5,9,8,4,2])
for e in range (len(vals)):
      print(vals[e])
# can I use character in place of integer? yes, by using the typecode
from array import *
vals = array('u',['a','e','i'])
for i in range (len(vals)):
      print(vals[i])
###############################################################
# I want to create a new array with the same value
from array import *
vals = array('i',[5,9,8,4,2])
newArr = array(vals.typecode, (a for a in vals))
for e in newArr:
      print(e)
############################################################
# suppose I want to get the square of a number
from array import *
vals = array('i',[5,9,8,4,2])
newArr = array(vals.typecode, (a*a for a in vals))
for e in newArr:
      print(e)
# as we can see from the output we have the square of a number
#############################################################
# we can use the while loop
# we have use initialization,increment or decrement
from array import *
vals = array('i',[5,9,8,4,2])
newArr = array(vals.typecode, (a for a in vals))
i =0
while i<len(newArr):
      print(newArr[i])
      i+=1
