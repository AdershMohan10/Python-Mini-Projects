from abc import ABC,abstractmethod

class Animal(ABC):

    def __init__(self):
        print('animal is created')

    @abstractmethod
    def sound(self):
        print('animal made sound')

class Dog(Animal):
    def __init__(self):
        print('dog created')

    def sound(self):
        print('woff woff')    

d=Dog()
d.sound()