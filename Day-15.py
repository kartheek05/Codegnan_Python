'''
# Required Arguments -----> IF two arguments are passed then when calling it need two arrugemnts.
#                                               it should match same number of variables in calling wiht def
num = 9
num_2 = 10
def add(num,num_2):
    print(num)
add (num,num_2)
<---------------------------------------------------------------------------------------------------------------------------------------------------->
Default Arguments-----> It will take the default 


name = "Kartheek"
def add(name):
    print(name)
add (name = "Kumar")
add (name = "Karthik")
add (name = "Ravi")
<---------------------------------------------------------------------------------------------------------------------------------------------------->
n = int(input("Enter The Number: "))
def prime_(n):
    count = 0
    for i in range(1,n):
        if n % i == 0:
            count += 1
    if count == 2:
        print(f"{n} Prime Number")
    else:
        print(f"{n} Not a Prime Number")
prime_(n)
<---------------------------------------------------------------------------------------------------------------------------------------------------->

      def name (*Candidate_):
# Adding a star (*) before the,parameter name in the function, receive a tuple of arguments and can access items with indexes
    print(Candidate_)
name("kartheek","Kumar","Ravi")
name(67,89,45)
<---------------------------------------------------------------------------------------------------------------------------------------------------->

def Prime_num(num,count):
    for i in range(1,num+1):
        if num % i == 0:
            count += 1
    if count == 2:
        print(f"{num} is a Prime Number")
    else:
        print(f"{num} is not a Prime Number")
Prime_num(num = int(input("Enter the Number: ")), count = 0)#key Word arguments - as like dictionary here we have key and value directly in the argyments

'''


