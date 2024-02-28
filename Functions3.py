#closure functions
 #these are nested functions
#accessing non-local variables
#return Nested function
# we can use closures instead of caller classes

# def fun1():
#     msg="saketh,venkat,surya are friends"
#     def fun2():
#         print('*'*20)
#         print(msg)
#         print('*'*20)
#     return fun2()
# f=fun1
# f()



# class Dept:
#     def __init__(self):
#         self.depts={'Name':'saketh','age':19,'height':6,'color':'fair'}
#     def __call__(self,d):
#         return self.depts[d]
# data=Dept()
# s=data('Name')
# print(s)
# print(data('color'))


#now replace the caller class  meand class containing  this__call__ with closure function
# def Dept():
#     depts={'Name':'saketh','age':19,'height':6,'color':'fair'}
#     def dname(dept):
#         return depts[dept]
#     return dname
# data=Dept()
# s=data('Name')
# print(s)
# print(data('color'))


#decorator
#passing function as parameter
#nested function calling parameter function
#return nested function

# def decorator(fun):
#     def wrapper(msg):
#         print('*'*30)
#         print('HI')
#         fun(msg)
#         print('*'*30)
#     return wrapper

# @decorator
# def showing(msg):
#     print(msg)
# decorator(showing)

#lambda functions
#anonyms function   means functions which doesnt have any name
#single line expression
#any number of arguments

kms=lambda miles:1.6*miles
print('KMS:',kms(10))


s=lambda x,y :x+y
print(s(4,5))


g=lambda a,b:a if a>b else b
print(g(10,15))