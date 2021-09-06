Python 3.9.7 (v3.9.7:1016ef3790, Aug 30 2021, 16:39:15) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 5
b = 6
# for swapping we must need to use a third variable to swap them
# for swapping we can do this program we can use a third variable which is a
# another way to fins swap value by using a+b, but we have one issue with this
##
# temp = a
# a = b
# b = temp
 # a = a+b   # 11
# b = a-b  # 5
# a = a-b  # 6
# here we can use "xor" symbol to find the value, here we are not wasting extra memory
 # a = a ^ b
 # b = a ^ b
 # a = a ^ b
 # we have one more way to swap the value in python, this goes into stack and then it's reverse, or rotation or rotating the value ,just search about xor,rot2 for swapping
a,b = b,a
print(a)
print(b)
 