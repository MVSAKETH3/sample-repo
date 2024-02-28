#iterators and generators
l1=[1,2,3,4,5]
itr=iter(l1)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
# print(next(itr)) eroor as all the elemnst are accessed
l2={'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
itr=iter(l2)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))


#generators
#we use yield it is like return but yield doesnt stops the function but yield doesnt stops the function it holds the value and continue from that.
def days():
    l3=['sun','mon','tue','wed','thu','fri','sat']
    i=0
    while True:
        yield l3[i]
        i=(i+1)%7
d=days()
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))

print('*'*30)

#local and global variables
g=10

def fun1(a,b):
    c=a+b
    print(c)
    print(g)
# print(c)   error
print(g)
fun1(4,8)

print('*'*30)
def fun2(a,b):
    c=a+b
    print(c)
    print(k)
k=10
fun2(9,10)

print('*'*30)


def fun3(a,b):
    global g
    print(g)
    g=20
    print(g)
    c=a+b
    print(c)
fun3(223,56)

a,b,c,d=1,2,3,4
def fun4(a=12,b=45):
    x,y,z=45,567,67
    print(locals())
fun4()
print(globals())

#Recursive()

def fun5(n):
    if n==0:
        return 1
    else:
        # return n*fun5(n-1)
        res=n*fun5(n-1)
        return res

print(fun5(5))

#function as object

def fun6():
    print("Hello i am Saketh")
f=fun6
f()

#Nested Function

def Outer():
    def Inner():
        print("Hello i am Saketh")
    Inner()
Outer()

# function as parameter
def display():
    print("Hi i am psycho")
def calling(d):
    d()
dis=display
calling(dis)


def add(x,y):
    print(x+y)
def sub(x,y):
    print(x-y)
def calls(f,a,b):
    f(a,b)
calls(add,10,20)
calls(sub,6,8)


#function returing a function

def outer():
    def show():
        print("hello world")
    return show()
o=outer
o()


