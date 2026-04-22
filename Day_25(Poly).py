'''
Polymorphism:
-->This allows a object of different classes to be treated as instance if the same class, 
with methods behaving differently based on the actual object type.Eg: (len,slicing)
print(len("Pyhton"))
print(len([1,2,3]))
'''
'''
Method Overloding:
--->Ths defines multiple methods with same name but different parameters such as(number,type or order) in the class.

class calculator:
    def add(self,a,b=0,c=0):
        return a+b+c
    def sub(self,a,b=0,c=0):
        return a-b-c
cal = calculator()
print(cal.add(2))#a=2,b=0,c=0
print(cal.add(9,3))#a=9,b=3,c=0
print(cal.add(5,7,8))#a=5,b=7,c=8
print(cal.sub(2))#a=2,b=0,c=0
print(cal.sub(3,4,7))#a=3,b=4,c=7


class Calculator:
    def mul(self,a,b):
        return a*b
cal = Calculator()
'''
'''
Method Overriding :
---> This occurs in the child class, redefining a parent class method with the same signature for runtime.

class Animal:
    def speak(self):
        return "Sound"
class dog(Animal):
    def speak(self):
        return "Woof"
class snake(Animal):
    def speak(self):
        return "Schhhhh"
class scoulding(Animal):
    def speak(self):
        return "nuvu chala manchi vadi vi"
var = scoulding()
print(var.speak())
print(var.speak())


class dad:
    def speak(self):
        return "Good Boy"
class mom:
    def speak(self):
        return "Take Care"
obj = mom()
print(obj.speak())
'''

'''
Operator Overloding:
this is customizes operator like +,- for user-defined classes by implementing special methods..
Eg: ......__add__,__sub__

class someone:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __add__(self,other):
        return someone(self.a+other.a,self.b+other.b)
    def __str__(self):
        return f"({self.a},{self.b})"
any = someone(2,3)
so = someone(5,9)
print(any+so)'''

'''
Data Abstraction
This hides complex implementation details, exposing anly essential features via abstract class or interface.

from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
Circle = circle(5)
print(Circle.area())
'''
