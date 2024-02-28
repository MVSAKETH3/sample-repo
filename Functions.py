#1.
def fun1(a,b,c):
    print(id(a))
    print(id(b))
    print(id(c))
    print(a*b*c)
    return a+b+c
x,y,z=10,20,30
print(id(x))
print(id(y))
print(id(z))
sum=fun1(x,y,z)
print(sum)
#2.positional vs keyword arguments
#positional arguments
def fun2(a,b):
    print('a',a)
    print('b',b)
fun2('saketh','surya')
print('*****************************************************************')
#keyword arguments
def fun3(a,b,c):
    print('a',a)
    print('b',b)
    print('c',c)
fun3(b='saketh',a='surya',c='venkat')
print('*****************************************************************')
#default arguments
#positional should be given as first while calling function  or make all the argumnets as keyword while calling but 
#don't make the positional last
#default should be on right side in function
#defaults are created only once
def fun4(a,b=0,c=0):
    print('a',a)
    print('b',b)
    print('c',c)
fun4(10,20,30)
fun4(10,b=40,c=60)
fun4(10)
fun4(10,20)
# fun4(a=10,20) error


#defaults are created only once
def fun5(item,l=[]):
    l.append(item)
    print(l)

fun5(10)
fun5(20)
fun5(30)

l1=['saketh','surya','venkat']
fun5('hari',l1)
fun5('aparna',l1)
fun5(l1)



#Mixed positional or keyword arguments
#/ before must be positional after / it may be positional or keyword
#anything after * must be keyword 
def fun6(a,b,c,d,e,f):
    print(a,b,c,d,e,f)
fun6(10,20,30,40,50,60)
fun6(f=10,c=20,d=30,b=40,a=50,e=60)
fun6(30,40,10,d=20,e=70,f=90)
print('*****************************************')
def fun7(a,b,/,c,d,e,f):
    print(a,b,c,d,e,f)
fun7(10,20,30,40,50,60)
# fun7(f=10,c=20,d=30,b=40,a=50,e=60)
fun7(30,40,10,d=20,e=70,f=90)
print('*****************************************')

def fun8(a,b,/,c,d,*,e,f):
    print(a,b,c,d,e,f)
# fun8(10,20,30,40,50,60) error
fun8(10,20,30,40,e=70,f=90)
fun8(40,50,60,d=80,e=100,f=110)
print('*****************************************')

#varibale length arguments
def fun9(*args):
    print(args,type(args))
fun9(1,2,3,5,4,56,6789,5678)
fun9()
fun9(2)

def fun10(a,b,*args):
    print(a,b,args)
fun10(1,2,78,6789,7890,7890)
# fun10() error
fun10(1,2)

def fun11(*args,a,b): 
    print(a,b,args)
fun11(1,2,78,6789,7890,7890,a=6,b=7)
# fun11(45678,3456,5678,567,5678,67,6,23456,23,4) rror as if we give *args first then definelt we should pass keyword arguments.
print('*****************************************')

#unpacking arguments

def fun12(a,b,c):
    print(a,b,c)
l1=[1,2,3]
# fun12(l1)
fun12(l1[0],l1[1],l1[2])

fun12(*l1)
s1='sky'
fun12(*s1)
print('*****************************************')
#multiple return values

def fun13(a,b,c):
    return a+1,b+1,c+1
x,y,z=fun13(10,20,30)
t=fun13(50,60,70)
print(x,y,z)
print(t)

#keyword variable length arguments

def fun14(**kwargs):
    print(kwargs)
    print(type(kwargs))
fun14(name='saketh',age=19,height=6)


def fun15(**kwargs):
    for i in kwargs:
        print(i,kwargs[i])
fun15(name='saketh',age=19,height=6)


#mixed arguments

def fun16(a,b,*args,c,**kwargs):   #for mixed arguments always **kwargs should be last and a,b should be first
    print(a,b,args,c,kwargs)
fun16(10,20,34,56,78,345,567,4567,3456,c=90,name='saketh',age=19,height=6)