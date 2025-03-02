from abc import ABC, abstractmethod
from lib2to3.pgen2.driver import Driver


class Demo(ABC):

    @abstractmethod
    def greet(self):
        pass

    @abstractmethod
    def add(self, a, b):
        pass

    def spam(self):
        print("in spam")


class Derived(Demo):

    def greet(self):
        print("Hello world")


    def add(self, a, b):
        print(a + b)

d = Derived()
d.add(1 , 2)

