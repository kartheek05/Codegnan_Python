'''
Length = int(input("Enter the Length of Rectangle: "))
Width = int(input("Entre the Width of Rectangle: "))
Area = Length * Width
print(Area)
<---------------------------------------------------------------------------------------------------------------------------------------------------->
Name  = input("Enter the name: ")
Age = int(input("Enter the age: "))
print(f"HI {Name} Wish you a good day!")
<---------------------------------------------------------------------------------------------------------------------------------------------------->
n = int(input("Enter the Number: "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")
<---------------------------------------------------------------------------------------------------------------------------------------------------->
List_1 = list(map(int,input("Enter the Values: ").split()))
print("Maximum",max(List_1))#Built in Function
print("Minimun",min(List_1))#Bulit in Function

minimum = List_1[0]
maximum = List_1[0]

for i in List_1:
    if i < minimum:
        minimum = i
    if i > maximum:
        maximum = i
print(f"The Maximum no is {maximum} and Minimum number is {minimum}")
<---------------------------------------------------------------------------------------------------------------------------------------------------->
n = input("Enter the Data: ")

# if n == n[::-1]:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")
<---------------------------------------------------------------------------------------------------------------------------------------------------->

'''

