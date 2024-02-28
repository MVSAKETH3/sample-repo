a='hi i am "saketh" studing in vit'
print(a)
b="hello i am 'saketh sharma' from vit-b"
print(b)
c='HI I AM \'SAKETH\' FROM IT'
print(c)
d="hello i am \"saketh sharma\" from it-b"
print(d)
e=""" good morningi to all i am saketh from vit college
i am from the IT department
i have participated in GDSC"""
print(e)
f='''name is :saketh sharma
age:19
color:fairy
height:5.5'''
print(f)

# ACCESSING INDIVIDUAL CHARACTERS AND SUBSTRING IN A STRING
g="saketh sharma"
print('1',g[:4])
print('2',g[1:6])
print('3',g[-1:13])
print('4',g[-10:-2])
print('5',g[-1:-4])
print('6',g[0])
print('7',g[3])
# g[2]='y'      #they are Immutable
# print(g)
#STRING OPERATIONS:
#1.STRING CONCATENATION AN REPETITION CHARACTER
h='i'
i='am'
j='saketh sharma'
print(h+i+j)
print('1',3*j)
print('2',j*3)
print('3',3*j)
print('4',0*j)
print('5',-4*j)
#2.STRING COMPARISON OPERATOR
#comparsion is based on ASCII for a=97 A=65
#so A<a
print('1','hello'=='Hello')
print('2','hello'=='hello')
print('3','hello'!='Hello')
print('4','hello'!='hello')
print('5','hello'<'Hello')
print('5.1','hello'<'hello')
print('5.2','hello'<='hello')
print('6','hello'>'Hello')
print('6.1','hello'>'hello')
print('6.2','hello'>='hello')
#3.MEMBERSHIP OPERATOR
#in and not in
k='saketh'
l='saketh sharma'
print('1',k in l)
print('2',k not in l)
print('3','' in l)
print('4','e' in k)
#4.Escape sequence operator
#\n for new line \b for backspace \t for tab space \000 for 3 digit octal number \xhh for hxadecimal number
#to convert ocatl to decimal we multiple each digit with 8^ and its place value similarly to conversion of heaxadecimal 16^
print('hi i am saketh \n I am \x66rom "Indi\141"\t byee..')
#4.STRING FORMATTING OPERATOR 
#% is used to fromat a string
#%d,%c,%s,%f are commonly used string formatters
age=19
height=5.5
accuracy=0.01
extra='sharma'
nick='b'
print('1','my age is %d'%(age))
print('2','my height is %f'%(height))
print('3','my accuracy is %f'%(accuracy))
print('4','my nickname is %c'%(nick))
print('5','my name extra added is saketh%s'%(extra))

#STRING SLICING IN DETAIL
m='abc'*3
print(m)
print('1',m[::3])  #it means 3-1-2 so skip every 2 character  it is STEPCOUNT
print('2',m[1::3])
print('3',m[:5:3]) 
n='i am jaspreet'
print('1',n[2:10:2])   #ositive indicates to traverse in left to right direction
print('2',n[8:1:-2])  #negative indicates to travesre in right to left
#negative third parameter
#1.stepvalue+1 specifies the number of values to skip starting from the last
#2.the first parametr is greater than second parameter
#3.second parameter+1 specifies the stopping point
o='string'
print('**',o[5:0:-1])
print('##',o[5:-1:-1])
print('$$',o[5::-1])

#reversing a string
p='saketh sharma'
print('reverse is:',p[::-1])


#STRING FORMATTING
#string formatting is also called as string interpolation
# interpolation:interpolation is the insertion of something of a different nature into something else
#string interpolation:it is defined as inserting an object into a predefined string
#%-formatting is an old technique to insert object into a string
print("my name is %s" %p)
print("my name is %s and i am learnig about %s" % (p,o))
#str.format()Function
print('**************************************************************************')
print("my name is {0} and i am learnig about {1}".format(p,o))
print("my name is {} and i am learnig about {}".format(p,o))
print("my name is {name} and i am learnig about {topic}".format(name=p,topic=o))  #for better readbility we use keywords.
print('**************************************************************************')
print("i got {0:f}% marks in xams".format(92.22))
print("i got {:f}% marks in xams".format(92.22))
print("i got {:.3f}% marks in GATE".format(97.7894567))
print("i got {1:f}% marks in xams and overall average is {0:f}% ".format(92.22,96.78))
print("i got {1:f}% marks in xams and overall percent is{0:f}% ".format(92.22,98))
print('********************************************************************************')
print(f'my name is {p} and i am learnining about {o}.')

#call to method is possible
print(f'my name is {p.upper()} and i am learnining about {o.upper()}.')
#multiline f-strings
print('**************************************************************')
details=f"my name is {p}."\
f"I am learnining about {o}."\
f"my age is {age}."
print(details)
print('**************************************************')
data=(f"my name is {p}."\
f"I am learnining about {o}."\
f"my age is {age}.")
print(data)
print('**************************************************')
info=f"""my name is {p}.
I am learnining about {o}.
my age is {age}."""
print(info)
print('**************************************************')
print(f'{"SAKETH"}')
# print(f'{'SAKETH'}')  #it give error
print(f"{'SAKETH'}")
# print(f"{"SAKETH"}")   #it give error
print(f"""SAKETH""")
print(f'Hello my name is \"saketh\" and i am in \"B.Tech\".')
x=10
y=20
print(f'the sum of x+y is {x+y}')
print(f'the sum of {{x+y}} is {x+y}')
print(f'the sum of {{x+y}} is {{{x+y}}}')

t=x+y
#python will not convert implicity from integer to string
# print('the sum is'+t)

print('#############################')
z1='0078.965'
z2='3345'
temp1=int(z2)
print(temp1)
# print(int(z1))
temp2=float(z1)
print(temp2)
temp22=float(z2)
print(temp22)
z3=89.788
temp3=int(z3)
print(temp3)
print('################')
v1=34
v2=34.65
demo1=str(v1)
demo2=str(v2)
print(demo1)
print(demo2)
print(type(demo1))
print(type(demo2))

#so now t=x+y
print('Now the sum of x+y is '+str(t))

print('-----example for implicit conversion-----')
ans=3+89.78
print(ans)
print(type(ans))
v3='a'
# demo3=int(v3)
# print(demo3)  #but it gives error
print(ord(v3))
print(chr(65))