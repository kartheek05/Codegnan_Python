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
Amount = int(input("Enter the Amount: "))
interest_rate = int(input("Enter the Interest Rate: "))
time_perios = int(input("Enter the Time Periosd"))

ci = Amount*(1+interest_rate/100)**time_perios
print(ci)
<---------------------------------------------------------------------------------------------------------------------------------------------------->
days = int(input("Enter the Days: "))
year = 365/days
week = 7/days

print(days)
print(year)
print(week)
<---------------------------------------------------------------------------------------------------------------------------------------------------->
Positive_integers = list(map(int,input("Enter the numbers: ").split()))
sum = []
for i in Positive_integers:
    if i > 0:
        sum += i
        print("sum")
    else:
        print("No positive numbers")
<---------------------------------------------------------------------------------------------------------------------------------------------------->
n = input("Enter the sentence: ")
print(len(n))
<---------------------------------------------------------------------------------------------------------------------------------------------------->
n = int(input("Enter the first number: "))
s = int(input("enter the second number: "))
n,s = s,n
print(f"first number{n} and second number {s}")
'''