# as we know prime number is a number which is divisible by 1 and itself, for instance, 7,13 and 19
# how do you check a given number is prime or not?
# so for getting a prime number the logic is every time we will have to check, ex: 7, we will check 7 is
# divisible by 2, then, 3,4,5,6, and we stop before 7, if it won't divisible with anyone it is a prime number
num = 7
for i in range(2,num):
    if num % i ==0:
        print("Not prime")
        break
else:
    print("Prime")
######################################################
# we can find the prime number in a effivient way.