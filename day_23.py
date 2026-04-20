'''
Encapsulation---->The principle of building data(Attribute) and method that operate on the data into a single unit, which is a class

class BankAc:
    def __init__(self, balance):
        self.__balance = balance

    def deposite(self, amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance

Acc = BankAc(int(input("Enter the Balance Amount: ")))
Acc.deposite(int(input("Enter the Deposite Amount: ")))
print(Acc.get_balance())

'''

'''
Inheritance----> This allows a child class(subclass) to acquire the attributes and methods of a parent class(Base class)
this is called Inheritance.
1.single Inheritance: It can Access Only single method from the parent class is called as single Inheritance.
class Parent:
    def display(self):
        print("This is Parent Method")
class child(Parent):
    def display(self):
        super().display()
        print("This is Child Method")
any = child()
any.display()
2.Multiple inheritance

Super()------->This is used to call methods of the parent class from the child class.
'''
class Father:
    def skill_1(self):
        print("Father: Hard Working")
class Mother:
    def skill_2(self):
        print("Mother: Lovely")
class Child(Father, Mother):
    def All_skills(self):
        print("Child: Coding")
any = Child()
any.skill_1()
any.skill_2()
any.All_skills()
         

