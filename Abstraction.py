from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, n):
        self.n = n
    
    @abstractmethod
    def display(self):
        pass
    
    @abstractmethod
    def Notyres(self, n):
        pass

class Bike(Vehicle):
    def __init__(self, n):
        super().__init__(n)
    
    def display(self):
        print('I am a Bike')
    
    def Notyres(self):
        print('I have', self.n, 'Tyres')

class Car(Vehicle):
    def __init__(self, n):
        super().__init__(n)
    
    def display(self):
        print('I am a Car')
    
    def Notyres(self):
        print('I have', self.n, 'Tyres')

b = Bike(2)
b.display()
b.Notyres()

c = Car(4)
c.display()
c.Notyres()
