# forelse in python
# in python we can use for and else together
nums = [12,15,18,21,26]
# here I want to check if the list has a number which is divisible by 5.
# so we will check it from start to end, so we must have to use a loop.
for num in nums:
   if num % 5 ==0:
       print(num)
# let's see if we have to print only the first number which is divisible by 5
nums = [12,15,18,21,26,25]
for num in nums:
    if num % 5 == 0:
        print(num)
##################################
# how we could print only one number which is divisible by 5
# if we will simply apply the break ,it will give only 20
nums = [12,15,18,21,26,25]
for num in nums:
    if num % 5 == 0:
        print(num)
        break
# we can see from output we are getting only 15.
#######################################
# when we don't have a number in our list, what we will do
nums = [12,17,18,21,26,27]
for num in nums:
    if num % 5 == 0:
        print(num)
        break
    else:
       print("not found")
######################################
# we do not want to print the same code multiple time so we will use else, for for loop
nums = [12,17,18,21,26,27]
for num in nums:
    if num % 5 == 0:
        print(num)
        break
else:
     print("not found")
# we can see we have only one notfound.