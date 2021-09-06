Python 3.9.7 (v3.9.7:1016ef3790, Aug 30 2021, 16:39:15) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> NameError: name 'python3' is not defined
>>> ###################################
# Number system conversion in python
# Binary
#Decimal
# Octal
# Hexadecimal
# Convert decimal to binary format
# bin function in python
# convert binary format to decimal format
# decimal to octal conversion
# decimal to hexadecimal conversion
# oct function
# hex function
>>> # numbersystem conversion
>>> ## in programming world we use binary and decimal system and also octal and hexadecimal number system
>>> ##like in networking we use mac adress which is used in hexadecimal
>>> ## so we need to know the conversion of one system to other by using programming
>>> ## i want to cobert 25 in binary format, how? by dividing 2 and taking the remainder
>>> ## so here we can use function called "bin" which will help us to convert from decimal system to binary system
>>> bin(25) ## so in decimal system we have base 10 ( where we go from 0 to9)
'0b11001'
>>> # whereas in Binary system we have base is 2 and we go from 0 to 1( which consist od 2 digits)
>>> # thats why we say bits which means it is binary digit
>>> ## in fact we have octal system which is 8 digit, it starts with 0 and end with 7,hexadecimal = we have base with base with 16( it starts from 0 and end at 15), so it go from 0 to 9, and then a-f)
>>> bin(25)
'0b11001'
>>> ## result of converting decimal to binary
>>> ## a bin function cotaining the statements of conversion which we do not have to write one by one
>>> ## "ob' this is the way to specify the binary format
>>> ## infact we can convert a number from decimal into a binary format, which is very east
>>> 0b0101
5
>>> ## in the above statement we get the output from a bunary format to decimal format which is 101 is 5
>>> ## lets do it with octal
>>> oct(25)
'0o31'
>>> ## octal conversion of 25, 0o is o is octal
>>> ## lets see the conversion of hexadecimal
>>> hex(25)
'0x19'
>>> # so x is for hexadecimal here
>>> hex(10)
'0xa'
>>> 0xf
15
>>> ## convert the decimal in to binary
>>> 



