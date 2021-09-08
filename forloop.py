# in for loop we do not have to perform the intialization, incrementation, here we will get the output by itself.
x = ['navin',65,2.5]
for i in x:  # so here we are fetching the value of x to i.
    print(i)
#############ex2
x = 'navin'
for i in x:
    print(i)
    #########ex3 we can also take a list here
for i in [2,6,'paul']:
    print(i)
#####################
for i in range(10):  # here the range value has started from 0 end at 9.
    print(i)
#############
for i in range(11,21,1): # starting point,ending point,interval
    print(i)
    ##########
    for i in range(11,21,4):
        print(i)
  #printing reverse by using the range function, here as we have used -1, it is printing one value extra
for i in range(20,10,-1):
      print(i)
# let's write a program, if the value get divisible by 5, it should not print
for i in range(1,21):
    if i % 5 != 0:
        print(i)