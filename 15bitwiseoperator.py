Python 3.9.7 (v3.9.7:1016ef3790, Aug 30 2021, 16:39:15) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> ## Bit-wise operator
## example of bit-wise operator
## complement operator
## Tild sign
## Negative number 2's complement
## conversion of 1's complement to 2's complement
## and operator
## finding bitwise and of numbers
## or operator
## finding bitwise OR of numbers
## xor operator
## finding bitwise xor of numbers
## Left shift operator
## right shift operator
## Example of left shift and right shift operator
>>> ################# bitwise operator
>>> ## In "bit-wise operator" we have 6 operatoe 1) complement,2) and 3) or(|)
>>> 4)xor(^)5)Left shift(<<) 6) Right shift(>>)
  File "<stdin>", line 1
    4)xor(^)5)Left shift(<<) 6) Right shift(>>)
     ^
SyntaxError: unmatched ')'
>>> ## In "bit-wise operator" we have 6 operatoe 1) complement,2) and 3) or(|)
>>> >>> ## complement(~) ~ this is called 'tild' operator.
>>> ~12
-13
>>> # this is the complement of -12 is 13, it just reverse of your binary format.
>>> ## bit-wise and operator = as we know in and operator if both are true then only we get true
>>> ## but in or if any one of them is True we get True value
>>> 12 & 13
12
>>> ## how to find bit-wise in traditional way.
>>> ## let's do bit wise 'or' operator
>>> 12|13
13
>>> # so bitwise and or or means binary and and or operation
>>> 25&30
24
>>> ## try it in your notebook
>>> ## x-or operator,
>>> There is always little diffrence between bit-wise and logical operator, the bit-wise operator means we convert the number format to decimal number format, so unlike logical operator 
  File "<stdin>", line 1
    There is always little diffrence between bit-wise and logical operator, the bit-wise operator means we convert the number format to decimal number format, so unlike logical operator 
                    ^
SyntaxError: invalid syntax
>>> ## here we mainly use instead of using and and or we use in the symbol form like ( & and |) in case of bitwise operator.
>>> 25 & 30
24
>>> ## here we covert 25 into binary format and 30 into binary format, and then we perform the and operation, 
>>> ## x-or operator: we can represent the operation with the symbol(^), where 0 x-or 0 give 0
>>> # 0 xor 1 give 1
>>> # 1 x-or 0 give 1
>>> # 1 x-or 1 give 0
>>> # logic is diffrent value give 1 in x-or and equal value give 0 in x-or
>>> 12 ^ 13
1
>>> 25 ^ 13
20
>>> 25 ^ 30
7
>>> ## left shift operator: the symbol of left-shit operator is (<<):
>>> 10 <<2
40
>>> ## in left-shift we are shifting the bits towards left by applying extra 0, before the decimal or dot
>>> # that is why we are gaining the bits in left-shift
>>> ## but in case of right shift we are losing the bits.
>>> ## 10>>2
>>> 10>>2
2
>>> ## so here we are moving 2 digit to the right, so rest we have only 10.
