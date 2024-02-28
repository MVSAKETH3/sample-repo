#encapsulation is wrapping up of dat into a single unit
#it is an implemantation of abstraction
#abstarction is just a thought process at design leb=vel
#but actull abstraction is achieved through encapsulation
#to access and modify private variable use get and set methods 
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
    def set_color(self,color):
        if self.__color=='fair':
            self.__color = "red"
        else:
            self.__color = color
    def get_color(self):
        return self.__color
        
class Child(Parent):
    pass

c1=Parent('sai',56)
c1._Parent__display()   #now we can access private methods directly
print(c1.get_color())
c1.set_color('fair')
print(c1.get_color())
c1.set_color('black')
print(c1.get_color())
