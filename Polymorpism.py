#Polymorphism means one that exists in many forms
#we can achieve it through 4 ways:
#1.Duck Typing
#2.Method Overloading
#3.Method Overriding
#4.Opeartor Overloading


#Duck Typing



# In a statically typed language, data types are defined during compile time and cannot change during runtime. 
# This behavior is because of static type checking. 
# In contrast, dynamic typing allows variables to change their data type during runtime.

#the objects of the class doent matter it may change but the method are important

class Duck:
    def work(self):
        print('i am Duck and i can swim')
    def speak(self):
        print('qua qua')
class Dog:
    def work(self):
        print('i am Dog and i can run')
    def speak(self):
        print('woof woof')
class Person:
    def work(self):
        print('i am Person and i can code')
def display(object):
    object.work()
    object.speak()
    print('Information displayed')
du=Duck()
do=Dog()
p=Person()
display(du)
display(do)
# display(p)  #it will show error as it doesnt have the method speak.




#operator overloading
class ComlexNumber:
    def __init__(self,r,i):
        self.real=r
        self.imag=i
    def __add__(self,other):
        return f'{self.real+other.real}+{self.imag+other.imag}j'
c1=ComlexNumber(3,4)
c2=ComlexNumber(5,8)
print(c1+c2)



class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __gt__(self,other):
        return self.age>other.age
p1=Person('saketh',19)
p2=Person('aparna',20)
if p1>p2:
    print(f'{p1.name} is older than {p2.name}')
else:
    print(f'{p1.name} is elder than {p2.name}')

