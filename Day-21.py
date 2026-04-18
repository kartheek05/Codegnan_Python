'''
Introduction to OOP's
Classes
Obejcts
Attributes
Methods
<---------------------------------------------------------------------------------------------------------------------------------------------------->
OOP'S------->(Object-Oriented Language)
                    --is a style of programming where we model real world things as object that contains both data and
                    functions(behaviors)
                    --Reuseability of the code
                    --scalability
<---------------------------------------------------------------------------------------------------------------------------------------------------->                    
CLASS------->This is blue-print or template
Syntax: class class_Name:
             pass
Example: class car:
<---------------------------------------------------------------------------------------------------------------------------------------------------->
OBJECT------->Instance of class or An object is a real instance created from a class.It is the actual thing that exists
                         in memory while the program runs.
Example:
class class_Name:
    pass
car1 = car()
car2 = car()
<---------------------------------------------------------------------------------------------------------------------------------------------------->
ATTRIBUTE------> These are the variables that store data related to a class or object.

'''
'''
class Dog:
    def __init__(self, breed, color, Type,gender):
        self.breed = breed
        self.color = color
        self.Type = Type
        self.gender = gender
Dog_1 = Dog("husky","white","Friendly","Female")
Dog_2 = Dog("lab","gold","Eco-friendly","Male")
Dog_3 = Dog("German Sheped","White","Friendly","Male")
print(Dog_1.breed,Dog_2.color,Dog_1.Type,Dog_2.gender)

class car:
    def __init__(self,Brand,Model,Type,Year,):
        self.Brand = Brand
        self.Model = Model
        self.Type = Type
        self.Year = Year
car_1 = car("Ferrari","Purosangue","Sport","2022")
car_2 = car("Toyota","Supra","Sport","2022")
car_3 = car("BMW","5Series","premium luxury sedans","2021")
car_4 = car("Audi","A4","premium luxury sedans","2021")
car_5 = car("Honda","CB350C","Normal","2026")
car_6 = car("TATA","Safari","Family","2026")
print(car_6.Model,car_5.Type)
'''
class Food:
    def __init__(self):
        pass

