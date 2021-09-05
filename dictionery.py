Python 3.9.7 (v3.9.7:1016ef3790, Aug 30 2021, 16:39:15) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> >>> >> ###########################################################
>>> Dictionary= = datatype
  File "<stdin>", line 1
    Dictionary= = datatype
                ^
SyntaxError: invalid syntax
>>> # dictionary datatype
>>> # so a dictionary have both  key and value, and the key should be unique and unmutable.
>>> data = {1: 'Navin', 2:'Kiran', 4:'Harsh'}
>>> data
{1: 'Navin', 2: 'Kiran', 4: 'Harsh'}
>>> ## we always have to specify the key to fetch the value.
>>> ## if I do somethibg outside of key value, I will get an error.
>>> data[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 3
>>> data4[4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'data4' is not defined
>>> data[4]
'Harsh'
>>> # we can always use several function with the dictionary key
>>> ## like clear,get,pop,
>>> data.get(1)
'Navin'
>>> ## data will print 'not found'
>>> data.get(1, 'Not Found')
'Navin'
>>> data.get(3,'Not Found')
'Not Found'
>>> ## let's create adictionary with the help of list:
>>> keys = ['Navin, 'Kiran', 'Harsh']
  File "<stdin>", line 1
    keys = ['Navin, 'Kiran', 'Harsh']
                     ^
SyntaxError: invalid syntax
>>> Keys = ['Navin', 'Kiran','Harsh']
>>> Values = ['Python', 'java','js']
>>> data = dict(zip(keys,values))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'keys' is not defined
>>> data = dict(zip(Keys,Values)
... data
  File "<stdin>", line 2
    data
    ^
SyntaxError: invalid syntax
>>> keys = ['Navin','Kiran','Harsh']
>>> values = ['python','java','js]
  File "<stdin>", line 1
    values = ['python','java','js]
                                  ^
SyntaxError: EOL while scanning string literal
>>> keys = ['navin', 'kiran', 'harsh']
>>> values = ['python','java','js']
>>> data = dict(zip(keys,values))
>>> data
{'navin': 'python', 'kiran': 'java', 'harsh': 'js'}
>>> ## we can access these value through key
>>> data['Kiran']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Kiran'
>>> data['Navin']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Navin'
>>> data[navin']
  File "<stdin>", line 1
    data[navin']
                ^
SyntaxError: EOL while scanning string literal
>>> data['kiran']
'java'
>>> data['navin']
'python'
>>> ## if we want to fetch new value and key into the eictionery
>>> data[monika'] = 'cs'
  File "<stdin>", line 1
    data[monika'] = 'cs'
               ^
SyntaxError: invalid syntax
>>> data['monika'] = 'cs'
>>> data
{'navin': 'python', 'kiran': 'java', 'harsh': 'js', 'monika': 'cs'}
>>> ## we can also deleat value from a dictionery by accessing the key
>>> del data['harsh']
>>> data
{'navin': 'python', 'kiran': 'java', 'monika': 'cs'}
>>> ## we will create a new dictionary, which will have dictionary and list inside it.
>>> prog = {'js' : 'atom', 'cs':'vs','python':['pycharm','sublime'], 'java': {'jse':'netbeans','jee':'Eclipse'}}
>>> prog['js']
'atom'
>>> prog['python']
['pycharm', 'sublime']
>>> prog['python'],[1]
(['pycharm', 'sublime'], [1])
>>> prog['java']
{'jse': 'netbeans', 'jee': 'Eclipse'}
>>> prog['java']['jee']
'Eclipse'
>>> 
