#public
#private __
#protected _
class Parent:
    def __init__(self, name, age):
        self.name = name
        self._age = age
        self.__color = "fair"

    def __display(self):
        print(f"Hi this is {self.name} I am {self._age} and I am {self.__color}")

    def _eat(self):
        print(f"I can eat and my color is {self.__color}")

    def talk(self):
        print(f'I can Talk and my age is {self._age}')
    def show(self):
        print({self.__color})
        self.__display()


class Child(Parent):
    pass

c1 = Child('saketh', 19)
# c1.__display() # This line is commented out because __display() is a private method.
c1._eat()
c1.talk()
print(c1._age)
# print(c1.__color)   #it is private variable
c1.show()