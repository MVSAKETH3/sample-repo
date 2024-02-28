class Instruction:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.followers = 0

    def show(self, subjects):
        self.followers += 1
        print(subjects)

inst1 = Instruction("saketh", 18)
print(inst1.name)
print(inst1.age)
print(inst1.followers)
inst1.show('PYTHON')


# Inheritance
class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('I can Eat')

    def work(self):
        print('I can Work')

class Child(Parent):
    def __init__(self, name, age, height, weight):
        super().__init__(name, age)
        self.height = height
        self.weight = weight

    def talk(self):
        print('Yes i can talk')

    def walk(self):
        print('I can Walk')

    def work(self):
        super().work()
        print('I can code')

p1 = Child("saketh", 6, 19, 120)
p1.work()
p1.eat()
p1.walk()
p1.talk()
print(p1.name, p1.age, p1.weight, p1.height)


#Multiple Iheritance
class Data1:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print('Hi This is a Data1 class')
class Data2:
    def __init__(self,marks,grade):
        self.marks=marks
        self.grade=grade
    def display(self):
        print('Hi This is a Data2 class')
class Childer(Data1,Data2):
    def __init__(self,name,age,marks,grade):
        super().__init__(name,age)
        super().__init__(marks,grade)
    def details(self):
        print(f"This is the child class which is inherting characters from both classes i am {self.name}")
per1=Childer('saketh',19,98,'A')
per1.show()
per1.display()
per1.details()

# Your current implementation seems to be attempting multiple inheritance, but it's not quite correct. In Python, when using super(), it's essential to remember that it works with the Method Resolution Order (MRO), which defines the order in which superclasses are initialized.

# However, your current implementation calls super().__init__(name, age) and then immediately overrides those attributes by calling super().__init__(marks, grade). This will lead to unexpected behavior.

# Here's a corrected version of your code:

# python
class Data1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print('Hi This is a Data1 class')

class Data2:
    def __init__(self, marks, grade):
        self.marks = marks
        self.grade = grade

    def display(self):
        print('Hi This is a Data2 class')

class Childer(Data1, Data2):
    def __init__(self, name, age, marks, grade):
        super().__init__(name, age)  # Initialize Data1 attributes
        Data2.__init__(self, marks, grade)  # Initialize Data2 attributes

    def details(self):
        print(f"This is the child class which inherits characters from both classes. I am {self.name}, "
              f"age {self.age}, got {self.marks} marks and grade {self.grade}")

per1 = Childer('saketh', 19, 98, 'A')
per1.show()
per1.display()
per1.details()


#Multilevel inheritance,Multiple inheritance=hybrid inheritance

class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")
        super().greet()  # Calling super().greet() to invoke the method from superclass A

class E:
    def greet(self):
        print('HI i am new')

class C(A):
    def greet(self):
        print("Hello from C")
        super().greet()  # If E had a superclass, this would invoke that superclass's greet method

class D(C, B):  
    def greet(self):
        print("Hello from D")
        super().greet()  # This will invoke the method from superclass C

# Method Resolution Order
print(D.mro())
# print(D.__mro__)
d = D()
d.greet()




# Output
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]





#Diamond Problem
#the mro uses in Python, the method resolution order (MRO) determines the order in which methods are searched for and executed in the inheritance hierarchy. Python uses the C3 linearization algorithm to calculate the MRO. In the case of the diamond problem, the MRO ensures that methods are looked up in a consistent and predictable order.
#mro follows left,right then depth.
