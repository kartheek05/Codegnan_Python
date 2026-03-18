'''
variables is basically named storage location that is used yo haold data in the memory, to make it simple is the label which is points out to a value
They are aslo called as storage placeholders 

Rules for the defining variables are
--> A-Z, a-z, 0-9
--> start with uppercase, lowercase letters, even with a underscore.
--> But you cannot start wiht symbols (@,$,&.....), even number we czannot start using them.

Better preferable way is go with general purpose.---> you want to store your detalis name,emails_id,account numbers.


a=1
b=5
# Pyhton is dynamic typed, you need not say define the datatype and also
#only the recent value to the variable with the same name is wanted

print(a)
print(b)

#1a23 = 25 #syntax error
#@werf = 4.5 #synatx error 
#$dsf = 12 #Invalid error

name = "Codegnan"
location = "Visakhapatnam"
age = 7
email_ID = "Kumarkartheek@gmail.com"
print(name,location,age,email_ID)

#How to assing mutipile values to a variables
akash,praneeth,kartheek = 21,20,23
print(akash)
print(praneeth)
print(kartheek)

#assign same value to multiple values
x = y = z = 21
print(x,y,z)

#keywords are reserved word which have specific usage.
#There are 35 keywords in Python.
#never use keywords as Identifiers.
#if = 23
#lambda = 'kartheek'
#False = 0 #cannot asign

false = 25

#Identifiers are  anems given to variables, functions, classes, objects....
#Literals are fixed values to a Identifiers
name = 25
name = 'saketh'
# name is Identifiers, 25 is literal.
#Single line comments --> #
#Multiple Line Comments --> ''' '''
# Built-in datatypes --> Numeric,Boolen,Collections

#Numeric datatypes --> int, float, complex
#int --> count,vlaues, quantities
#float --> temperature,percentages,price
#complex--> specific conversions(real and imaginary)


count = 40
print(count)
print(type(count))

price = 272.24
print(type(price))

j3 = 25
value = 2+j3
print(value)
print(type(value))

value = 2+3j
print(value)
print(type(value))

#TypeCasting --> converting one type to another
#int --> float ,complex

age = 25
print(type(age))

b= float(age)
print(b)
print(type(b))
c= complex (age)
print(c)
print(type(c))

#float,complex
a = 25.5
print(type(a))

b = int(a)
print(b)
print(type(b))
c=complex(a)
print(type(c))

#complex to int,float

g=3+5j
print(type(g))

k = float(g)
print(type(g))
h = int(g)
print(type(h))

Boolean
a= True
print(a)
print(type(a))

#TypeCasting of bool
b = int(a)
print(b)
c  = float(a)
print(c)
d = complex(float(int(False)))
print(d)
print(type(d))
#Input --> input()/output -->
a=5
print(a)

a = input("Enter a Value")  #only integer input
print(a)
print(type(a))

a = int(input("Enter a Value:")) #only integer input
b = float(input("Enter a Value:"))
print(a)
print(type(a))
'''

#Now let's work on a simple case study using above -->Fee Calculator

#Detalis of the Student
name = input("Enter the student name:")
print("--------------------------------------")
admission_fees = int(input("Enter the Admission fees:"))
tuition_fees = float(input("Enter the Tuition Fees"))
hostel_fees = float(input("Enter the Hostel Fees"))
#Calculate the Total Fees
Total_fees = admission_fees+tuition_fees+hostel_fees
print("<----------------------------------------------------->")
print("Student Name:",name)
print("Admission_fees is:",admission_fees)
print("Tuition_fees:",tuition_fees)
print("Hostel_fees:",hostel_fees)
print("Total_fees:",Total_fees)
print("<----------------------------------------------------->")











