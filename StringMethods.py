#1.strip
v1='###Hello world###'.strip('#')
print(v1)
v2='    Hello World    '.strip()
print(v2)
v3=' ###Hello world###'.strip('#')
print(v3)
v4='Hello world'.strip('ldoH')
print(v4)
v5='Hello world'.strip('ldoh')
print(v5)
v6='      Hello World###'.lstrip()
print(v6)
v7='###Hello World     '.rstrip()
print(v7)
v8=" solving any problem is an art. ".strip('. ')
print(v8)
v9=" solving any problem is an art. ".strip('')
print(v9)
v10=" solving any problem is an art. ".strip(' ')
print(v10)

s1='I am Jaspreet  .'.lstrip('I am.')
print(s1)
s2='I am Jaspreet  .'.rstrip('I am.')
print(s2)
print(s1)
print(s2)

#2.Split
val1="Hello!$I$am$saketh".split('$',maxsplit=2)
print(val1)
val2="Hello I am Saketh".split()
print(val2)
val3="Hello!$I$am$saketh".rsplit('$',maxsplit=2)
print(val3)
val4="Hello I am Saketh".rsplit()
print(val4)

#s.partition(sep) it separtes the string into a tuple,s.rpartition(sep).

#3.join()    it is used to join the iterable
d1=['h','e','l','l','o']
print(''.join(d1))
d2=['i','am','saketh']
print(' '.join(d2))
d3={'name':'saketh','country':'india'}
print(' and '.join(d3))
f3=[1,2,3]
# print(' '.join(f3))  #we cant join the integers only the strings
#4.replace() it replaces a newstring with an old string
f1='i love to eat apples'.replace('apple','mangoes')
print(f1)
f2='i love you forever and ever'.replace(' ','-',2)
print(f2)
#5.Cases
q1='Saketh sharma'.upper()
print(q1)
q2='Saketh sharma'.lower()
print(q2)
q3='saketh sharma'.capitalize()   #only first letter is capitalized
print(q3)
q4='Saketh'.swapcase()
print(q4)
q5='saketh sharma'.title()  #it converst the first letter of every word to capital
print(q5)
print(q1.isupper())
print(q1.islower())

#casefold() it is similar to lower but it converts all the character in the world to lower but lower didnt convert all only the characters in ASCII
#so better to use casefold()

#isalpha(),isnumeric(),isalnum()
print('********************************')
w1='Hello saketh'
print(w1.isalpha())
w2='saketh'
print(w2.isalpha())
w3='23356'
w4='2/4'
w5='45.678'
w6='-12345'
print('********************************')
print(w3.isnumeric())
print(w4.isnumeric())
print(w5.isnumeric())
print(w6.isnumeric())
#according to string /,-,. are like blackslash,hipen,and dot so they are not conidered as numerics
w7='saketh123'
w8='saketh sharma'
w9='-34567'
print('********************************')
print(w7.isalnum())
print(w8.isalnum())
print(w9.isalnum())   #only a-z A-Z and 0-9

print('********************************')
hw1='sam234@gmail.com'.islower()
hw2='sam234@gmail.com'.upper()
hw3='sam234@gmail.com'.isalnum()
hw4='sam234@gmail.com'.isalpha()
print(hw1)
print(hw2)
print(hw3)
print(hw4)
print('********************************')
#count()it helps in finding te no.of occurences of a substring in a given string,if it is not found then it retrns 0
t1='i love fruits,fruits makes me healthy'
t2='i love fruits,Fruits makes me healthy'
print(t1.count('fruits'))
print(t2.count('fruits'))
print(t1.count('fruits',3,13))
print(t1.count('fruits',3,11))
print('********************************')
#find() it returns the index of first occurence of a substring in a given string if not found it returns -1
y1='it is beautiful'
print(y1.find('b'))
print(y1.find('b',1,5))
print(y1.find('B'))
#rfind() it returns the index of last occurence of a substring in a given string if not found it returns -1
print('********************************')
print(y1.rfind('i'))
print(y1.rfind('I',3,7))


#similarly we have index() and rindedx() works like find() but if the substring is not found it raises an exception.
#we have startswith(string,start,stop),endswith(string,start,stop),removesuffix(string),removeprefix(string)

#to igonore cases we use casefold()


print('************************************************************')
#to know about methods of a datatype we use
print(type(y1))
print(dir(y1))
print(help(y1.startswith))
print('************************************************************')

print('************************************************************')
#ljust(),rjust(),center()
r1='saketh'
print(r1.ljust(10))
print(r1.ljust(3))
print(r1.ljust(10,'*'))
print(r1.rjust(10))
print(r1.rjust(3))
print(r1.rjust(10,'*'))
print(r1.center(10))
print(r1.center(3))
print(r1.center(10,'*'))


print('************************************************************') 
#observe differences in isdecimal,isdigit,isnumeric for each case
h1='125'
h2='3.56'
print(h1.isdecimal())
print(h2.isdecimal())
print(h1.isdigit())
print(h1.isnumeric())
h3='134\u00b3'
print(h3)
print(h3.isdecimal())
print(h3.isdigit())
print(h3.isnumeric())
h4='5\u00bd'
print(h4)
print(h4.isdecimal())
print(h4.isdigit())
print(h4.isnumeric())


